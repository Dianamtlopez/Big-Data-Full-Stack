select nombre, apellido, fecha_nacimiento
from estudiante 
where fecha_nacimiento > some (select est.fecha_nacimiento
				from estudiante est join departamento dep
				on (est.id_departamento = dep.id)
				where dep.nombre = 'Medicina') 

select nombre, apellido, fecha_nacimiento
from estudiante 
where fecha_nacimiento > all (select est.fecha_nacimiento
				from estudiante est join departamento dep
				on (est.id_departamento = dep.id)
				where dep.nombre = 'Medicina') 

select nombre, apellido, fecha_nacimiento
from estudiante 
where fecha_nacimiento in (select est.fecha_nacimiento
				from estudiante est join departamento dep 
				on (est.id_departamento = dep.id)
				where dep.nombre = 'MACC')							

select dept
from (select dep.nombre as dept, pro.nombre prof, pro.apellido
	  from departamento dep left outer join profesor pro
	  on (dep.id = pro.id_departamento)) as dept_prof
where dept_prof.prof is null	



