-- 1. Nombre modelo, marca y grupo de coches (los nombre de todos) --
-- 2. Fecha de compra --
-- 3. Matricula --
-- 4. Nombre del color del coche --
-- 5. Total kilómetros --
-- 6. Nombre empresa que está asegurado el coche --
-- 7. Numero de póliza --
select 
	b.modelo, 
	b.marca, 
	b.grupo_empresarial, 
	a.fecha_compra, 
	a.matricula, 
	a.color, 
	c.kilometraje, 
	d.nombre_aseguradora,
	c.codigo_poliza
from practica_vehiculos.empresa_vehiculo a inner join practica_vehiculos.fabricante_vehiculo b on a.id_modelo = b.id_modelo
inner join practica_vehiculos.poliza_empresa c on a.matricula = c.matricula
inner join practica_vehiculos.aseguradora d on c.id_aseguradora = d.id_aseguradora
inner join practica_vehiculos.poliza_empresa e on a.matricula = e.matricula

-- Nota: se ha seleccionado inner join porque se quiso hacer la interseccion de las tablas involucradas, que tuvieran informacion en común --