select avg(calificacion) 
from inscripcion

select avg(calificacion) 
from inscripcion
where calificacion > 30

select max(calificacion)
from inscripcion

select min(calificacion)
from inscripcion

select sum(creditos)
from curso
where id_departamento = 7

select count(id)
from curso
where id_departamento = 7

select est.nombre, est.apellido, round(avg(ins.calificacion),2)
from estudiante est, inscripcion ins
where est.codigo = ins.codigo_estudiante
group by est.nombre, est.apellido

select est.nombre, est.apellido, round(avg(ins.calificacion),2)
from estudiante est, inscripcion ins
where est.codigo = ins.codigo_estudiante
group by est.nombre, est.apellido
having avg(ins.calificacion) > 40

