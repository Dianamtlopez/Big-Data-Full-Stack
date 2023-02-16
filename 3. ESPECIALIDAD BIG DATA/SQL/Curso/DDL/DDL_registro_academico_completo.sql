-- Database generated with pgModeler (PostgreSQL Database Modeler).
-- pgModeler version: 0.9.4
-- PostgreSQL version: 13.0
-- Project Site: pgmodeler.io
-- Model Author: ---

-- Database creation must be performed outside a multi lined SQL file. 
-- These commands were put in this file only as a convenience.
-- 
-- object: registro_academico | type: DATABASE --
-- DROP DATABASE IF EXISTS registro_academico;
CREATE DATABASE registro_academico;
-- ddl-end --


-- object: public.estudiante | type: TABLE --
-- DROP TABLE IF EXISTS public.estudiante CASCADE;
CREATE TABLE public.estudiante (
	codigo serial NOT NULL,
	nombre varchar(45) NOT NULL,
	apellido varchar(45) NOT NULL,
	fecha_nacimiento date NOT NULL,
	genero char NOT NULL,
	id_departamento integer,
	CONSTRAINT estudiante_pk PRIMARY KEY (codigo)
);
-- ddl-end --
ALTER TABLE public.estudiante OWNER TO postgres;
-- ddl-end --

-- object: public.facultad | type: TABLE --
-- DROP TABLE IF EXISTS public.facultad CASCADE;
CREATE TABLE public.facultad (
	id serial NOT NULL,
	nombre varchar(45) NOT NULL,
	CONSTRAINT facultad_pk PRIMARY KEY (id)
);
-- ddl-end --
ALTER TABLE public.facultad OWNER TO postgres;
-- ddl-end --

-- object: public.departamento | type: TABLE --
-- DROP TABLE IF EXISTS public.departamento CASCADE;
CREATE TABLE public.departamento (
	id serial NOT NULL,
	nombre varchar(45) NOT NULL,
	id_facultad integer,
	CONSTRAINT departamento_pk PRIMARY KEY (id)
);
-- ddl-end --
ALTER TABLE public.departamento OWNER TO postgres;
-- ddl-end --

-- object: facultad_fk | type: CONSTRAINT --
-- ALTER TABLE public.departamento DROP CONSTRAINT IF EXISTS facultad_fk CASCADE;
ALTER TABLE public.departamento ADD CONSTRAINT facultad_fk FOREIGN KEY (id_facultad)
REFERENCES public.facultad (id) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: departamento_fk | type: CONSTRAINT --
-- ALTER TABLE public.estudiante DROP CONSTRAINT IF EXISTS departamento_fk CASCADE;
ALTER TABLE public.estudiante ADD CONSTRAINT departamento_fk FOREIGN KEY (id_departamento)
REFERENCES public.departamento (id) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: public.curso | type: TABLE --
-- DROP TABLE IF EXISTS public.curso CASCADE;
CREATE TABLE public.curso (
	id serial NOT NULL,
	nombre varchar(45) NOT NULL,
	creditos smallint NOT NULL,
	id_departamento integer,
	CONSTRAINT curso_pk PRIMARY KEY (id)
);
-- ddl-end --
ALTER TABLE public.curso OWNER TO postgres;
-- ddl-end --

-- object: departamento_fk | type: CONSTRAINT --
-- ALTER TABLE public.curso DROP CONSTRAINT IF EXISTS departamento_fk CASCADE;
ALTER TABLE public.curso ADD CONSTRAINT departamento_fk FOREIGN KEY (id_departamento)
REFERENCES public.departamento (id) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: public.profesor | type: TABLE --
-- DROP TABLE IF EXISTS public.profesor CASCADE;
CREATE TABLE public.profesor (
	id serial NOT NULL,
	nombre varchar(45) NOT NULL,
	apellido varchar(45) NOT NULL,
	id_departamento integer,
	CONSTRAINT profesor_pk PRIMARY KEY (id)
);
-- ddl-end --
ALTER TABLE public.profesor OWNER TO postgres;
-- ddl-end --

-- object: public.grupo | type: TABLE --
-- DROP TABLE IF EXISTS public.grupo CASCADE;
CREATE TABLE public.grupo (
	id serial NOT NULL,
	nombre varchar NOT NULL,
	anio smallint NOT NULL,
	periodo smallint NOT NULL,
	id_curso integer,
	id_profesor integer,
	CONSTRAINT grupo_pk PRIMARY KEY (id)
);
-- ddl-end --
ALTER TABLE public.grupo OWNER TO postgres;
-- ddl-end --

-- object: curso_fk | type: CONSTRAINT --
-- ALTER TABLE public.grupo DROP CONSTRAINT IF EXISTS curso_fk CASCADE;
ALTER TABLE public.grupo ADD CONSTRAINT curso_fk FOREIGN KEY (id_curso)
REFERENCES public.curso (id) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: profesor_fk | type: CONSTRAINT --
-- ALTER TABLE public.grupo DROP CONSTRAINT IF EXISTS profesor_fk CASCADE;
ALTER TABLE public.grupo ADD CONSTRAINT profesor_fk FOREIGN KEY (id_profesor)
REFERENCES public.profesor (id) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: public.inscripcion | type: TABLE --
-- DROP TABLE IF EXISTS public.inscripcion CASCADE;
CREATE TABLE public.inscripcion (
	calificacion smallint NOT NULL DEFAULT 0,
	codigo_estudiante integer NOT NULL,
	id_grupo integer NOT NULL,
	CONSTRAINT inscripcion_pk PRIMARY KEY (codigo_estudiante,id_grupo)
);
-- ddl-end --
ALTER TABLE public.inscripcion OWNER TO postgres;
-- ddl-end --

-- object: estudiante_fk | type: CONSTRAINT --
-- ALTER TABLE public.inscripcion DROP CONSTRAINT IF EXISTS estudiante_fk CASCADE;
ALTER TABLE public.inscripcion ADD CONSTRAINT estudiante_fk FOREIGN KEY (codigo_estudiante)
REFERENCES public.estudiante (codigo) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: grupo_fk | type: CONSTRAINT --
-- ALTER TABLE public.inscripcion DROP CONSTRAINT IF EXISTS grupo_fk CASCADE;
ALTER TABLE public.inscripcion ADD CONSTRAINT grupo_fk FOREIGN KEY (id_grupo)
REFERENCES public.grupo (id) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: departamento_fk | type: CONSTRAINT --
-- ALTER TABLE public.profesor DROP CONSTRAINT IF EXISTS departamento_fk CASCADE;
ALTER TABLE public.profesor ADD CONSTRAINT departamento_fk FOREIGN KEY (id_departamento)
REFERENCES public.departamento (id) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --


