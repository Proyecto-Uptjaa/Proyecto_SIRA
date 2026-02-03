-- MySQL dump 10.13  Distrib 8.0.36, for Linux (x86_64)
--
-- Host: localhost    Database: SIRA_DB
-- ------------------------------------------------------
-- Server version	8.0.44-0ubuntu0.24.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auditoria`
--

DROP TABLE IF EXISTS `auditoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auditoria` (
  `id` int NOT NULL AUTO_INCREMENT,
  `usuario_id` int NOT NULL,
  `accion` varchar(100) NOT NULL,
  `entidad` varchar(50) NOT NULL,
  `entidad_id` int NOT NULL,
  `referencia` varchar(150) DEFAULT NULL,
  `descripcion` text,
  `fecha` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `usuario_id` (`usuario_id`),
  CONSTRAINT `auditoria_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=354 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `años_escolares`
--

DROP TABLE IF EXISTS `años_escolares`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `años_escolares` (
  `id` int NOT NULL AUTO_INCREMENT,
  `año_inicio` year NOT NULL,
  `año_fin` year NOT NULL,
  `nombre` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `fecha_inicio` date DEFAULT NULL,
  `fecha_fin` date DEFAULT NULL,
  `estado` enum('planificado','activo','cerrado') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT 'planificado',
  `es_actual` tinyint(1) DEFAULT '0',
  `creado_en` datetime DEFAULT CURRENT_TIMESTAMP,
  `cerrado_en` datetime DEFAULT NULL,
  `creado_por` int DEFAULT NULL,
  `cerrado_por` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_anio` (`año_inicio`),
  KEY `creado_por` (`creado_por`),
  KEY `cerrado_por` (`cerrado_por`),
  CONSTRAINT `años_escolares_ibfk_1` FOREIGN KEY (`creado_por`) REFERENCES `usuarios` (`id`),
  CONSTRAINT `años_escolares_ibfk_2` FOREIGN KEY (`cerrado_por`) REFERENCES `usuarios` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `empleados`
--

DROP TABLE IF EXISTS `empleados`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `empleados` (
  `id` int NOT NULL AUTO_INCREMENT,
  `cedula` varchar(10) NOT NULL,
  `nombres` varchar(100) NOT NULL,
  `apellidos` varchar(100) NOT NULL,
  `fecha_nac` date NOT NULL,
  `genero` varchar(1) NOT NULL,
  `direccion` varchar(100) DEFAULT NULL,
  `num_contact` varchar(11) DEFAULT NULL,
  `correo` varchar(100) DEFAULT NULL,
  `titulo` varchar(30) NOT NULL,
  `cargo` varchar(30) NOT NULL,
  `fecha_ingreso` date NOT NULL,
  `num_carnet` varchar(20) DEFAULT NULL,
  `rif` varchar(15) DEFAULT NULL,
  `centro_votacion` varchar(50) DEFAULT NULL,
  `estado` tinyint(1) NOT NULL DEFAULT '1',
  `codigo_rac` varchar(10) DEFAULT NULL,
  `horas_acad` decimal(4,2) DEFAULT NULL,
  `horas_adm` decimal(4,2) DEFAULT NULL,
  `especialidad` varchar(200) DEFAULT NULL,
  `tipo_personal` varchar(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `cedula` (`cedula`)
) ENGINE=InnoDB AUTO_INCREMENT=76 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `estudiantes`
--

DROP TABLE IF EXISTS `estudiantes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `estudiantes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `cedula` varchar(15) DEFAULT NULL,
  `nombres` varchar(100) NOT NULL,
  `apellidos` varchar(100) NOT NULL,
  `fecha_nac` date NOT NULL,
  `ciudad` varchar(50) NOT NULL,
  `genero` varchar(1) NOT NULL,
  `direccion` varchar(100) NOT NULL,
  `fecha_ingreso` date DEFAULT NULL,
  `tallaC` varchar(2) DEFAULT NULL,
  `tallaP` varchar(2) DEFAULT NULL,
  `tallaZ` varchar(2) DEFAULT NULL,
  `padre` varchar(100) DEFAULT NULL,
  `padre_ci` varchar(9) DEFAULT NULL,
  `ocupacion_padre` varchar(200) DEFAULT NULL,
  `madre` varchar(100) DEFAULT NULL,
  `madre_ci` varchar(9) DEFAULT NULL,
  `ocupacion_madre` varchar(200) DEFAULT NULL,
  `representante_id` int NOT NULL,
  `estado` tinyint(1) NOT NULL DEFAULT '1',
  `estatus_academico` varchar(20) DEFAULT 'Regular',
  `motivo_retiro` text COMMENT 'Motivo del retiro del estudiante',
  `fecha_retiro` date DEFAULT NULL COMMENT 'Fecha en que se retiró el estudiante',
  PRIMARY KEY (`id`),
  UNIQUE KEY `cedula` (`cedula`),
  KEY `fk_representante` (`representante_id`),
  CONSTRAINT `fk_representante` FOREIGN KEY (`representante_id`) REFERENCES `representantes` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=612 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `historial_secciones`
--

DROP TABLE IF EXISTS `historial_secciones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `historial_secciones` (
  `id` int NOT NULL AUTO_INCREMENT,
  `estudiante_id` int NOT NULL,
  `seccion_id` int NOT NULL,
  `año_inicio` year NOT NULL DEFAULT '2025',
  `fecha_asignacion` date DEFAULT (curdate()),
  `fecha_retiro` date DEFAULT NULL,
  `observaciones` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uniq_estudiante_año` (`estudiante_id`,`año_inicio`),
  KEY `seccion_id` (`seccion_id`),
  CONSTRAINT `historial_secciones_ibfk_1` FOREIGN KEY (`estudiante_id`) REFERENCES `estudiantes` (`id`) ON DELETE CASCADE,
  CONSTRAINT `historial_secciones_ibfk_2` FOREIGN KEY (`seccion_id`) REFERENCES `secciones` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1147 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `institucion`
--

DROP TABLE IF EXISTS `institucion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `institucion` (
  `id` int NOT NULL,
  `nombre` varchar(150) NOT NULL,
  `codigo_dea` varchar(50) DEFAULT NULL,
  `direccion` varchar(200) DEFAULT NULL,
  `telefono` varchar(50) DEFAULT NULL,
  `correo` varchar(100) DEFAULT NULL,
  `logo` longblob,
  `actualizado_en` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `director` varchar(150) NOT NULL,
  `director_ci` varchar(10) NOT NULL,
  `codigo_dependencia` varchar(30) DEFAULT NULL,
  `codigo_estadistico` varchar(30) DEFAULT NULL,
  `rif` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `materia_grado`
--

DROP TABLE IF EXISTS `materia_grado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `materia_grado` (
  `id` int NOT NULL AUTO_INCREMENT,
  `materia_id` int NOT NULL,
  `nivel` enum('Inicial','Primaria') COLLATE utf8mb4_general_ci NOT NULL,
  `grado` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_materia_nivel_grado` (`materia_id`,`nivel`,`grado`),
  CONSTRAINT `materia_grado_ibfk_1` FOREIGN KEY (`materia_id`) REFERENCES `materias` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `materias`
--

DROP TABLE IF EXISTS `materias`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `materias` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `abreviatura` varchar(10) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `tipo_evaluacion` enum('numerico','literal') COLLATE utf8mb4_general_ci DEFAULT 'numerico',
  `estado` tinyint(1) DEFAULT '1',
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_nombre` (`nombre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `notas`
--

DROP TABLE IF EXISTS `notas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `notas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `estudiante_id` int NOT NULL,
  `seccion_materia_id` int NOT NULL,
  `lapso` tinyint NOT NULL,
  `nota` decimal(4,2) DEFAULT NULL,
  `nota_literal` varchar(5) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `observaciones` text COLLATE utf8mb4_general_ci,
  `fecha_registro` datetime DEFAULT CURRENT_TIMESTAMP,
  `registrado_por` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_nota` (`estudiante_id`,`seccion_materia_id`,`lapso`),
  KEY `seccion_materia_id` (`seccion_materia_id`),
  KEY `registrado_por` (`registrado_por`),
  CONSTRAINT `notas_ibfk_1` FOREIGN KEY (`estudiante_id`) REFERENCES `estudiantes` (`id`) ON DELETE CASCADE,
  CONSTRAINT `notas_ibfk_2` FOREIGN KEY (`seccion_materia_id`) REFERENCES `seccion_materia` (`id`) ON DELETE CASCADE,
  CONSTRAINT `notas_ibfk_3` FOREIGN KEY (`registrado_por`) REFERENCES `usuarios` (`id`),
  CONSTRAINT `notas_chk_1` CHECK ((`lapso` between 1 and 3))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `notas_finales`
--

DROP TABLE IF EXISTS `notas_finales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `notas_finales` (
  `id` int NOT NULL AUTO_INCREMENT,
  `estudiante_id` int NOT NULL,
  `seccion_materia_id` int NOT NULL,
  `nota_final` decimal(4,2) DEFAULT NULL,
  `nota_final_literal` varchar(5) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `aprobado` tinyint(1) DEFAULT NULL,
  `observaciones` text COLLATE utf8mb4_general_ci,
  `fecha_calculo` datetime DEFAULT CURRENT_TIMESTAMP,
  `calculado_por` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_nota_final` (`estudiante_id`,`seccion_materia_id`),
  KEY `seccion_materia_id` (`seccion_materia_id`),
  KEY `calculado_por` (`calculado_por`),
  CONSTRAINT `notas_finales_ibfk_1` FOREIGN KEY (`estudiante_id`) REFERENCES `estudiantes` (`id`) ON DELETE CASCADE,
  CONSTRAINT `notas_finales_ibfk_2` FOREIGN KEY (`seccion_materia_id`) REFERENCES `seccion_materia` (`id`) ON DELETE CASCADE,
  CONSTRAINT `notas_finales_ibfk_3` FOREIGN KEY (`calculado_por`) REFERENCES `usuarios` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `representantes`
--

DROP TABLE IF EXISTS `representantes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `representantes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `cedula` varchar(10) NOT NULL,
  `nombres` varchar(100) NOT NULL,
  `apellidos` varchar(100) NOT NULL,
  `fecha_nac` date DEFAULT NULL,
  `genero` varchar(10) DEFAULT NULL,
  `direccion` varchar(100) DEFAULT NULL,
  `num_contact` varchar(11) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `observacion` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `cedula_repre` (`cedula`)
) ENGINE=InnoDB AUTO_INCREMENT=305 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `seccion_estudiante`
--

DROP TABLE IF EXISTS `seccion_estudiante`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `seccion_estudiante` (
  `seccion_id` int NOT NULL,
  `estudiante_id` int NOT NULL,
  `año_asignacion` year NOT NULL,
  PRIMARY KEY (`seccion_id`,`estudiante_id`),
  KEY `estudiante_id` (`estudiante_id`),
  CONSTRAINT `seccion_estudiante_ibfk_1` FOREIGN KEY (`seccion_id`) REFERENCES `secciones` (`id`) ON DELETE CASCADE,
  CONSTRAINT `seccion_estudiante_ibfk_2` FOREIGN KEY (`estudiante_id`) REFERENCES `estudiantes` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `seccion_materia`
--

DROP TABLE IF EXISTS `seccion_materia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `seccion_materia` (
  `id` int NOT NULL AUTO_INCREMENT,
  `seccion_id` int NOT NULL,
  `materia_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_seccion_materia` (`seccion_id`,`materia_id`),
  KEY `materia_id` (`materia_id`),
  CONSTRAINT `seccion_materia_ibfk_1` FOREIGN KEY (`seccion_id`) REFERENCES `secciones` (`id`) ON DELETE CASCADE,
  CONSTRAINT `seccion_materia_ibfk_2` FOREIGN KEY (`materia_id`) REFERENCES `materias` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `secciones`
--

DROP TABLE IF EXISTS `secciones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `secciones` (
  `id` int NOT NULL AUTO_INCREMENT,
  `año_escolar_id` int NOT NULL,
  `nivel` enum('Inicial','Primaria') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `grado` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `letra` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `salon` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `cupo_maximo` int DEFAULT '30',
  `docente_id` int DEFAULT NULL,
  `activo` tinyint(1) DEFAULT '1',
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_seccion_anio` (`nivel`,`grado`,`letra`,`año_escolar_id`),
  KEY `fk_secciones_año_escolar` (`año_escolar_id`),
  CONSTRAINT `fk_secciones_año_escolar` FOREIGN KEY (`año_escolar_id`) REFERENCES `años_escolares` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=151 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `nombre_completo` varchar(150) NOT NULL,
  `password_hash` varchar(255) NOT NULL,
  `rol` enum('Administrador','Empleado') DEFAULT NULL,
  `estado` tinyint(1) NOT NULL DEFAULT '1',
  `creado_en` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `actualizado_en` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-02-01 16:31:39
