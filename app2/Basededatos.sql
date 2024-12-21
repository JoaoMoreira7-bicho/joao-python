CREATE DATABASE RegistroAutos;
USE RegistroAutos;

CREATE TABLE autos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    marca VARCHAR(100) NOT NULL,
    modelo VARCHAR(100) NOT NULL,
    anio INT NOT NULL,
    precio DECIMAL(10, 2) NOT NULL
);