select nombre 
from departamento
where id_facultad = 1

select dep.nombre as depto, fac.nombre as facultad 
from departamento dep, facultad fac
where fac.id = 1 and fac.id = dep.id_facultad

select dep.nombre as depto, fac.nombre as facultad 
from departamento dep, facultad fac
where dep.nombre like 'M%' and fac.id = dep.id_facultad

select dep.nombre as depto, fac.nombre as facultad 
from departamento dep, facultad fac
where dep.nombre like '_i%' and fac.id = dep.id_facultad

select dep.nombre as depto, fac.nombre as facultad 
from departamento dep, facultad fac
where fac.id = dep.id_facultad
order by dep.nombre asc


