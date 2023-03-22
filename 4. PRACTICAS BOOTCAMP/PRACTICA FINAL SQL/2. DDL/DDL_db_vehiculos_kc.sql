-- Model Author: Dianamtlopez
-- object: dianamtlopez | type: ROLE --
-- DROP ROLE IF EXISTS dianamtlopez;
CREATE ROLE dianamtlopez WITH 
	INHERIT;
-- ddl-end --
COMMENT ON ROLE dianamtlopez IS E'Rol creado para la presentación de la práctica de SQL';
-- ddl-end --


-- Database creation must be performed outside a multi lined SQL file. 
-- These commands were put in this file only as a convenience.
-- 
-- object: vehiculos_kc | type: DATABASE --
-- DROP DATABASE IF EXISTS vehiculos_kc;
CREATE DATABASE vehiculos_kc
	OWNER = dianamtlopez;
-- ddl-end --
COMMENT ON DATABASE vehiculos_kc IS E'BD que almacena los vehiculos que pertenecen al parque automotor de Keepcodin, asi mismo almacenar todos los procesos realizados con sus vehiculos';
-- ddl-end --


-- object: practica_vehiculos | type: SCHEMA --
-- DROP SCHEMA IF EXISTS practica_vehiculos CASCADE;
CREATE SCHEMA practica_vehiculos;
-- ddl-end --
ALTER SCHEMA practica_vehiculos OWNER TO dianamtlopez;
-- ddl-end --

SET search_path TO pg_catalog,public,practica_vehiculos;
-- ddl-end --

-- object: practica_vehiculos.fabricante_vehiculo | type: TABLE --
-- DROP TABLE IF EXISTS practica_vehiculos.fabricante_vehiculo CASCADE;
CREATE TABLE practica_vehiculos.fabricante_vehiculo (
	id_modelo serial NOT NULL,
	modelo varchar(25) NOT NULL,
	marca varchar(15) NOT NULL,
	"grupo_empresarial" varchar(20) NOT NULL,
	CONSTRAINT fabricante_vehiculo_pk PRIMARY KEY (id_modelo)
);
-- ddl-end --
COMMENT ON TABLE practica_vehiculos.fabricante_vehiculo IS E'Tabla creada para almacenar los diferentes vehiculos que la empresa puede adqquirir';
-- ddl-end --
COMMENT ON COLUMN practica_vehiculos.fabricante_vehiculo.id_modelo IS E'Columna que almacena la identificacion de cada vehiculo';
-- ddl-end --
COMMENT ON COLUMN practica_vehiculos.fabricante_vehiculo.modelo IS E'Columna que almacena el modelo del vehículo';
-- ddl-end --
COMMENT ON COLUMN practica_vehiculos.fabricante_vehiculo.marca IS E'Columna que almacena la marca del vehículo';
-- ddl-end --
COMMENT ON COLUMN practica_vehiculos.fabricante_vehiculo."grupo_empresarial" IS E'Columna que almacena el grupo empresarial al que pertenece el vehículo';
-- ddl-end --
ALTER TABLE practica_vehiculos.fabricante_vehiculo OWNER TO dianamtlopez;
-- ddl-end --

-- object: practica_vehiculos.empresa_vehiculo | type: TABLE --
-- DROP TABLE IF EXISTS practica_vehiculos.empresa_vehiculo CASCADE;
CREATE TABLE practica_vehiculos.empresa_vehiculo (
	matricula varchar(10) NOT NULL,
	color varchar(10) NOT NULL,
	fecha_compra date NOT NULL,
	id_modelo integer NOT NULL,
	CONSTRAINT empresa_vehiculo_pk PRIMARY KEY (matricula)
);
-- ddl-end --
COMMENT ON COLUMN practica_vehiculos.empresa_vehiculo.matricula IS E'Columna que almacena la matrícula del vehículo';
-- ddl-end --
COMMENT ON COLUMN practica_vehiculos.empresa_vehiculo.color IS E'Columna que almacena el color del vehículo';
-- ddl-end --
COMMENT ON COLUMN practica_vehiculos.empresa_vehiculo.fecha_compra IS E'Columna que almacena la fecha de compra del vehículo';
-- ddl-end --
ALTER TABLE practica_vehiculos.empresa_vehiculo OWNER TO dianamtlopez;
-- ddl-end --

-- object: fabricante_vehiculo_fk | type: CONSTRAINT --
-- ALTER TABLE practica_vehiculos.empresa_vehiculo DROP CONSTRAINT IF EXISTS fabricante_vehiculo_fk CASCADE;
ALTER TABLE practica_vehiculos.empresa_vehiculo ADD CONSTRAINT fabricante_vehiculo_fk FOREIGN KEY (id_modelo)
REFERENCES practica_vehiculos.fabricante_vehiculo (id_modelo) MATCH FULL
ON DELETE RESTRICT ON UPDATE CASCADE;
-- ddl-end --

