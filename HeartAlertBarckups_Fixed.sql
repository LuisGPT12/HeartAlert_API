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
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Volcando estructura de base de datos para heartalertdb
CREATE DATABASE IF NOT EXISTS `heartalertdb` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_uca1400_ai_ci */;
USE `heartalertdb`;

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

-- Volcando datos para la tabla heartalertdb.pacientes: ~8 rows (aproximadamente)
INSERT INTO `pacientes` (`ID_Paciente`, `nombre_paciente`, `apellido_paciente`, `cedula_paciente`, `fecha_Nacimiento`, `sexo_paciente`, `email`, `telefono`, `direccion`, `contacto_emergencia_nombre`, `contacto_emergencia_telefono`) VALUES
    (1, 'Juan', 'Pérez', '12345678', '1985-03-15', 'M', 'juan.perez@email.com', '555-1234', 'Calle 123 #45-67', 'María Pérez', '555-5678'),
    (2, 'Ana', 'García', '87654321', '1990-07-22', 'F', 'ana.garcia@email.com', '555-2345', 'Av. Central 89-12', 'Carlos García', '555-6789'),
    (3, 'Luis', 'Rodríguez', '11223344', '1978-12-10', 'M', 'luis.rodriguez@email.com', '555-3456', 'Carrera 45 #78-90', 'Elena Rodríguez', '555-7890'),
    (4, 'Carmen', 'López', '44332211', '1995-05-08', 'F', 'carmen.lopez@email.com', '555-4567', 'Calle 67 #12-34', 'José López', '555-8901'),
    (5, 'Pedro', 'Martínez', '55667788', '1982-09-25', 'M', 'pedro.martinez@email.com', '555-5678', 'Av. Norte 23-45', 'Lucía Martínez', '555-9012'),
    (6, 'Sofia', 'Herrera', '99887766', '1988-11-30', 'F', 'sofia.herrera@email.com', '555-6789', 'Calle 89 #56-78', 'Miguel Herrera', '555-0123'),
    (7, 'Diego', 'Morales', '13579246', '1976-04-18', 'M', 'diego.morales@email.com', '555-7890', 'Carrera 12 #34-56', 'Rosa Morales', '555-1234'),
    (8, 'Valentina', 'Castro', '24681357', '1993-08-12', 'F', 'valentina.castro@email.com', '555-8901', 'Av. Sur 78-90', 'Andrés Castro', '555-2345');

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

-- Volcando datos para la tabla heartalertdb.electrocardiograma: ~12 rows (aproximadamente)
INSERT INTO `electrocardiograma` (`ID_Lectura`, `COD_Paciente`, `tiempo_actual`, `frecuencia_cardiaca`, `balance_cardiaca_hrv`) VALUES
    (1, 1, '2024-01-15 08:30:00', 72, 45.2),
    (2, 1, '2024-01-15 14:30:00', 78, 42.8),
    (3, 2, '2024-01-16 09:15:00', 85, 38.5),
    (4, 2, '2024-01-16 15:45:00', 92, 35.2),
    (5, 3, '2024-01-17 10:20:00', 68, 52.1),
    (6, 3, '2024-01-17 16:30:00', 75, 48.9),
    (7, 4, '2024-01-18 11:45:00', 88, 40.3),
    (8, 4, '2024-01-18 17:15:00', 95, 36.8),
    (9, 5, '2024-01-19 08:00:00', 70, 46.7),
    (10, 5, '2024-01-19 14:20:00', 82, 43.5),
    (11, 6, '2024-01-20 09:30:00', 76, 44.1),
    (12, 6, '2024-01-20 15:50:00', 83, 41.2);

