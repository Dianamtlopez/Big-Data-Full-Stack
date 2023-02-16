insert into facultad (id, nombre) values
(1, 'Administración'),
(2, 'Ciencias Naturales'),
(3, 'Economía'),
(4, 'Escuela de Medicina'),
(5, 'Ingeniería, Ciencia y Tecnología')

insert into departamento (nombre, id_facultad) values
('Administración de empresas', 1),
('Marketing y negocios digitales', 1),
('Biología', 2),
('Economía', 3),
('Finanzas y comercio internacional', 3),
('Medicina', 4),
('Matemáticas aplicadas y ciencias de la computación', 5)

update departamento set
nombre = 'MACC'
where id = 7

delete from departamento 
where id = 7

