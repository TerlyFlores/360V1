CREATE DATABASE tour_virtual;

USE tour_virtual;


CREATE TABLE usuarios (
    id INT PRIMARY KEY AUTO_INCREMENT,
    codigo VARCHAR(50) UNIQUE,
    nombre VARCHAR(255),
    edad INT,
    carrera VARCHAR(255),
    ciclo INT,
    contraseña VARCHAR(255) 
);


CREATE TABLE sedes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(255)
);


CREATE TABLE aulas (
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_sede INT,
    nombre VARCHAR(10), -- Para cumplir con el formato C0607
    imagen VARCHAR(255),
    tipo VARCHAR(255),
    piso VARCHAR (255),
    FOREIGN KEY (id_sede) REFERENCES sedes(id)
);


CREATE TABLE cursos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(255),
    horario VARCHAR(255),
    id_profesor INT,
    FOREIGN KEY (id_profesor) REFERENCES usuarios(id) -- Suponiendo que los profesores son también usuarios
);


CREATE TABLE alumno_curso (
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_alumno INT,
    id_curso INT,
    FOREIGN KEY (id_alumno) REFERENCES usuarios(id),
    FOREIGN KEY (id_curso) REFERENCES cursos(id)
);


CREATE TABLE profesores (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(255),
    especialidad VARCHAR(255)
);

INSERT INTO sedes (nombre) VALUES ('Julio Hernan');


INSERT INTO usuarios (codigo, nombre, edad, carrera, ciclo, contraseña) 
VALUES 
('A001', 'Juan Pérez', 20, 'Ingeniería de Sistemas', 3, 'contraseña123'),
('A002', 'María Gómez', 21, 'Arquitectura', 5, 'contraseña456');


INSERT INTO aulas (id_sede, nombre, imagen, tipo, piso) 
VALUES 
(1, 'C0607', 'dato a prueba',"Lanoratorio", 'Piso 6'),
(1, 'C0608', 'dato a prueba','Teorica', 'Piso 6');


INSERT INTO cursos (nombre,horario, id_profesor) 
VALUES 
('Integrado de Sistemas','18:30 a 20:15', 1),  
('Etica','20:15 a 21:45', 2);  


INSERT INTO alumno_curso (id_alumno, id_curso) 
VALUES 
(1, 1), 
(2, 2); 

