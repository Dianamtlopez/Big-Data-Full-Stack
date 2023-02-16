(select est.nombre, est.apellido, dep.nombre
from estudiante est, departamento dep
where est.id_departamento = dep.id and dep.nombre = 'Economía')
union all
(select est.nombre, est.apellido, dep.nombre
from estudiante est, departamento dep
where est.id_departamento = dep.id and dep.nombre = 'MACC')

(select pro.nombre, pro.apellido
from profesor pro, grupo gru, curso cur
where pro.id = gru.id_profesor and cur.id = gru.Id_curso and cur.nombre = 'Programacion de Computadores')
intersect all
(select pro.nombre, pro.apellido
from profesor pro, grupo gru, curso cur
where pro.id = gru.id_profesor and cur.id = gru.Id_curso and cur.nombre = 'Manejo de Bases de Datos') 