-- Volcando estructura para tabla heartalertdb.alertas - SIN constraint a electrocardiograma
CREATE TABLE IF NOT EXISTS `alertas` (
  `ID_Alerta` int(11) NOT NULL AUTO_INCREMENT,
  `COD_Lectura` int(11) NOT NULL,
  `COD_Paciente` int(11) NOT NULL,
  `tipo_alerta` varchar(15) NOT NULL,
  `atendido` char(1) NOT NULL,
  PRIMARY KEY (`ID_Alerta`),
  KEY `COD_Lectura` (`COD_Lectura`),
  KEY `COD_Paciente` (`COD_Paciente`),
  CONSTRAINT `alertas_ibfk_2` FOREIGN KEY (`COD_Paciente`) REFERENCES `pacientes` (`ID_Paciente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- Volcando datos para la tabla heartalertdb.alertas: ~8 rows (aproximadamente)
INSERT INTO `alertas` (`ID_Alerta`, `COD_Lectura`, `COD_Paciente`, `tipo_alerta`, `atendido`) VALUES
    (1, 4, 2, 'Taquicardia', 'N'),
    (2, 8, 4, 'Arritmia', 'S'),
    (3, 3, 2, 'Bradicardia', 'N'),
    (4, 7, 4, 'Palpitaciones', 'N'),
    (5, 1, 1, 'Normal', 'S'),
    (6, 12, 6, 'Taquicardia', 'N'),
    (7, 5, 3, 'Normal', 'S'),
    (8, 10, 5, 'Arritmia', 'N');

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

-- Volcando datos para la tabla heartalertdb.historial: ~8 rows (aproximadamente)
INSERT INTO `historial` (`ID_Historial`, `COD_Paciente`, `Tipo_sangre`, `Alergias`, `diagnóstico`, `Observaciones`) VALUES
    (1, 1, 'O+', 'Penicilina', 'Hipertensión arterial', 'Paciente estable, control mensual'),
    (2, 2, 'A-', 'Ninguna', 'Arritmia cardiaca', 'Requiere monitoreo continuo'),
    (3, 3, 'B+', 'Aspirina', 'Diabetes tipo 2', 'Control glucémico adecuado'),
    (4, 4, 'AB+', 'Mariscos', 'Taquicardia supraventricular', 'Episodios frecuentes'),
    (5, 5, 'O-', 'Polen', 'Bradicardia sinusal', 'Asintomático'),
    (6, 6, 'A+', 'Ninguna', 'Fibrilación auricular', 'Anticoagulación requerida'),
    (7, 7, 'B-', 'Yodo', 'Infarto agudo de miocardio', 'Post-quirúrgico estable'),
    (8, 8, 'AB-', 'Látex', 'Insuficiencia cardiaca', 'Tratamiento con diuréticos');

-- Volcando estructura para tabla heartalertdb.pacientes_doctor
CREATE TABLE IF NOT EXISTS `pacientes_doctor` (
  `COD_Paciente` int(11) NOT NULL,
  `COD_Doctor` int(11) NOT NULL,
  KEY `COD_Paciente` (`COD_Paciente`),
  KEY `COD_Doctor` (`COD_Doctor`),
  CONSTRAINT `pacientes_doctor_ibfk_1` FOREIGN KEY (`COD_Paciente`) REFERENCES `pacientes` (`ID_Paciente`),
  CONSTRAINT `pacientes_doctor_ibfk_2` FOREIGN KEY (`COD_Doctor`) REFERENCES `doctor` (`ID_Doctor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- Volcando datos para la tabla heartalertdb.pacientes_doctor: ~10 rows (aproximadamente)
INSERT INTO `pacientes_doctor` (`COD_Paciente`, `COD_Doctor`) VALUES
    (1, 1),
    (2, 1),
    (3, 3),
    (4, 1),
    (5, 2),
    (6, 1),
    (7, 1),
    (8, 5),
    (1, 3),
    (2, 5);

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
    (6, 1, 'mariana_cardio', 'mariana123'),
    (7, 2, 'enrique_neuro', 'enrique456'),
    (8, 3, 'julia_interna', 'julia789'),
    (9, 4, 'carlos_pediatra', 'carlos012'),
    (10, 5, 'ana_geriatria', 'ana345'),
    (11, 6, 'tilinazo_admin', 'tilinazo678'),
    (12, 1, 'user_cardio1', 'cardio901'),
    (13, 2, 'user_neuro1', 'neuro234'),
    (14, 3, 'user_interna1', 'interna567'),
    (15, 4, 'user_pediatra1', 'pediatra890');

-- Volcando estructura para tabla heartalertdb.usuario_google
CREATE TABLE IF NOT EXISTS `usuario_google` (
  `ID_UsuarioGoogle` int(11) NOT NULL AUTO_INCREMENT,
  `COD_Doctor` int(11) NOT NULL,
  `email` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`ID_UsuarioGoogle`),
  KEY `COD_Doctor` (`COD_Doctor`),
  CONSTRAINT `usuario_google_ibfk_1` FOREIGN KEY (`COD_Doctor`) REFERENCES `doctor` (`ID_Doctor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- Volcando datos para la tabla heartalertdb.usuario_google: ~6 rows (aproximadamente)
INSERT INTO `usuario_google` (`ID_UsuarioGoogle`, `COD_Doctor`, `email`) VALUES
    (1, 1, 'mariana.rios@gmail.com'),
    (2, 2, 'enrique.salazar@gmail.com'),
    (3, 3, 'julia.mendez@gmail.com'),
    (4, 4, 'carlos.luna@gmail.com'),
    (5, 5, 'ana.gomez@gmail.com'),
    (6, 6, 'tilinazo.vargas@gmail.com');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;