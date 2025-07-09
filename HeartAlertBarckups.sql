-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         11.5.2-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.6.0.6765
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 alertas*/;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para heartalertdb
CREATE DATABASE IF NOT EXISTS `heartalertdb` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_uca1400_ai_ci */;
USE `heartalertdb`;

-- Volcando estructura para tabla heartalertdb.alertas
CREATE TABLE IF NOT EXISTS `alertas` (
  `ID_Alerta` int(11) NOT NULL AUTO_INCREMENT,
  `COD_Lectura` int(11) NOT NULL,
  `COD_Paciente` int(11) NOT NULL,
  `tipo_alerta` varchar(15) NOT NULL,
  `atendido` char(1) NOT NULL,
  PRIMARY KEY (`ID_Alerta`),
  KEY `COD_Lectura` (`COD_Lectura`),
  KEY `COD_Paciente` (`COD_Paciente`),
  CONSTRAINT `alertas_ibfk_1` FOREIGN KEY (`COD_Lectura`) REFERENCES `electrocardiograma` (`ID_Lectura`),
  CONSTRAINT `alertas_ibfk_2` FOREIGN KEY (`COD_Paciente`) REFERENCES `pacientes` (`ID_Paciente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- Volcando datos para la tabla heartalertdb.alertas: ~0 rows (aproximadamente)

-- Volcando estructura para tabla heartalertdb.doctor
CREATE TABLE IF NOT EXISTS `doctor` (
  `ID_Doctor` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_doctor` varchar(20) NOT NULL,
  `apellido_doctor` varchar(20) NOT NULL,
  `especialidad` varchar(50) NOT NULL,
  `Verificacion_ID` varchar(6) NOT NULL,
  PRIMARY KEY (`ID_Doctor`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- Volcando datos para la tabla heartalertdb.doctor: ~6 rows (aproximadamente)
INSERT INTO `doctor` (`ID_Doctor`, `nombre_doctor`, `apellido_doctor`, `especialidad`, `Verificacion_ID`) VALUES
	(1, 'Mariana', 'Ríos', 'Cardiología', 'VRF001'),
	(2, 'Enrique', 'Salazar', 'Neurología', 'VRF002'),
	(3, 'Julia', 'Méndez', 'Medicina Interna', 'VRF003'),
	(4, 'Carlos', 'Luna', 'Pediatría', 'VRF004'),
	(5, 'Ana', 'Gómez', 'Geriatría', 'VRF005'),
	(6, 'Tilinazo', 'Vargas', 'Geyologia', '1234');

-- Volcando estructura para tabla heartalertdb.electrocardiograma
CREATE TABLE IF NOT EXISTS `electrocardiograma` (
  `ID_Lectura` int(11) NOT NULL AUTO_INCREMENT,
  `COD_Paciente` int(11) NOT NULL,
  `tiempo_actual` datetime NOT NULL,
  `frecuencia_cardiaca` int(11) NOT NULL,
  `balance_cardiaca_hrv` double NOT NULL,
  PRIMARY KEY (`ID_Lectura`),
  KEY `COD_Paciente` (`COD_Paciente`),
  CONSTRAINT `electrocardiograma_ibfk_1` FOREIGN KEY (`COD_Paciente`) REFERENCES `pacientes` (`ID_Paciente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- Volcando datos para la tabla heartalertdb.electrocardiograma: ~0 rows (aproximadamente)

-- Volcando estructura para tabla heartalertdb.historial
CREATE TABLE IF NOT EXISTS `historial` (
  `ID_Historial` int(11) NOT NULL AUTO_INCREMENT,
  `COD_Paciente` int(11) NOT NULL,
  `Tipo_sangre` char(3) NOT NULL,
  `Alergias` varchar(200) DEFAULT NULL,
  `diagnóstico` varchar(100) NOT NULL,
  `Observaciones` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`ID_Historial`),
  KEY `COD_Paciente` (`COD_Paciente`),
  CONSTRAINT `historial_ibfk_1` FOREIGN KEY (`COD_Paciente`) REFERENCES `pacientes` (`ID_Paciente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- Volcando datos para la tabla heartalertdb.historial: ~0 rows (aproximadamente)

-- Volcando estructura para tabla heartalertdb.pacientes
CREATE TABLE IF NOT EXISTS `pacientes` (
  `ID_Paciente` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_paciente` varchar(20) DEFAULT NULL,
  `apellido_paciente` varchar(20) DEFAULT NULL,
  `cedula_paciente` varchar(20) DEFAULT NULL,
  `fecha_Nacimiento` date DEFAULT NULL,
  `sexo_paciente` char(1) NOT NULL,
  `email` text DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `direccion` varchar(120) DEFAULT NULL,
  `contacto_emergencia_nombre` varchar(20) DEFAULT NULL,
  `contacto_emergencia_telefono` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`ID_Paciente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- Volcando datos para la tabla heartalertdb.pacientes: ~0 rows (aproximadamente)

-- Volcando estructura para tabla heartalertdb.pacientes_doctor
CREATE TABLE IF NOT EXISTS `pacientes_doctor` (
  `COD_Paciente` int(11) NOT NULL,
  `COD_Doctor` int(11) NOT NULL,
  KEY `COD_Paciente` (`COD_Paciente`),
  KEY `COD_Doctor` (`COD_Doctor`),
  CONSTRAINT `pacientes_doctor_ibfk_1` FOREIGN KEY (`COD_Paciente`) REFERENCES `pacientes` (`ID_Paciente`),
  CONSTRAINT `pacientes_doctor_ibfk_2` FOREIGN KEY (`COD_Doctor`) REFERENCES `doctor` (`ID_Doctor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- Volcando datos para la tabla heartalertdb.pacientes_doctor: ~0 rows (aproximadamente)

-- Volcando estructura para tabla heartalertdb.usuarios
CREATE TABLE IF NOT EXISTS `usuarios` (
  `ID_Usuario` int(11) NOT NULL AUTO_INCREMENT,
  `COD_Doctor` int(11) NOT NULL,
  `nombre_usuario` varchar(20) NOT NULL,
  `contrasenia` varchar(20) NOT NULL,
  PRIMARY KEY (`ID_Usuario`),
  KEY `COD_Doctor` (`COD_Doctor`),
  CONSTRAINT `usuarios_ibfk_1` FOREIGN KEY (`COD_Doctor`) REFERENCES `doctor` (`ID_Doctor`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- Volcando datos para la tabla heartalertdb.usuarios: ~15 rows (aproximadamente)
INSERT INTO `usuarios` (`ID_Usuario`, `COD_Doctor`, `nombre_usuario`, `contrasenia`) VALUES
	(1, 1, 'jose_medico', 'password123'),
	(2, 2, 'laura_doc', 'segura456'),
	(3, 3, 'daniela123', 'clave789'),
	(4, 4, 'mario_pediatra', 'mariopass'),
	(5, 5, 'sofia_cardio', 'sofiastrong'),
	(6, 1, 'jose_medico', 'password123'),
	(7, 2, 'laura_doc', 'segura456'),
	(8, 3, 'daniela123', 'clave789'),
	(9, 4, 'mario_pediatra', 'mariopass'),
	(10, 5, 'sofia_cardio', 'sofiastrong'),
	(11, 1, 'jose_medico', 'password123'),
	(12, 2, 'laura_doc', 'segura456'),
	(13, 3, 'daniela123', 'clave789'),
	(14, 4, 'mario_pediatra', 'mariopass'),
	(15, 5, 'sofia_cardio', 'sofiastrong');

-- Volcando estructura para tabla heartalertdb.usuario_google
CREATE TABLE IF NOT EXISTS `usuario_google` (
  `ID_UsuarioGoogle` int(11) NOT NULL AUTO_INCREMENT,
  `COD_Doctor` int(11) NOT NULL,
  `email` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`ID_UsuarioGoogle`),
  KEY `COD_Doctor` (`COD_Doctor`),
  CONSTRAINT `usuario_google_ibfk_1` FOREIGN KEY (`COD_Doctor`) REFERENCES `doctor` (`ID_Doctor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- Volcando datos para la tabla heartalertdb.usuario_google: ~0 rows (aproximadamente)

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
