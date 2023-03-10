INSERT INTO facultad (id, nombre) VALUES (1, 'Administración');
INSERT INTO facultad (id, nombre) VALUES (2, 'Ciencias Naturales');
INSERT INTO facultad (id, nombre) VALUES (3, 'Economía');
INSERT INTO facultad (id, nombre) VALUES (4, 'Escuela de Medicina');
INSERT INTO facultad (id, nombre) VALUES (5, 'Ingeniería, Ciencia y Tecnología');

INSERT INTO departamento (id, nombre, id_facultad) VALUES (1, 'Administración de empresas', 1);
INSERT INTO departamento (id, nombre, id_facultad) VALUES (2, 'Marketing y negocios digitales', 1);
INSERT INTO departamento (id, nombre, id_facultad) VALUES (3, 'Biología', 2);
INSERT INTO departamento (id, nombre, id_facultad) VALUES (4, 'Economía', 3);
INSERT INTO departamento (id, nombre, id_facultad) VALUES (5, 'Finanzas y comercio internacional', 3);
INSERT INTO departamento (id, nombre, id_facultad) VALUES (6, 'Medicina', 4);
INSERT INTO departamento (id, nombre, id_facultad) VALUES (7, 'MACC', 5);

INSERT INTO curso (id, nombre, creditos, id_departamento) VALUES (1, 'Programacion de Computadores', 4, 7);
INSERT INTO curso (id, nombre, creditos, id_departamento) VALUES (2, 'Manejo de Bases de Datos', 4, 7);
INSERT INTO curso (id, nombre, creditos, id_departamento) VALUES (3, 'Algebra Abstracta', 4, 7);
INSERT INTO curso (id, nombre, creditos, id_departamento) VALUES (4, 'Algebra Lineal', 3, 7);
INSERT INTO curso (id, nombre, creditos, id_departamento) VALUES (5, 'Macroeconomía', 4, 4);
INSERT INTO curso (id, nombre, creditos, id_departamento) VALUES (6, 'Microeconomía', 4, 4);
INSERT INTO curso (id, nombre, creditos, id_departamento) VALUES (7, 'Economía Matematica', 4, 4);
INSERT INTO curso (id, nombre, creditos, id_departamento) VALUES (8, 'Pensamiento Matematico', 2, 7);
INSERT INTO curso (id, nombre, creditos, id_departamento) VALUES (9, 'Emprendimiento Social', 3, 5);
INSERT INTO curso (id, nombre, creditos, id_departamento) VALUES (10, 'Teoría de la Computación', 3, 7);
INSERT INTO curso (id, nombre, creditos, id_departamento) VALUES (11, 'Cálculo Diferencal', 3, 7);
INSERT INTO curso (id, nombre, creditos, id_departamento) VALUES (12, 'Cálculo Integral', 3, 7);

INSERT INTO profesor (id, nombre, apellido, id_departamento) VALUES (1, 'Hector', 'Florez', 7);
INSERT INTO profesor (id, nombre, apellido, id_departamento) VALUES (2, 'Claudia', 'Hernandez', 7);
INSERT INTO profesor (id, nombre, apellido, id_departamento) VALUES (3, 'Juan', 'Perez', 7);
INSERT INTO profesor (id, nombre, apellido, id_departamento) VALUES (4, 'Valerie', 'Gautier', 7);
INSERT INTO profesor (id, nombre, apellido, id_departamento) VALUES (6, 'Norma', 'Sarmiento', 7);
INSERT INTO profesor (id, nombre, apellido, id_departamento) VALUES (7, 'Carlos', 'Alvarez', 7);
INSERT INTO profesor (id, nombre, apellido, id_departamento) VALUES (8, 'Julian', 'Rincon', 7);
INSERT INTO profesor (id, nombre, apellido, id_departamento) VALUES (5, 'Jorge', 'Gallego', 4);
INSERT INTO profesor (id, nombre, apellido, id_departamento) VALUES (9, 'Pablo', 'Martinez', 5);

INSERT INTO estudiante (codigo, nombre, apellido, fecha_nacimiento, genero, id_departamento) VALUES (1, 'Homer', 'Simpson', '1998-06-26', 'M', 7);
INSERT INTO estudiante (codigo, nombre, apellido, fecha_nacimiento, genero, id_departamento) VALUES (2, 'Marge', 'Simpson', '2001-11-18', 'F', 6);
INSERT INTO estudiante (codigo, nombre, apellido, fecha_nacimiento, genero, id_departamento) VALUES (3, 'Bart', 'Simpson', '2003-02-15', 'M', 7);
INSERT INTO estudiante (codigo, nombre, apellido, fecha_nacimiento, genero, id_departamento) VALUES (4, 'Lisa', 'Simpson', '2001-05-23', 'F', 1);
INSERT INTO estudiante (codigo, nombre, apellido, fecha_nacimiento, genero, id_departamento) VALUES (5, 'Maggie', 'Simpson', '2002-05-29', 'F', 6);
INSERT INTO estudiante (codigo, nombre, apellido, fecha_nacimiento, genero, id_departamento) VALUES (6, 'Abraham', 'Simpson', '2000-06-12', 'M', 2);
INSERT INTO estudiante (codigo, nombre, apellido, fecha_nacimiento, genero, id_departamento) VALUES (7, 'Barney', 'Gumble', '1995-11-15', 'M', 7);
INSERT INTO estudiante (codigo, nombre, apellido, fecha_nacimiento, genero, id_departamento) VALUES (8, 'Edna', 'Krabappel', '2002-03-20', 'F', 3);
INSERT INTO estudiante (codigo, nombre, apellido, fecha_nacimiento, genero, id_departamento) VALUES (9, 'Kent', 'Brockman', '2003-01-12', 'M', 7);
INSERT INTO estudiante (codigo, nombre, apellido, fecha_nacimiento, genero, id_departamento) VALUES (10, 'Lenny', 'Leonard', '2001-10-31', 'M', 6);
INSERT INTO estudiante (codigo, nombre, apellido, fecha_nacimiento, genero, id_departamento) VALUES (11, 'Milhouse', 'Van Houten', '1993-09-22', 'M', 6);
INSERT INTO estudiante (codigo, nombre, apellido, fecha_nacimiento, genero, id_departamento) VALUES (12, 'Moe', 'Szyslak', '1998-07-21', 'M', 3);
INSERT INTO estudiante (codigo, nombre, apellido, fecha_nacimiento, genero, id_departamento) VALUES (13, 'Ned', 'Flanders', '1998-07-21', 'M', 5);
INSERT INTO estudiante (codigo, nombre, apellido, fecha_nacimiento, genero, id_departamento) VALUES (14, 'Tod', 'Flanders', '1998-07-21', 'M', 7);
INSERT INTO estudiante (codigo, nombre, apellido, fecha_nacimiento, genero, id_departamento) VALUES (15, 'Rod', 'Flanders', '1998-07-21', 'M', 4);

INSERT INTO grupo (id, nombre, anio, periodo, id_curso, id_profesor) VALUES (1, 'G1', 2020, 2, 2, 1);
INSERT INTO grupo (id, nombre, anio, periodo, id_curso, id_profesor) VALUES (2, 'G2', 2020, 2, 2, 3);
INSERT INTO grupo (id, nombre, anio, periodo, id_curso, id_profesor) VALUES (3, 'G1', 2021, 1, 2, 1);
INSERT INTO grupo (id, nombre, anio, periodo, id_curso, id_profesor) VALUES (4, 'G2', 2021, 1, 2, 2);
INSERT INTO grupo (id, nombre, anio, periodo, id_curso, id_profesor) VALUES (5, 'G1', 2020, 2, 1, 7);
INSERT INTO grupo (id, nombre, anio, periodo, id_curso, id_profesor) VALUES (6, 'G2', 2020, 2, 1, 3);
INSERT INTO grupo (id, nombre, anio, periodo, id_curso, id_profesor) VALUES (7, 'G1', 2021, 1, 1, 7);
INSERT INTO grupo (id, nombre, anio, periodo, id_curso, id_profesor) VALUES (8, 'G2', 2021, 1, 1, 1);
INSERT INTO grupo (id, nombre, anio, periodo, id_curso, id_profesor) VALUES (9, 'G1', 2021, 1, 6, 5);
INSERT INTO grupo (id, nombre, anio, periodo, id_curso, id_profesor) VALUES (10, 'G1', 2021, 1, 7, 5);
INSERT INTO grupo (id, nombre, anio, periodo, id_curso, id_profesor) VALUES (11, 'G1', 2021, 1, 11, 4);
INSERT INTO grupo (id, nombre, anio, periodo, id_curso, id_profesor) VALUES (12, 'G2', 2021, 1, 11, 6);

INSERT INTO inscripcion (calificacion, codigo_estudiante, id_grupo) VALUES (35, 8, 1);
INSERT INTO inscripcion (calificacion, codigo_estudiante, id_grupo) VALUES (40, 6, 1);
INSERT INTO inscripcion (calificacion, codigo_estudiante, id_grupo) VALUES (45, 1, 2);
INSERT INTO inscripcion (calificacion, codigo_estudiante, id_grupo) VALUES (42, 3, 2);
INSERT INTO inscripcion (calificacion, codigo_estudiante, id_grupo) VALUES (40, 2, 3);
INSERT INTO inscripcion (calificacion, codigo_estudiante, id_grupo) VALUES (35, 4, 4);
INSERT INTO inscripcion (calificacion, codigo_estudiante, id_grupo) VALUES (38, 7, 3);
INSERT INTO inscripcion (calificacion, codigo_estudiante, id_grupo) VALUES (41, 9, 3);
INSERT INTO inscripcion (calificacion, codigo_estudiante, id_grupo) VALUES (46, 10, 4);
INSERT INTO inscripcion (calificacion, codigo_estudiante, id_grupo) VALUES (42, 2, 7);
INSERT INTO inscripcion (calificacion, codigo_estudiante, id_grupo) VALUES (40, 4, 7);
INSERT INTO inscripcion (calificacion, codigo_estudiante, id_grupo) VALUES (30, 6, 7);
INSERT INTO inscripcion (calificacion, codigo_estudiante, id_grupo) VALUES (25, 1, 8);
INSERT INTO inscripcion (calificacion, codigo_estudiante, id_grupo) VALUES (30, 9, 8);
INSERT INTO inscripcion (calificacion, codigo_estudiante, id_grupo) VALUES (49, 10, 8);
INSERT INTO inscripcion (calificacion, codigo_estudiante, id_grupo) VALUES (47, 11, 8);
