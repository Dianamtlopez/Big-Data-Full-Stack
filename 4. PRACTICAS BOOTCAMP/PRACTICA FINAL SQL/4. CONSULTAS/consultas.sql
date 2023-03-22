-- 1. Nombre modelo, marca y grupo de coches (los nombre de todos) --
select b.modelo, b.marca, b.grupo_empresarial
from practica_vehiculos.empresa_vehiculo a inner join practica_vehiculos.fabricante_vehiculo b
on a.id_modelo = b.id_modelo

-- 2. Fecha de compra --
select a.fecha_compra
from practica_vehiculos.empresa_vehiculo a inner join practica_vehiculos.fabricante_vehiculo b
on a.id_modelo = b.id_modelo

-- 3. Matricula --
select a.matricula
from practica_vehiculos.empresa_vehiculo a inner join practica_vehiculos.fabricante_vehiculo b
on a.id_modelo = b.id_modelo

-- 4. Nombre del color del coche --
select a.color
from practica_vehiculos.empresa_vehiculo a inner join practica_vehiculos.fabricante_vehiculo b
on a.id_modelo = b.id_modelo

-- 5. Total kilómetros --
select b.kilometraje
from practica_vehiculos.empresa_vehiculo a inner join practica_vehiculos.poliza_empresa b
on a.matricula = b.matricula

-- 6. Nombre empresa que está asegurado el coche --
select b.nombre_aseguradora
from practica_vehiculos.poliza_empresa a inner join practica_vehiculos.aseguradora b
on a.id_aseguradora = b.id_aseguradora

-- 7. Numero de póliza --
select b.codigo_poliza
from practica_vehiculos.empresa_vehiculo a inner join practica_vehiculos.poliza_empresa b
on a.matricula = b.matricula

-- Nota: se ha seleccionado inner join porque se quiso hacer la interseccion de las tablas involucradas, que tuvieran informacion en común --