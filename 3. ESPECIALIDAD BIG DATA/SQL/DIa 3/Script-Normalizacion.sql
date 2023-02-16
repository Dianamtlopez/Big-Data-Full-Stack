-- Ejercicio de normalizacion. Creamos las estructuras del modelo E-R
-- y cargamos los datos que hay del cliente (public)
-------------------------------------------------------------------------

-- primero creamos un esquema de trabajo
create schema personalmaster authorization oodhuafv;



-- Empezamos con PERSONA -------------

-- tipo de documentos: es el NIF; NIE, el pasaporte etc.
create table personalmaster.type_docs(
	type_doc varchar(20) not null, --PK
	name varchar(200) not null,
	description varchar(512) null
);

alter table personalmaster.type_docs
add constraint type_docs_PK primary key (type_doc);


-- tipo de generos: si es hombre o mujer
create table personalmaster.type_gender (
	gender varchar(20) not null, -- PK
	name varchar(200) not null,
	description varchar(512) null
);

alter table personalmaster.type_gender
add constraint type_gender_PK primary key (gender);



--tabla de Personas

create table personalmaster.person(
	id_person varchar(10) not null, --PK
	name varchar(50) not null,
	apell1 varchar(50) not null,
	apell2 varchar(50) null, -- puede o no tener apellidos 2.
	dt_birth date not null,
	type_doc varchar(20) not null, -- FK -> type_docs -> type_doc
	legal_id varchar(20) not null,
	email varchar(255)  null,
	phone varchar(50) null,
	gender varchar(20) not null, -- FK -> type_gender -> gender
	description varchar(512) null
	
);


alter table personalmaster.person
add constraint person_PK primary key (id_person); 

alter table personalmaster.person
add constraint person_type_docs_FK foreign key (type_doc) 
references personalmaster.type_docs(type_doc);

alter table personalmaster.person
add constraint person_type_gender_FK foreign key (gender)
references personalmaster.type_gender(gender);


--- Cargamos los datos....

--select distinct type_doc from public.person
insert into personalmaster.type_docs
(type_doc, name, description)
values ('NIF','DNI/NIF','Documento oficial de España');
 

insert into personalmaster.type_docs
(type_doc, name, description)
values ('PASS','Pasaporte','');

--select * from personalmaster.type_docs


--select distinct gender from public.person

insert into personalmaster.type_gender
values ('FLUIDO','Genero fluido','');

insert into personalmaster.type_gender
values ('MUJER','Genero Femenino/Mujer','');

insert into personalmaster.type_gender
values ('HOMBRE','Genero Masculino/Varón','');

insert into personalmaster.type_gender
values ('NO DEFINIDO','Genero no definido','');

select * from personalmaster.type_gender


-- INSERT SELECT
insert into personalmaster.person
(id_person, name, apell1 , apell2 , dt_birth , type_doc , legal_id , email,
phone , gender , description )
select id_person, name, apell1 , apelli2 , dt_birth , type_doc , legal_id , email,
phone , gender , description 
from public.person ;


--select * from personalmaster.person

--delete from personalmaster.type_gender
--where gender  = 'FLUIDO'


-- EMPEZAMOS CON EMPLEADO --------------

create table personalmaster.motivos(
	id_reason varchar(100) not null, --PK
	name varchar(256) not null,
	description varchar(512) null
);

alter table personalmaster.motivos
add constraint motivos_PK primary key(id_reason);


select distinct reason_hire from public.employees 

select distinct reason_termination from public.employees 


-- NUEVA ALTA -  SIN MOTIVO


insert into personalmaster.motivos
(id_reason, name, description)
values ('01','Nueva alta','Nueva alta en la organizacion');

insert into personalmaster.motivos
(id_reason, name, description)
values ('02','Nueva alta Seleccion','Nueva alta en la organizacion por proceso de seleccion');

insert into personalmaster.motivos
(id_reason, name, description)
values ('00','Sin motivo','');




--select * from personalmaster.motivos

--me creo una copia de la tabla de empleados del cliente

