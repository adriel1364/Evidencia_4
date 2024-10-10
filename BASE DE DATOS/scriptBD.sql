CREATE DATABASE Cafebar;
USE Cafebar;
CREATE TABLE Cafetera (
    idCafetera INT PRIMARY KEY AUTO_INCREMENT,
    capacidad DECIMAL(5, 2) NOT NULL,
    nivel_agua DECIMAL(5, 2) NOT NULL,
    temperatura DECIMAL(5, 2) NOT NULL
);

CREATE TABLE HistorialPreparacion (
    id INT PRIMARY KEY AUTO_INCREMENT,
    cafetera_id INT,
    cantidad DECIMAL(5, 2) NOT NULL,
    fecha_preparacion DATETIME NOT NULL,
    FOREIGN KEY (cafetera_id) REFERENCES Cafetera(idCafetera)
);