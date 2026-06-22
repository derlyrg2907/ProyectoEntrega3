-- Base de datos para GlowSkin - Cuidado Facial

CREATE DATABASE IF NOT EXISTS belleza_db;
USE belleza_db;

CREATE TABLE IF NOT EXISTS productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10, 2) NOT NULL,
    categoria VARCHAR(50),
    creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Datos iniciales de ejemplo
INSERT INTO productos (nombre, descripcion, precio, categoria) VALUES
('Crema Hidratante Facial', 'Hidratación profunda con ácido hialurónico para todo tipo de piel', 45000.00, 'Hidratantes'),
('Sérum Vitamina C', 'Ilumina y unifica el tono de la piel, reduce manchas', 68000.00, 'Sérum'),
('Protector Solar SPF 50', 'Protección UVA/UVB sin residuo blanco, textura ligera', 39000.00, 'Protección Solar'),
('Limpiador Micelar', 'Elimina maquillaje y suciedad sin irritar la piel sensible', 28000.00, 'Limpieza'),
('Mascarilla de Arcilla', 'Purifica y controla el exceso de grasa, reduce poros', 35000.00, 'Tratamiento'),
('Contorno de Ojos', 'Reduce ojeras y bolsas, hidrata el área del contorno ocular', 55000.00, 'Tratamiento');