create table personalmaster.employees_aux_borrar
as
select * from public.employees;

select * from personalmaster.employees_aux_borrar

--Transcodificacion de los motivos de baja y alta en persona, con los codigos nuevos

update personalmaster.employees_aux_borrar
set reason_hire  = '01';

update personalmaster.employees_aux_borrar
set reason_termination  = '00';



-- seguimos con llos tipos de contratacion

create table personalmaster.tpcontratacion(
	idtipocontratacion varchar(100) not null, --PK
	name varchar(256) not null,
	description varchar(512) null
);

alter table personalmaster.tpcontratacion
add constraint tpcontratacion_PK primary key(idtipocontratacion);

select distinct employee_type from personalmaster.employees_aux_borrar


insert into personalmaster.tpcontratacion
(idtipocontratacion, name, description)
values ('01','Empleado','Empleado con contrato laboral de cuenta ajena');

insert into personalmaster.tpcontratacion
(idtipocontratacion, name, description)
values ('02','Profesional','Freelance que trabaja con nosotros');



select * from  personalmaster.employees_aux_borrar

-- transcodificacion

update personalmaster.employees_aux_borrar
set employee_type = '01'
where employee_type  = 'EMPLEADO';

update personalmaster.employees_aux_borrar
set employee_type = '02'
where employee_type  = 'PROFESIONAL';



--- PUESTOS

create table personalmaster.jobs(
	idjob varchar(100) not null, --PK
	name varchar(256) not null,
	description varchar(512) null
);

alter table personalmaster.jobs
add constraint jobs_PK primary key(idjob);



select distinct job from personalmaster.employees_aux_borrar



insert into jobs (idjob, name, description) values()



insert into personalmaster.jobs (idjob, name, description) values('01','DISEÑADOR','');
insert into personalmaster.jobs (idjob, name, description) values('02','MAQUETADOR','');
insert into personalmaster.jobs (idjob, name, description) values('03','PROGRAMADOR','');
insert into personalmaster.jobs (idjob, name, description) values('04','IOS JUNIOR','');
insert into personalmaster.jobs (idjob, name, description) values('05','EXPERTO EN REDES NEURONALES','');
insert into personalmaster.jobs (idjob, name, description) values('06','PROG. WEB ANGULAR','');
insert into personalmaster.jobs (idjob, name, description) values('07','IOS SENIOR','');
insert into personalmaster.jobs (idjob, name, description) values('08','ANALISTA','');
insert into personalmaster.jobs (idjob, name, description) values('09','DISEÑADOR JUNIOR','');
insert into personalmaster.jobs (idjob, name, description) values('10','PROG. WEB REACT','');
insert into personalmaster.jobs (idjob, name, description) values('11','EXPERTO NLP','');
insert into personalmaster.jobs (idjob, name, description) values('12','ANDROID SENIOR','');
insert into personalmaster.jobs (idjob, name, description) values('13','DISEÑADOR SENIOR','');
insert into personalmaster.jobs (idjob, name, description) values('14','CIENTIFICO DE DATOS','');
insert into personalmaster.jobs (idjob, name, description) values('15','EXPERTO ML','');
insert into personalmaster.jobs (idjob, name, description) values('16','PROFESIONAL','');

select * from personalmaster.jobs


select * from personalmaster.employees_aux_borrar


