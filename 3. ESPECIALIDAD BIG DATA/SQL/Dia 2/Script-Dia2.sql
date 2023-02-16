--Creamos el esquema
create schema prueba_ddl authorization oodhuafv;


--Crear la tabla de series

create table prueba_ddl.series(
	idserie varchar(10),
	nombre varchar(200),
	year_create integer
);

-- Borramos la tabla

drop table prueba_ddl.series ;


-- creamos la serie con su Pk y control de nulos
create table prueba_ddl.series(
	idserie varchar(10) not null, -- PK
	nombre varchar(200) not null,
	year_create integer not null,
	constraint series_pk primary key (idserie)
);

-- Modificamos la tabla series con un comentario

alter table prueba_ddl.series 
add column comentario varchar(250) null;

--Borrar column.. Ojo columna + datos

alter table prueba_ddl.series 
drop column comentario;


-- Creamos la tabla de temporadas
create table prueba_ddl.temporadas (
	 varchar(10) not null, --idserie PK, FK -> series (idserie)
	num_temporada integer not null, --PK
	anio integer not null, --obligarorio
	titulo varchar(200) not null, --obligatorio
	comentario varchar(250) null -- no es  obligatorio
);

--Creamos la PK de la tabla
alter table prueba_ddl.temporadas
add constraint temporadas_pk primary key (idserie, num_temporada);

-- Creamos la FK de la tabla
alter table prueba_ddl.temporadas 
add constraint temporadas_FK foreign key (idserie) 
references prueba_ddl.series (idserie); --on delete cascade


---- DML -----
-- COmando Insert -----

insert into prueba_ddl.series 
(idserie, nombre, year_create)
values ('0001','Breaking Bad', 2008);


insert into prueba_ddl.series 
(idserie, nombre, year_create)
values ('0002','Juego de tronos', 2011);

insert into prueba_ddl.series 
(idserie, nombre, year_create)
values ('0003','Hermanos de sangre', 2001);


--- avance SELECT ---
select * from prueba_ddl.series



insert into prueba_ddl.temporadas 
(idserie, num_temporada, anio, titulo)
values ('0001', 1, 2008, 'Primera temporada');


insert into prueba_ddl.temporadas 
(idserie, num_temporada, anio, titulo)
values ('0001', 2, 2008, 'Segunda temporada');


insert into prueba_ddl.temporadas 
(idserie, num_temporada, anio, titulo)
values ('0002', 1, 2011, 'Primera temporada');

insert into prueba_ddl.temporadas 
(idserie, num_temporada, anio, titulo)
values ('0002', 2, 2012, 'Segunda temporada');

insert into prueba_ddl.temporadas 
(idserie, num_temporada, anio, titulo)
values ('0002', 3, 2013, 'Tercera temporada');


select * from prueba_ddl.temporadas 


--- comando SELECT ---  full scan

select *
from prueba_ddl.temporadas ;

select idserie , num_temporada , anio, titulo, comentario
from prueba_ddl.temporadas ;


-- Serie juego de Tronos
select *
from prueba_ddl.temporadas t 
where idserie  = '0002';


-- Serie juego de Tronos temporada 2
select *
from prueba_ddl.temporadas t 
where idserie  = '0002' and num_temporada = 2;


-- Serie juego de Tronos temporada 2 y la temporada 1
select *
from prueba_ddl.temporadas t 
where idserie  = '0002' and (num_temporada = 2 or num_temporada  = 1)

-- temporadas mayores al año 2010
select *
from prueba_ddl.temporadas a
where anio > 2010


-- temporadas mayores al año 2010 ordenadas por año descendente
select *
from prueba_ddl.temporadas t 
where t.anio > 2010
order by t.anio desc, t.titulo  desc -- asc / desc


-- No repetir el id serie, desde la tabla temporadas

select  distinct idserie  
from prueba_ddl.temporadas 



--- Comando DELETE

delete from prueba_ddl.series 
where idserie  = '0003';



--- COMANDO UPDATE ---

select *
from prueba_ddl.temporadas
where idserie  = '0001' and num_temporada = 2



update prueba_ddl.temporadas
set comentario = 'Hola', titulo  = 'temporada 2'
where idserie  = '0001' and num_temporada = 2;


--- COMANDO SELECT - AGRUPACIONES ---

select count(*)
from prueba_ddl.temporadas t 
where num_temporada  = 1


select sum(num_temporada), avg(num_temporada)
from prueba_ddl.temporadas t 



--- numero temporadas por serie
select idserie , count(*)
from prueba_ddl.temporadas t 
group by idserie


-- numero series que tengas mas de 2 temporadas
select idserie , count(*)
from prueba_ddl.temporadas t 
group by idserie
having count(*) >= 2
order by idserie desc


--- UNION ALL ---

-- temporadas de las 2 series
select idserie, titulo 
from prueba_ddl.temporadas where idserie  = '0001'
union all
select idserie, titulo 
from prueba_ddl.temporadas where idserie  = '0002'


--- usando 2 tablas distintas

select distinct idserie as pepe from prueba_ddl.temporadas 
where idserie  = '0001'
union all
select idserie as manolo from prueba_ddl.series s 
where idserie  = '0002' or idserie  = '0003'




--- Tabla temporal, auxiliar, intermedia... copia seguridad etc...


create table prueba_ddl.series_copia
as
select * from prueba_ddl.series s  where 1 = 1



select * from prueba_ddl.series_copia sc 




--- FUNCIONES-----

select dt_birth as "Fecha de nacimiento", date_part('year',dt_birth) as anio  
from public.person 
where date_part('year',dt_birth) < 1976

select email, trim(upper(email)) as email2 
from public.person p 



select * 
from public.employees e 





---- Ejerccios


select gender, count(*)
from person
group by gender

select count(*)
from person p 
where dt_birth  < '1970-01-01'



select COUNT(*)
from employees  
where employee_type = 'PROFESIONAL'

select AVG(salary_gross_annual), MAX(salary_gross_annual), MIN(salary_gross_annual)
from employees  

select  job , AVG(salary_gross_annual)
from employees  
group by job

















