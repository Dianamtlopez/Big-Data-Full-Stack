select pro.nombre, pro.apellido, dep.nombre 
from profesor pro cross join departamento dep

select pro.nombre, pro.apellido, dep.nombre 
from profesor pro inner join departamento dep 
on (pro.id_departamento = dep.id)

select pro.nombre, pro.apellido, dep.nombre 
from profesor pro left outer join departamento dep 
on (pro.id_departamento = dep.id)

select dep.nombre, pro.nombre, pro.apellido
from departamento dep left outer join profesor pro
on (dep.id = pro.id_departamento)

select pro.nombre, pro.apellido, dep.nombre 
from profesor pro right outer join departamento dep 
on (pro.id_departamento = dep.id)

select dep.nombre, pro.nombre, pro.apellido
from departamento dep right outer join profesor pro
on (dep.id = pro.id_departamento)

select pro.nombre, pro.apellido, dep.nombre 
from profesor pro full outer join departamento dep 
on (pro.id_departamento = dep.id)

select dep.nombre, pro.nombre, pro.apellido
from departamento dep full outer join profesor pro
on (dep.id = pro.id_departamento)

