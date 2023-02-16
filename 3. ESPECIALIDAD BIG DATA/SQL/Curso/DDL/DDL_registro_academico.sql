create table facultad(
  id serial,
  nombre varchar(45),   
  primary key (id)
)

create table departamento(
  id serial,
  nombre varchar(45),   
  id_facultad integer,
  primary key (id),
  foreign key (id_facultad) references facultad(id)
)

alter table departamento rename to depto

alter table depto rename column nombre to nombre_depto

drop table depto