-- object: practica_vehiculos.poliza_empresa | type: TABLE --
-- DROP TABLE IF EXISTS practica_vehiculos.poliza_empresa CASCADE;
CREATE TABLE practica_vehiculos.poliza_empresa (
	codigo_poliza varchar(10) NOT NULL,
	id_aseguradora varchar(10) NOT NULL,
	matricula varchar(10) NOT NULL,
	fecha_poliza date NOT NULL,
	kilometraje float NOT NULL,
	id_divisa integer NOT NULL,
	importe_poliza float NOT NULL,
	CONSTRAINT poliza_empresa_pk PRIMARY KEY (codigo_poliza)
);
-- ddl-end --
COMMENT ON TABLE practica_vehiculos.poliza_empresa IS E'Tabla que almacena las polizas que se adquieren para los vehiculos de Keepcoding';
-- ddl-end --
COMMENT ON COLUMN practica_vehiculos.poliza_empresa.codigo_poliza IS E'Columna que almacena el número de la póliza parra cada vehiculo';
-- ddl-end --
COMMENT ON COLUMN practica_vehiculos.poliza_empresa.fecha_poliza IS E'Columna que almacena la fecha en la que se adquirió la póliza para cada vehículo de Keepcoding';
-- ddl-end --
COMMENT ON COLUMN practica_vehiculos.poliza_empresa.kilometraje IS E'Columna que almacena el kilometraje que tiene el vehículo en el momento de adquirir la póliza';
-- ddl-end --
COMMENT ON COLUMN practica_vehiculos.poliza_empresa.importe_poliza IS E'Columna que almacena el valor de la póliza';
-- ddl-end --
ALTER TABLE practica_vehiculos.poliza_empresa OWNER TO dianamtlopez;
-- ddl-end --

-- object: empresa_vehiculo_fk | type: CONSTRAINT --
-- ALTER TABLE practica_vehiculos.poliza_empresa DROP CONSTRAINT IF EXISTS empresa_vehiculo_fk CASCADE;
ALTER TABLE practica_vehiculos.poliza_empresa ADD CONSTRAINT empresa_vehiculo_fk FOREIGN KEY (matricula)
REFERENCES practica_vehiculos.empresa_vehiculo (matricula) MATCH FULL
ON DELETE RESTRICT ON UPDATE CASCADE;
-- ddl-end --

-- object: practica_vehiculos.empresa_revision | type: TABLE --
-- DROP TABLE IF EXISTS practica_vehiculos.empresa_revision CASCADE;
CREATE TABLE practica_vehiculos.empresa_revision (
	consecutivo serial NOT NULL,
	id_revision integer NOT NULL,
	fecha_revision date NOT NULL,
	matricula varchar(10) NOT NULL,
	kilometraje_revision float NOT NULL,
	id_divisa integer NOT NULL,
	importe_revision float NOT NULL,
	CONSTRAINT empresa_revision_pk PRIMARY KEY (consecutivo)
);
-- ddl-end --
COMMENT ON TABLE practica_vehiculos.empresa_revision IS E'Tabla que almacena las revisiones tecnico mecánicas de los vehículos que pertenecen a Keepcoding';
-- ddl-end --
COMMENT ON COLUMN practica_vehiculos.empresa_revision.consecutivo IS E'Columna que almacena el consecutivo de las revisiones tecnico mecánicas';
-- ddl-end --
COMMENT ON COLUMN practica_vehiculos.empresa_revision.fecha_revision IS E'Columna que almacena la fecha en la cual se ha sacado la revision tecnico mecánica';
-- ddl-end --
COMMENT ON COLUMN practica_vehiculos.empresa_revision.kilometraje_revision IS E'Columna que almacena el kilometraje que tiene el vehículo en el momento de la revision';
-- ddl-end --
COMMENT ON COLUMN practica_vehiculos.empresa_revision.importe_revision IS E'Columna que almacena el valor cancelado por la revisión tecnico mecánica';
-- ddl-end --
ALTER TABLE practica_vehiculos.empresa_revision OWNER TO dianamtlopez;
-- ddl-end --

-- object: empresa_vehiculo_fk | type: CONSTRAINT --
-- ALTER TABLE practica_vehiculos.empresa_revision DROP CONSTRAINT IF EXISTS empresa_vehiculo_fk CASCADE;
ALTER TABLE practica_vehiculos.empresa_revision ADD CONSTRAINT empresa_vehiculo_fk FOREIGN KEY (matricula)
REFERENCES practica_vehiculos.empresa_vehiculo (matricula) MATCH FULL
ON DELETE RESTRICT ON UPDATE CASCADE;
-- ddl-end --

-- object: practica_vehiculos.aseguradora | type: TABLE --
-- DROP TABLE IF EXISTS practica_vehiculos.aseguradora CASCADE;
CREATE TABLE practica_vehiculos.aseguradora (
	id_aseguradora varchar(10) NOT NULL,
	nombre_aseguradora varchar(70) NOT NULL,
	CONSTRAINT aseguradora_pk PRIMARY KEY (id_aseguradora)
);
-- ddl-end --
COMMENT ON TABLE practica_vehiculos.aseguradora IS E'Tabla que almacena las diferentes aseguradoras que proporcionan polizas para los vehículos de Keepcoding';
-- ddl-end --
COMMENT ON COLUMN practica_vehiculos.aseguradora.id_aseguradora IS E'Columna que almacena la identificacion de la aseguradora';
-- ddl-end --
COMMENT ON COLUMN practica_vehiculos.aseguradora.nombre_aseguradora IS E'Coolumna que almacena los nombres de las aseguradoras qie proporcionan las pólizas';
-- ddl-end --
ALTER TABLE practica_vehiculos.aseguradora OWNER TO dianamtlopez;
-- ddl-end --

-- object: aseguradora_fk | type: CONSTRAINT --
-- ALTER TABLE practica_vehiculos.poliza_empresa DROP CONSTRAINT IF EXISTS aseguradora_fk CASCADE;
ALTER TABLE practica_vehiculos.poliza_empresa ADD CONSTRAINT aseguradora_fk FOREIGN KEY (id_aseguradora)
REFERENCES practica_vehiculos.aseguradora (id_aseguradora) MATCH FULL
ON DELETE RESTRICT ON UPDATE CASCADE;
-- ddl-end --

-- object: practica_vehiculos.divisa | type: TABLE --
-- DROP TABLE IF EXISTS practica_vehiculos.divisa CASCADE;
CREATE TABLE practica_vehiculos.divisa (
	id_divisa serial NOT NULL,
	nombre_divisa varchar(25) NOT NULL,
	sigla varchar(5) NOT NULL,
	CONSTRAINT divisa_pk PRIMARY KEY (id_divisa)
);
-- ddl-end --
COMMENT ON TABLE practica_vehiculos.divisa IS E'Columna que almacena las divisas en las cuales se puede negociar';
-- ddl-end --
COMMENT ON COLUMN practica_vehiculos.divisa.id_divisa IS E'Columna que almacena el id de la divisa en la cual se negocia';
-- ddl-end --
COMMENT ON COLUMN practica_vehiculos.divisa.nombre_divisa IS E'Columna que almacena el nombre de la divisa en la que se puede negociar';
-- ddl-end --
COMMENT ON COLUMN practica_vehiculos.divisa.sigla IS E'Columna que almacena la sigla de la divisa en la cual se negocia';
-- ddl-end --
ALTER TABLE practica_vehiculos.divisa OWNER TO dianamtlopez;
-- ddl-end --

-- object: divisa_fk | type: CONSTRAINT --
-- ALTER TABLE practica_vehiculos.poliza_empresa DROP CONSTRAINT IF EXISTS divisa_fk CASCADE;
ALTER TABLE practica_vehiculos.poliza_empresa ADD CONSTRAINT divisa_fk FOREIGN KEY (id_divisa)
REFERENCES practica_vehiculos.divisa (id_divisa) MATCH FULL
ON DELETE RESTRICT ON UPDATE CASCADE;
-- ddl-end --

-- object: practica_vehiculos.revision | type: TABLE --
-- DROP TABLE IF EXISTS practica_vehiculos.revision CASCADE;
CREATE TABLE practica_vehiculos.revision (
	id_revision serial NOT NULL,
	descripcion varchar(15) NOT NULL,
	CONSTRAINT revision_pk PRIMARY KEY (id_revision)
);
-- ddl-end --
COMMENT ON TABLE practica_vehiculos.revision IS E'Tabla que almacena las descripciones de lass revisiones tecnico mecánicas de los vehiculos';
-- ddl-end --
COMMENT ON COLUMN practica_vehiculos.revision.id_revision IS E'Columna que almacena el identificador de las revisiones';
-- ddl-end --
COMMENT ON COLUMN practica_vehiculos.revision.descripcion IS E'Columna que almacena la descripción de las revisiones tecnico mecánicas';
-- ddl-end --
ALTER TABLE practica_vehiculos.revision OWNER TO dianamtlopez;
-- ddl-end --

-- object: revision_fk | type: CONSTRAINT --
-- ALTER TABLE practica_vehiculos.empresa_revision DROP CONSTRAINT IF EXISTS revision_fk CASCADE;
ALTER TABLE practica_vehiculos.empresa_revision ADD CONSTRAINT revision_fk FOREIGN KEY (id_revision)
REFERENCES practica_vehiculos.revision (id_revision) MATCH FULL
ON DELETE RESTRICT ON UPDATE CASCADE;
-- ddl-end --

-- object: divisa_fk | type: CONSTRAINT --
-- ALTER TABLE practica_vehiculos.empresa_revision DROP CONSTRAINT IF EXISTS divisa_fk CASCADE;
ALTER TABLE practica_vehiculos.empresa_revision ADD CONSTRAINT divisa_fk FOREIGN KEY (id_divisa)
REFERENCES practica_vehiculos.divisa (id_divisa) MATCH FULL
ON DELETE RESTRICT ON UPDATE CASCADE;
-- ddl-end --

