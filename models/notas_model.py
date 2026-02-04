from utils.db import get_connection
from models.auditoria_model import AuditoriaModel
from typing import Optional, Dict, List, Tuple
from decimal import Decimal


class NotasModel:
    """Modelo de notas (solo aplica para Primaria)"""

    # Notas literales válidas (A-E para Primaria)
    NOTAS_LITERALES_VALIDAS = ["A", "B", "C", "D", "E"]
    
    # Nota mínima para aprobar (literal)
    NOTA_MINIMA_APROBATORIA = "C"  # A, B, C son aprobatorias; D, E son reprobatorias

    @staticmethod
    def registrar_nota(
        estudiante_id: int,
        seccion_materia_id: int,
        lapso: int,
        nota: float = None,
        nota_literal: str = None,
        observaciones: str = None,
        usuario_actual: dict = None
    ) -> Tuple[bool, str]:
        """Registra o actualiza una nota para un estudiante."""
        
        # Validaciones
        if lapso not in (1, 2, 3):
            return False, "El lapso debe ser 1, 2 o 3."
        
        if nota is not None:
            if not (0 <= nota <= 20):
                return False, "La nota debe estar entre 0 y 20."
        
        if nota_literal is not None:
            if nota_literal.upper() not in NotasModel.NOTAS_LITERALES_VALIDAS:
                return False, f"Nota literal inválida. Valores permitidos: {', '.join(NotasModel.NOTAS_LITERALES_VALIDAS)}"
            nota_literal = nota_literal.upper()
        
        if nota is None and nota_literal is None:
            return False, "Debe proporcionar una nota numérica o literal."
        
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return False, "Error de conexión a la base de datos."
            
            cursor = conexion.cursor(dictionary=True)
            
            # Verificar que existe la relación estudiante-sección-materia válida
            cursor.execute("""
                SELECT sm.id, m.nombre as materia, m.tipo_evaluacion,
                       e.nombres, e.apellidos, s.grado, s.letra
                FROM seccion_materia sm
                JOIN materias m ON sm.materia_id = m.id
                JOIN secciones s ON sm.seccion_id = s.id
                JOIN seccion_estudiante se ON se.seccion_id = s.id
                JOIN estudiantes e ON se.estudiante_id = e.id
                WHERE sm.id = %s AND e.id = %s
            """, (seccion_materia_id, estudiante_id))
            
            info = cursor.fetchone()
            if not info:
                return False, "El estudiante no está asignado a esta sección/materia."
            
            # Validar tipo de nota según materia
            if info["tipo_evaluacion"] == "literal" and nota is not None:
                return False, f"La materia '{info['materia']}' requiere nota literal (A, B, C...)."
            if info["tipo_evaluacion"] == "numerico" and nota_literal is not None:
                return False, f"La materia '{info['materia']}' requiere nota numérica."
            
            # Insertar o actualizar
            cursor.execute("""
                INSERT INTO notas (estudiante_id, seccion_materia_id, lapso, 
                                   nota, nota_literal, observaciones, registrado_por)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                    nota = VALUES(nota),
                    nota_literal = VALUES(nota_literal),
                    observaciones = VALUES(observaciones),
                    fecha_registro = CURRENT_TIMESTAMP,
                    registrado_por = VALUES(registrado_por)
            """, (
                estudiante_id, seccion_materia_id, lapso,
                nota, nota_literal, observaciones,
                usuario_actual["id"] if usuario_actual else None
            ))
            
            conexion.commit()
            
            return True, "Nota registrada correctamente."
            
        except Exception as e:
            if conexion:
                conexion.rollback()
            return False, f"Error al registrar nota: {str(e)}"
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def registrar_notas_masivo(
        notas_data: List[Dict],
        usuario_actual: dict
    ) -> Tuple[bool, str, int]:
        """Registra múltiples notas en una sola transacción."""
        
        if not notas_data:
            return False, "No hay notas para registrar.", 0
        
        if not usuario_actual or "id" not in usuario_actual:
            return False, "Usuario no válido.", 0
        
        conexion = None
        cursor = None
        registradas = 0
        
        try:
            conexion = get_connection()
            if not conexion:
                return False, "Error de conexión a la base de datos.", 0
            
            cursor = conexion.cursor(dictionary=True)
            conexion.start_transaction()
            
            # Conjunto para rastrear combinaciones estudiante-materia que necesitan cálculo final
            combinaciones_afectadas = set()
            
            for nota_info in notas_data:
                estudiante_id = nota_info.get("estudiante_id")
                seccion_materia_id = nota_info.get("seccion_materia_id")
                lapso = nota_info.get("lapso")
                nota = nota_info.get("nota")
                nota_literal = nota_info.get("nota_literal")
                observaciones = nota_info.get("observaciones")
                
                # Saltar si no hay nota que registrar
                if nota is None and nota_literal is None:
                    continue
                
                # Validar lapso
                if lapso not in (1, 2, 3):
                    continue
                
                # Convertir nota literal a mayúsculas
                if nota_literal:
                    nota_literal = nota_literal.upper()
                
                cursor.execute("""
                    INSERT INTO notas (estudiante_id, seccion_materia_id, lapso, 
                                       nota, nota_literal, observaciones, registrado_por)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    ON DUPLICATE KEY UPDATE
                        nota = VALUES(nota),
                        nota_literal = VALUES(nota_literal),
                        observaciones = VALUES(observaciones),
                        fecha_registro = CURRENT_TIMESTAMP,
                        registrado_por = VALUES(registrado_por)
                """, (
                    estudiante_id, seccion_materia_id, lapso,
                    nota, nota_literal, observaciones,
                    usuario_actual["id"]
                ))
                registradas += 1
                
                # Registrar combinación afectada para calcular nota final después
                combinaciones_afectadas.add((estudiante_id, seccion_materia_id))
            
            # Calcular notas finales para estudiantes que completaron 3 lapsos
            notas_finales_calculadas = 0
            for estudiante_id, seccion_materia_id in combinaciones_afectadas:
                # Verificar si tiene los 3 lapsos completos
                cursor.execute("""
                    SELECT 
                        COUNT(*) as total,
                        COUNT(CASE WHEN nota IS NOT NULL THEN 1 END) as notas_numericas,
                        COUNT(CASE WHEN nota_literal IS NOT NULL THEN 1 END) as notas_literales
                    FROM notas
                    WHERE estudiante_id = %s 
                      AND seccion_materia_id = %s
                """, (estudiante_id, seccion_materia_id))
                
                resultado = cursor.fetchone()
                if not resultado or resultado['total'] < 3:
                    continue  # No tiene 3 lapsos completos
                
                # Determinar tipo de notas
                tiene_numericas = resultado['notas_numericas'] > 0
                tiene_literales = resultado['notas_literales'] > 0
                
                if tiene_numericas and not tiene_literales:
                    # Calcular promedio numérico
                    cursor.execute("""
                        SELECT AVG(nota) as promedio
                        FROM notas
                        WHERE estudiante_id = %s AND seccion_materia_id = %s
                        AND nota IS NOT NULL
                    """, (estudiante_id, seccion_materia_id))
                    
                    prom = cursor.fetchone()
                    if prom and prom['promedio']:
                        nota_final = round(float(prom['promedio']), 2)
                        aprobado = 1 if nota_final >= 10 else 0
                        
                        cursor.execute("""
                            INSERT INTO notas_finales 
                                (estudiante_id, seccion_materia_id, nota_final, aprobado, calculado_por)
                            VALUES (%s, %s, %s, %s, %s)
                            ON DUPLICATE KEY UPDATE
                                nota_final = VALUES(nota_final),
                                aprobado = VALUES(aprobado),
                                fecha_calculo = CURRENT_TIMESTAMP,
                                calculado_por = VALUES(calculado_por)
                        """, (estudiante_id, seccion_materia_id, nota_final, aprobado, 
                              usuario_actual["id"]))
                        notas_finales_calculadas += 1
                
                elif tiene_literales:
                    # Calcular promedio de notas literales (A-E)
                    cursor.execute("""
                        SELECT nota_literal
                        FROM notas
                        WHERE estudiante_id = %s AND seccion_materia_id = %s
                        AND nota_literal IS NOT NULL
                        ORDER BY lapso
                    """, (estudiante_id, seccion_materia_id))
                    
                    notas_lit = cursor.fetchall()
                    if len(notas_lit) >= 3:
                        # Convertir letras a valores numéricos
                        valores_literales = {'A': 5, 'B': 4, 'C': 3, 'D': 2, 'E': 1}
                        letras_valores = {5: 'A', 4: 'B', 3: 'C', 2: 'D', 1: 'E'}
                        
                        valores = []
                        for n in notas_lit[:3]:  # Solo primeros 3
                            letra = n['nota_literal']
                            if letra in valores_literales:
                                valores.append(valores_literales[letra])
                        
                        if len(valores) == 3:
                            # Calcular promedio y redondear
                            promedio = sum(valores) / len(valores)
                            valor_final = round(promedio)
                            nota_final_lit = letras_valores.get(valor_final, 'E')
                            aprobado = 1 if nota_final_lit in ['A', 'B', 'C'] else 0
                            
                            cursor.execute("""
                                INSERT INTO notas_finales 
                                    (estudiante_id, seccion_materia_id, nota_final_literal, aprobado, calculado_por)
                                VALUES (%s, %s, %s, %s, %s)
                                ON DUPLICATE KEY UPDATE
                                    nota_final_literal = VALUES(nota_final_literal),
                                    aprobado = VALUES(aprobado),
                                    fecha_calculo = CURRENT_TIMESTAMP,
                                    calculado_por = VALUES(calculado_por)
                            """, (estudiante_id, seccion_materia_id, nota_final_lit, aprobado, 
                                  usuario_actual["id"]))
                            notas_finales_calculadas += 1
            
            conexion.commit()
            
            # Auditoría (una sola entrada para el lote)
            if registradas > 0:
                descripcion = f"Se registraron {registradas} notas"
                if notas_finales_calculadas > 0:
                    descripcion += f" y se calcularon {notas_finales_calculadas} notas finales automáticamente"
                
                AuditoriaModel.registrar(
                    usuario_id=usuario_actual["id"],
                    accion="INSERT",
                    entidad="notas",
                    entidad_id=seccion_materia_id,
                    referencia="Registro masivo",
                    descripcion=descripcion
                )
            
            mensaje = f"{registradas} notas registradas correctamente."
            if notas_finales_calculadas > 0:
                mensaje += f" Se calcularon {notas_finales_calculadas} notas finales automáticamente."
            
            return True, mensaje, registradas
            
        except Exception as e:
            if conexion:
                conexion.rollback()
            return False, f"Error al registrar notas: {str(e)}", 0
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def obtener_notas_seccion_materia(
        seccion_id: int,
        materia_id: int = None,
        lapso: int = None
    ) -> List[Dict]:
        """
        Obtiene las notas de todos los estudiantes de una sección.
        Incluye estudiantes sin notas para facilitar la carga.
        """
        
        if not isinstance(seccion_id, int) or seccion_id <= 0:
            return []
        
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return []
            
            cursor = conexion.cursor(dictionary=True)
            
            # Obtener estudiantes de la sección
            query = """
                SELECT 
                    e.id as estudiante_id,
                    e.cedula,
                    e.nombres,
                    e.apellidos,
                    CONCAT(e.apellidos, ', ', e.nombres) as nombre_completo,
                    sm.id as seccion_materia_id,
                    m.id as materia_id,
                    m.nombre as materia,
                    m.tipo_evaluacion,
                    n.nota as lapso_1,
                    n2.nota as lapso_2,
                    n3.nota as lapso_3,
                    n.nota_literal as lapso_1_lit,
                    n2.nota_literal as lapso_2_lit,
                    n3.nota_literal as lapso_3_lit,
                    nf.nota_final,
                    nf.nota_final_literal,
                    nf.aprobado
                FROM seccion_estudiante se
                JOIN estudiantes e ON se.estudiante_id = e.id
                JOIN seccion_materia sm ON sm.seccion_id = se.seccion_id
                JOIN materias m ON sm.materia_id = m.id
                LEFT JOIN notas n ON n.estudiante_id = e.id 
                    AND n.seccion_materia_id = sm.id AND n.lapso = 1
                LEFT JOIN notas n2 ON n2.estudiante_id = e.id 
                    AND n2.seccion_materia_id = sm.id AND n2.lapso = 2
                LEFT JOIN notas n3 ON n3.estudiante_id = e.id 
                    AND n3.seccion_materia_id = sm.id AND n3.lapso = 3
                LEFT JOIN notas_finales nf ON nf.estudiante_id = e.id 
                    AND nf.seccion_materia_id = sm.id
                WHERE se.seccion_id = %s AND e.estado = 1
            """
            params = [seccion_id]
            
            if materia_id:
                query += " AND m.id = %s"
                params.append(materia_id)
            
            query += " ORDER BY e.apellidos, e.nombres, m.nombre"
            
            cursor.execute(query, tuple(params))
            resultados = cursor.fetchall()
            
            # Convertir Decimal a float para JSON
            for r in resultados:
                for key in ['lapso_1', 'lapso_2', 'lapso_3', 'nota_final']:
                    if r.get(key) is not None and isinstance(r[key], Decimal):
                        r[key] = float(r[key])
            
            return resultados
            
        except Exception as e:
            print(f"Error al obtener notas de sección: {e}")
            return []
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def obtener_notas_estudiante(estudiante_id: int) -> List[Dict]:
        """
        Obtiene todas las notas históricas de un estudiante.
        Ordenadas por año escolar y materia.
        """
        if not isinstance(estudiante_id, int) or estudiante_id <= 0:
            return []
        
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return []
            
            cursor = conexion.cursor(dictionary=True)
            
            cursor.execute("""
                SELECT 
                    ae.nombre as año_escolar,
                    ae.año_inicio,
                    s.nivel,
                    s.grado,
                    s.letra,
                    m.nombre as materia,
                    m.tipo_evaluacion,
                    n1.nota as lapso_1,
                    n1.nota_literal as lapso_1_lit,
                    n2.nota as lapso_2,
                    n2.nota_literal as lapso_2_lit,
                    n3.nota as lapso_3,
                    n3.nota_literal as lapso_3_lit,
                    nf.nota_final,
                    nf.nota_final_literal,
                    nf.aprobado
                FROM seccion_materia sm
                JOIN secciones s ON sm.seccion_id = s.id
                JOIN años_escolares ae ON s.año_escolar_id = ae.id
                JOIN materias m ON sm.materia_id = m.id
                LEFT JOIN notas n1 ON n1.estudiante_id = %s 
                    AND n1.seccion_materia_id = sm.id AND n1.lapso = 1
                LEFT JOIN notas n2 ON n2.estudiante_id = %s 
                    AND n2.seccion_materia_id = sm.id AND n2.lapso = 2
                LEFT JOIN notas n3 ON n3.estudiante_id = %s 
                    AND n3.seccion_materia_id = sm.id AND n3.lapso = 3
                LEFT JOIN notas_finales nf ON nf.estudiante_id = %s 
                    AND nf.seccion_materia_id = sm.id
                WHERE EXISTS (
                    SELECT 1 FROM historial_secciones hs 
                    WHERE hs.estudiante_id = %s AND hs.seccion_id = s.id
                )
                AND (n1.id IS NOT NULL OR n2.id IS NOT NULL OR n3.id IS NOT NULL)
                ORDER BY ae.año_inicio DESC, m.nombre
            """, (estudiante_id, estudiante_id, estudiante_id, estudiante_id, estudiante_id))
            
            resultados = cursor.fetchall()
            
            # Convertir Decimal a float
            for r in resultados:
                for key in ['lapso_1', 'lapso_2', 'lapso_3', 'nota_final']:
                    if r.get(key) is not None and isinstance(r[key], Decimal):
                        r[key] = float(r[key])
            
            return resultados
            
        except Exception as e:
            print(f"Error al obtener notas del estudiante: {e}")
            return []
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def calcular_nota_final(
        estudiante_id: int,
        seccion_materia_id: int,
        usuario_actual: dict
    ) -> Tuple[bool, str]:
        """Calcula y guarda la nota final de un estudiante para una materia."""
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return False, "Error de conexión."
            
            cursor = conexion.cursor(dictionary=True)
            
            # Obtener tipo de evaluación
            cursor.execute("""
                SELECT m.tipo_evaluacion
                FROM seccion_materia sm
                JOIN materias m ON sm.materia_id = m.id
                WHERE sm.id = %s
            """, (seccion_materia_id,))
            materia_info = cursor.fetchone()
            
            if not materia_info:
                return False, "Materia no encontrada."
            
            tipo_eval = materia_info["tipo_evaluacion"]
            
            # Detectar qué tipo de notas tiene registradas
            cursor.execute("""
                SELECT 
                    COUNT(CASE WHEN nota IS NOT NULL THEN 1 END) as notas_numericas,
                    COUNT(CASE WHEN nota_literal IS NOT NULL THEN 1 END) as notas_literales
                FROM notas
                WHERE estudiante_id = %s AND seccion_materia_id = %s
            """, (estudiante_id, seccion_materia_id))
            
            tipo_notas = cursor.fetchone()
            tiene_numericas = tipo_notas["notas_numericas"] > 0
            tiene_literales = tipo_notas["notas_literales"] > 0
            
            # Decidir qué tipo de cálculo usar basado en las notas registradas
            if tiene_numericas and not tiene_literales:
                # Calcular promedio numérico
                cursor.execute("""
                    SELECT AVG(nota) as promedio, COUNT(*) as cantidad
                    FROM notas
                    WHERE estudiante_id = %s AND seccion_materia_id = %s
                    AND nota IS NOT NULL
                """, (estudiante_id, seccion_materia_id))
                
                resultado = cursor.fetchone()
                if not resultado or resultado["cantidad"] == 0:
                    return False, "No hay notas registradas para calcular."
                
                nota_final = round(float(resultado["promedio"]), 2)
                aprobado = 1 if nota_final >= NotasModel.NOTA_MINIMA_APROBATORIA else 0
                
                cursor.execute("""
                    INSERT INTO notas_finales 
                        (estudiante_id, seccion_materia_id, nota_final, aprobado, calculado_por)
                    VALUES (%s, %s, %s, %s, %s)
                    ON DUPLICATE KEY UPDATE
                        nota_final = VALUES(nota_final),
                        aprobado = VALUES(aprobado),
                        fecha_calculo = CURRENT_TIMESTAMP,
                        calculado_por = VALUES(calculado_por)
                """, (estudiante_id, seccion_materia_id, nota_final, aprobado, 
                      usuario_actual["id"]))
                
            elif tiene_literales:
                # Para literal, calcular promedio de los tres lapsos
                cursor.execute("""
                    SELECT 
                        n1.nota_literal as lapso_1,
                        n2.nota_literal as lapso_2,
                        n3.nota_literal as lapso_3
                    FROM notas n1
                    LEFT JOIN notas n2 ON n2.estudiante_id = n1.estudiante_id 
                        AND n2.seccion_materia_id = n1.seccion_materia_id AND n2.lapso = 2
                    LEFT JOIN notas n3 ON n3.estudiante_id = n1.estudiante_id 
                        AND n3.seccion_materia_id = n1.seccion_materia_id AND n3.lapso = 3
                    WHERE n1.estudiante_id = %s AND n1.seccion_materia_id = %s AND n1.lapso = 1
                """, (estudiante_id, seccion_materia_id))
                
                resultado = cursor.fetchone()
                if not resultado:
                    return False, "No hay notas registradas para calcular."
                
                # Convertir letras a valores numéricos
                valores_literales = {'A': 5, 'B': 4, 'C': 3, 'D': 2, 'E': 1}
                letras_valores = {5: 'A', 4: 'B', 3: 'C', 2: 'D', 1: 'E'}
                
                notas_numericas = []
                for lapso in ['lapso_1', 'lapso_2', 'lapso_3']:
                    nota_lit = resultado.get(lapso)
                    if nota_lit and nota_lit in valores_literales:
                        notas_numericas.append(valores_literales[nota_lit])
                
                if not notas_numericas:
                    return False, "No hay notas literales válidas para calcular."
                
                # Calcular promedio y redondear
                promedio = sum(notas_numericas) / len(notas_numericas)
                promedio_redondeado = round(promedio)
                
                # Convertir de vuelta a literal
                nota_literal = letras_valores.get(promedio_redondeado, 'E')
                
                # A, B, C = aprobado; D, E = reprobado
                aprobado = 1 if nota_literal in ("A", "B", "C") else 0
                
                cursor.execute("""
                    INSERT INTO notas_finales 
                        (estudiante_id, seccion_materia_id, nota_final_literal, aprobado, calculado_por)
                    VALUES (%s, %s, %s, %s, %s)
                    ON DUPLICATE KEY UPDATE
                        nota_final_literal = VALUES(nota_final_literal),
                        aprobado = VALUES(aprobado),
                        fecha_calculo = CURRENT_TIMESTAMP,
                        calculado_por = VALUES(calculado_por)
                """, (estudiante_id, seccion_materia_id, nota_literal, aprobado,
                      usuario_actual["id"]))
            
            else:
                return False, "No hay notas registradas (ni numéricas ni literales)."
            
            conexion.commit()
            return True, "Nota final calculada correctamente."
            
        except Exception as e:
            if conexion:
                conexion.rollback()
            return False, f"Error al calcular nota final: {str(e)}"
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def calcular_notas_finales_seccion(
        seccion_id: int,
        materia_id: int,
        usuario_actual: dict
    ) -> Tuple[bool, str, int]:
        """
        Calcula las notas finales de todos los estudiantes de una sección para una materia.
        """
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return False, "Error de conexión.", 0
            
            cursor = conexion.cursor(dictionary=True)
            
            # Obtener seccion_materia_id
            cursor.execute("""
                SELECT id FROM seccion_materia
                WHERE seccion_id = %s AND materia_id = %s
            """, (seccion_id, materia_id))
            sm = cursor.fetchone()
            if not sm:
                return False, "Materia no asignada a esta sección.", 0
            
            seccion_materia_id = sm["id"]
            
            # Obtener estudiantes
            cursor.execute("""
                SELECT estudiante_id FROM seccion_estudiante
                WHERE seccion_id = %s
            """, (seccion_id,))
            estudiantes = cursor.fetchall()
            
            calculadas = 0
            for est in estudiantes:
                ok, _ = NotasModel.calcular_nota_final(
                    est["estudiante_id"],
                    seccion_materia_id,
                    usuario_actual
                )
                if ok:
                    calculadas += 1
            
            return True, f"{calculadas} notas finales calculadas.", calculadas
            
        except Exception as e:
            return False, f"Error: {str(e)}", 0
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def obtener_estadisticas_seccion(seccion_id: int, materia_id: int = None) -> Dict:
        """
        Obtiene estadísticas de notas de una sección.
        """
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return {}
            
            cursor = conexion.cursor(dictionary=True)
            
            query = """
                SELECT 
                    COUNT(DISTINCT e.id) as total_estudiantes,
                    COUNT(DISTINCT n.id) as notas_registradas,
                    AVG(n.nota) as promedio_general,
                    MIN(n.nota) as nota_minima,
                    MAX(n.nota) as nota_maxima,
                    SUM(CASE WHEN n.nota >= 10 THEN 1 ELSE 0 END) as aprobados,
                    SUM(CASE WHEN n.nota < 10 THEN 1 ELSE 0 END) as reprobados
                FROM seccion_estudiante se
                JOIN estudiantes e ON se.estudiante_id = e.id
                JOIN seccion_materia sm ON sm.seccion_id = se.seccion_id
                LEFT JOIN notas n ON n.estudiante_id = e.id AND n.seccion_materia_id = sm.id
                WHERE se.seccion_id = %s AND e.estado = 1
            """
            params = [seccion_id]
            
            if materia_id:
                query += " AND sm.materia_id = %s"
                params.append(materia_id)
            
            cursor.execute(query, tuple(params))
            stats = cursor.fetchone()
            
            # Convertir Decimal
            if stats:
                for key in ['promedio_general', 'nota_minima', 'nota_maxima']:
                    if stats.get(key) is not None and isinstance(stats[key], Decimal):
                        stats[key] = round(float(stats[key]), 2)
            
            return stats or {}
            
        except Exception as e:
            print(f"Error al obtener estadísticas: {e}")
            return {}
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def obtener_boletin_estudiante(
        estudiante_id: int,
        año_escolar_id: int = None
    ) -> Dict:
        """Obtiene datos para generar el boletín de un estudiante."""
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return {}
            
            cursor = conexion.cursor(dictionary=True)
            
            # Datos del estudiante
            cursor.execute("""
                SELECT e.*, 
                       CONCAT(e.nombres, ' ', e.apellidos) as nombre_completo,
                       r.nombres as repr_nombres, r.apellidos as repr_apellidos,
                       r.cedula as repr_cedula
                FROM estudiantes e
                LEFT JOIN representantes r ON e.representante_id = r.id
                WHERE e.id = %s
            """, (estudiante_id,))
            estudiante = cursor.fetchone()
            
            if not estudiante:
                return {}
            
            # Obtener sección actual o del año especificado
            query_seccion = """
                SELECT s.*, ae.nombre as año_escolar,
                       CONCAT(emp.nombres, ' ', emp.apellidos) as docente
                FROM seccion_estudiante se
                JOIN secciones s ON se.seccion_id = s.id
                JOIN años_escolares ae ON s.año_escolar_id = ae.id
                LEFT JOIN empleados emp ON s.docente_id = emp.id
                WHERE se.estudiante_id = %s
            """
            if año_escolar_id:
                query_seccion += " AND s.año_escolar_id = %s"
                cursor.execute(query_seccion, (estudiante_id, año_escolar_id))
            else:
                query_seccion += " AND ae.es_actual = 1"
                cursor.execute(query_seccion, (estudiante_id,))
            
            seccion = cursor.fetchone()
            
            if not seccion:
                return {"estudiante": estudiante, "seccion": None, "notas": []}
            
            # Obtener notas
            cursor.execute("""
                SELECT 
                    m.nombre as materia,
                    m.tipo_evaluacion,
                    n1.nota as lapso_1,
                    n1.nota_literal as lapso_1_lit,
                    n2.nota as lapso_2,
                    n2.nota_literal as lapso_2_lit,
                    n3.nota as lapso_3,
                    n3.nota_literal as lapso_3_lit,
                    nf.nota_final,
                    nf.nota_final_literal,
                    nf.aprobado
                FROM seccion_materia sm
                JOIN materias m ON sm.materia_id = m.id
                LEFT JOIN notas n1 ON n1.estudiante_id = %s 
                    AND n1.seccion_materia_id = sm.id AND n1.lapso = 1
                LEFT JOIN notas n2 ON n2.estudiante_id = %s 
                    AND n2.seccion_materia_id = sm.id AND n2.lapso = 2
                LEFT JOIN notas n3 ON n3.estudiante_id = %s 
                    AND n3.seccion_materia_id = sm.id AND n3.lapso = 3
                LEFT JOIN notas_finales nf ON nf.estudiante_id = %s 
                    AND nf.seccion_materia_id = sm.id
                WHERE sm.seccion_id = %s
                ORDER BY m.nombre
            """, (estudiante_id, estudiante_id, estudiante_id, estudiante_id, seccion["id"]))
            
            notas = cursor.fetchall()
            
            # Convertir Decimal a float
            for n in notas:
                for key in ['lapso_1', 'lapso_2', 'lapso_3', 'nota_final']:
                    if n.get(key) is not None and isinstance(n[key], Decimal):
                        n[key] = float(n[key])
            
            return {
                "estudiante": estudiante,
                "seccion": seccion,
                "notas": notas
            }
            
        except Exception as e:
            print(f"Error al obtener boletín: {e}")
            return {}
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()