update personalmaster.employees_aux_borrar set job = '01' where job = 'DISEÑADOR';
update personalmaster.employees_aux_borrar set job = '02' where job = 'MAQUETADOR';
update personalmaster.employees_aux_borrar set job = '03' where job = 'PROGRAMADOR';
update personalmaster.employees_aux_borrar set job = '04' where job = 'IOS JUNIOR';
update personalmaster.employees_aux_borrar set job = '05' where job = 'EXPERTO EN REDES NEURONALES';
update personalmaster.employees_aux_borrar set job = '06' where job = 'PROG. WEB ANGULAR';
update personalmaster.employees_aux_borrar set job = '07' where job = 'IOS SENIOR';
update personalmaster.employees_aux_borrar set job = '08' where job = 'ANALISTA';
update personalmaster.employees_aux_borrar set job = '09' where job = 'DISEÑADOR JUNIOR';
update personalmaster.employees_aux_borrar set job = '10' where job = 'PROG. WEB REACT';
update personalmaster.employees_aux_borrar set job = '11' where job = 'EXPERTO NLP';
update personalmaster.employees_aux_borrar set job = '12' where job = 'ANDROID SENIOR';
update personalmaster.employees_aux_borrar set job = '13' where job = 'DISEÑADOR SENIOR';
update personalmaster.employees_aux_borrar set job = '14' where job = 'CIENTIFICO DE DATOS';
update personalmaster.employees_aux_borrar set job = '15' where job = 'EXPERTO ML';
update personalmaster.employees_aux_borrar set job = '16' where job = 'PROFESIONAL';






-- Tabla de empleados

create table personalmaster.employees(

	id_person varchar(10) not null, --PK, FK
	dt_hire date not null,  --PK, FK
	dt_termination date not null default '4000-01-01', 
	dt_seniority date not null  default '4000-01-01', 
	id_reason_hire varchar(100) not null, --FK
	id_reason_termination varchar(100) not null, --FK
	idtpcontratacion varchar(100) not null -- FK
);

alter table personalmaster.employees
add constraint employees_PK primary key (id_person, dt_hire);

--FK's
alter table personalmaster.employees
add constraint  employees_person_FK foreign key (id_person) 
references personalmaster.person(id_person);

alter table personalmaster.employees
add constraint employees_motivo_alta_FK foreign key (id_reason_hire)
references personalmaster.motivos(id_reason);

alter table personalmaster.employees
add constraint employees_motivo_baja_FK foreign key (id_reason_termination)
references personalmaster.motivos(id_reason);

alter table personalmaster.employees
add constraint employess_tp_contratacion_FK foreign key (idtpcontratacion)
references personalmaster.tpcontratacion(idtipocontratacion);




--cargar la tabla de empleados con insert-select
insert into personalmaster.employees 
(id_person, dt_hire, dt_termination, dt_seniority, id_reason_hire, id_reason_termination, idtpcontratacion)
select id_person , dt_hire , dt_termination , dt_seniority , reason_hire , reason_termination , employee_type 
from personalmaster.employees_aux_borrar 


select * from  personalmaster.employees_aux_borrar 

select * from personalmaster.employees 





-- Historico de puestos


create table personalmaster.hist_jobs_employee(
	id_person varchar(10) not null, --PK, FK
	dt_hire date not null,  --PK, FK
	dt_start date not null, --PK
	dt_end date not null default '4000-01-01',
	id_job varchar(100) not null, --FK
	description varchar(512) null
	
);

alter table personalmaster.hist_jobs_employee
add constraint hist_jobs_employee_PK primary key(id_person, dt_hire, dt_start);


--FK

alter table personalmaster.hist_jobs_employee
add constraint hist_jobs_employee_FK1 foreign key(id_person,dt_hire)
references personalmaster.employees(id_person,dt_hire);


alter table personalmaster.hist_jobs_employee
add constraint hist_jobs_employee_FK2 foreign key(id_job)
references personalmaster.jobs(idjob);



insert into personalmaster.hist_jobs_employee
(id_person,dt_hire, dt_start, id_job, description)
select id_person , dt_hire , dt_hire , job , 'carga inicial'
from personalmaster.employees_aux_borrar;




select * from personalmaster.hist_jobs_employee


--al final-...oodhuafv
--borrar la tabla
--drop table personalmaster.employees_aux_borrar ;





select a.id_person , a."name" , a.apell1 , a.apell2 , b.dt_hire , c.id_job  , d."name" 
from  personalmaster.person a ,  personalmaster.employees b ,  personalmaster.hist_jobs_employee c 
,  personalmaster.jobs d
where  a.id_person = b.id_person and b.id_person  = c.id_person  and b.dt_hire  = c.dt_hire 
and c.id_job  = d.idjob 
and c.id_job  =  '01'














