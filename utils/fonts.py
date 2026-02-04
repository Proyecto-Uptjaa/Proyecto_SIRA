from PySide6.QtGui import QFontDatabase, QFont
from PySide6.QtWidgets import QApplication
from paths import resource_path
import os


class FontManager:
    """Gestor de fuentes personalizadas"""
    
    _fuentes_cargadas = False
    _font_ids = {}
    _familia_principal = None
    
    # Mapeo de pesos a archivos de fuente
    VARIANTES = {
        "Thin": "Inter_18pt-Thin.ttf",
        "ExtraLight": "Inter_18pt-ExtraLight.ttf",
        "Light": "Inter_18pt-Light.ttf",
        "Regular": "Inter_18pt-Regular.ttf",
        "Medium": "Inter_18pt-Medium.ttf",
        "SemiBold": "Inter_18pt-SemiBold.ttf",
        "Bold": "Inter_18pt-Bold.ttf",
        "ExtraBold": "Inter_18pt-ExtraBold.ttf",
        "Black": "Inter_18pt-Black.ttf",
    }
    
    @classmethod
    def cargar_fuentes(cls) -> bool:
        """Carga todas las variantes de la fuente Inter."""
        if cls._fuentes_cargadas:
            return True
        
        exito = True
        
        for nombre, archivo in cls.VARIANTES.items():
            ruta = resource_path(f"resources/fonts/{archivo}")
            
            if not os.path.exists(ruta):
                print(f"⚠️  Advertencia: No se encontró {archivo}")
                exito = False
                continue
            
            font_id = QFontDatabase.addApplicationFont(ruta)
            
            if font_id == -1:
                print(f"❌ Error al cargar {archivo}")
                exito = False
            else:
                cls._font_ids[nombre] = font_id
                
                # Guardar la familia principal (todas deberían ser "Inter")
                if cls._familia_principal is None:
                    familias = QFontDatabase.applicationFontFamilies(font_id)
                    if familias:
                        cls._familia_principal = familias[0]
        
        cls._fuentes_cargadas = True
        return exito
    
    @classmethod
    def aplicar_fuente_global(cls, app: QApplication, tamaño: int = 10):
        """Aplica la fuente Inter como fuente global de la aplicación."""
        if not cls._fuentes_cargadas:
            cls.cargar_fuentes()
        
        if cls._familia_principal:
            fuente = QFont(cls._familia_principal, tamaño)
            fuente.setWeight(QFont.Weight.Normal)
            app.setFont(fuente)
            print(f"✓ Fuente global aplicada: {cls._familia_principal} {tamaño}pt")
        else:
            # Fallback: intentar usar "Inter" directamente
            fuente = QFont("Inter", tamaño)
            app.setFont(fuente)
            print("⚠️ Usando fuente fallback: Inter")
    
    @classmethod
    def obtener_fuente(cls, peso: str = "Regular", tamaño: int = 10) -> QFont:
        """Obtiene una instancia de QFont con la variante especificada."""
        if not cls._fuentes_cargadas:
            cls.cargar_fuentes()
        
        # Mapeo de nombres de peso a QFont.Weight
        pesos_qt = {
            "Thin": QFont.Weight.Thin,
            "ExtraLight": QFont.Weight.ExtraLight,
            "Light": QFont.Weight.Light,
            "Regular": QFont.Weight.Normal,
            "Medium": QFont.Weight.Medium,
            "SemiBold": QFont.Weight.DemiBold,
            "Bold": QFont.Weight.Bold,
            "ExtraBold": QFont.Weight.ExtraBold,
            "Black": QFont.Weight.Black,
        }
        
        familia = cls._familia_principal or "Inter"
        fuente = QFont(familia, tamaño)
        
        if peso in pesos_qt:
            fuente.setWeight(pesos_qt[peso])
        
        return fuente
    
    @classmethod
    def fuente_regular(cls, tamaño: int = 10) -> QFont:
        """Atajo para obtener fuente Regular."""
        return cls.obtener_fuente("Regular", tamaño)
    
    @classmethod
    def fuente_medium(cls, tamaño: int = 10) -> QFont:
        """Atajo para obtener fuente Medium."""
        return cls.obtener_fuente("Medium", tamaño)
    
    @classmethod
    def fuente_semibold(cls, tamaño: int = 10) -> QFont:
        """Atajo para obtener fuente SemiBold."""
        return cls.obtener_fuente("SemiBold", tamaño)
    
    @classmethod
    def fuente_bold(cls, tamaño: int = 10) -> QFont:
        """Atajo para obtener fuente Bold."""
        return cls.obtener_fuente("Bold", tamaño)
