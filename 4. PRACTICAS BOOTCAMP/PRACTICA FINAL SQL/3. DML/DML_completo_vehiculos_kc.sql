-- Model Author: Dianamtlopez 
-- object: practica_vehiculos_kc | type: DATABASE --

-- Table fabricante_vehiculo --
INSERT INTO practica_vehiculos.fabricante_vehiculo (id_modelo, modelo, marca, grupo_empresarial) VALUES (1, '100 4A/C4', 'Audi', 'Avant Berlina');
INSERT INTO practica_vehiculos.fabricante_vehiculo (id_modelo, modelo, marca, grupo_empresarial) VALUES (2, '100 S2', 'Audi', 'Sedan');
INSERT INTO practica_vehiculos.fabricante_vehiculo (id_modelo, modelo, marca, grupo_empresarial) VALUES (3, '80 8A/B3', 'Audi', 'Sedan');
INSERT INTO practica_vehiculos.fabricante_vehiculo (id_modelo, modelo, marca, grupo_empresarial) VALUES (4, 'Sedici 1 generacion', 'Fiat', 'Hatchback');
INSERT INTO practica_vehiculos.fabricante_vehiculo (id_modelo, modelo, marca, grupo_empresarial) VALUES (5, 'Stilo 1 generacion', 'Fiat', 'Hatchback 3-puertas');
INSERT INTO practica_vehiculos.fabricante_vehiculo (id_modelo, modelo, marca, grupo_empresarial) VALUES (6, 'Ulysse 1 generacion', 'Fiat', 'Minivan');
INSERT INTO practica_vehiculos.fabricante_vehiculo (id_modelo, modelo, marca, grupo_empresarial) VALUES (7, 'Doblo 1 generacion', 'Fiat', 'Panorama Minivan');
-- dml-end --

-- Table empresa_vehiculo --
INSERT INTO practica_vehiculos.empresa_vehiculo(matricula, id_modelo, color, fecha_compra) VALUES ('0262-JKT', 1, 'blanco', '03/08/2022');
INSERT INTO practica_vehiculos.empresa_vehiculo(matricula, id_modelo, color, fecha_compra) VALUES ('1027-JLF', 1, 'amarillo', '03/08/2022');
INSERT INTO practica_vehiculos.empresa_vehiculo(matricula, id_modelo, color, fecha_compra) VALUES ('2324-JGL', 2, 'azul', '04/08/2022');
INSERT INTO practica_vehiculos.empresa_vehiculo(matricula, id_modelo, color, fecha_compra) VALUES ('8580-HYV', 2, 'rojo', '04/08/2022');
INSERT INTO practica_vehiculos.empresa_vehiculo(matricula, id_modelo, color, fecha_compra) VALUES ('3488-DTM', 3, 'negro', '05/08/2022');
INSERT INTO practica_vehiculos.empresa_vehiculo(matricula, id_modelo, color, fecha_compra) VALUES ('5157-DVS', 3, 'gris', '05/08/2022');
INSERT INTO practica_vehiculos.empresa_vehiculo(matricula, id_modelo, color, fecha_compra) VALUES ('0011-KDJ', 4, 'verde', '06/08/2022');
INSERT INTO practica_vehiculos.empresa_vehiculo(matricula, id_modelo, color, fecha_compra) VALUES ('0276-KHP', 4, 'blanco', '06/08/2022');
INSERT INTO practica_vehiculos.empresa_vehiculo(matricula, id_modelo, color, fecha_compra) VALUES ('0336-CNK', 5, 'amarillo', '07/08/2022');
INSERT INTO practica_vehiculos.empresa_vehiculo(matricula, id_modelo, color, fecha_compra) VALUES ('0670-JBP', 5, 'azul', '07/08/2022');
INSERT INTO practica_vehiculos.empresa_vehiculo(matricula, id_modelo, color, fecha_compra) VALUES ('0760-CCW', 6, 'rojo', '08/08/2022');
INSERT INTO practica_vehiculos.empresa_vehiculo(matricula, id_modelo, color, fecha_compra) VALUES ('1468-JRC', 6, 'negro', '08/08/2022');
INSERT INTO practica_vehiculos.empresa_vehiculo(matricula, id_modelo, color, fecha_compra) VALUES ('1889-CJS', 7, 'gris', '09/08/2022');
INSERT INTO practica_vehiculos.empresa_vehiculo(matricula, id_modelo, color, fecha_compra) VALUES ('2160-GHF', 7, 'verde', '09/08/2022');
-- dml-end --

-- Table aseguradora --
INSERT INTO practica_vehiculos.aseguradora(id_aseguradora, nombre_aseguradora) VALUES ('A60917978', 'MAPFRE ESPAÑA, COMPAÑIA DE SEGUROS Y REASEGUROS, S.A.');
INSERT INTO practica_vehiculos.aseguradora(id_aseguradora, nombre_aseguradora) VALUES ('A70918979', 'ABANCA GENERALES DE SEGUROS Y REASEGUROS, S.A.');
INSERT INTO practica_vehiculos.aseguradora(id_aseguradora, nombre_aseguradora) VALUES ('A80919980', 'AGRUPACION SANITARIA SEGUROS, S.A.');
INSERT INTO practica_vehiculos.aseguradora(id_aseguradora, nombre_aseguradora) VALUES ('A90920981', 'AIG EUROPE S.A.');
INSERT INTO practica_vehiculos.aseguradora(id_aseguradora, nombre_aseguradora) VALUES ('A10921982', 'ALIANZA ESPAÑOLA S.A.');
INSERT INTO practica_vehiculos.aseguradora(id_aseguradora, nombre_aseguradora) VALUES ('A11092983', 'ALLIANZ LEBENSVERSICHERUNGS-AG');
INSERT INTO practica_vehiculos.aseguradora(id_aseguradora, nombre_aseguradora) VALUES ('A12093984', 'ALTER MÚTUA DE PREVISIÓ SOCIAL DELS ADVOCATS DE CATALUNYA A PRIMA FIXA');
INSERT INTO practica_vehiculos.aseguradora(id_aseguradora, nombre_aseguradora) VALUES ('A30924985', 'AMA VIDA SEGUROS Y REASEGUROS, S.A');
INSERT INTO practica_vehiculos.aseguradora(id_aseguradora, nombre_aseguradora) VALUES ('A40925986', 'ARAG SE SUC.ESPAÑA');
INSERT INTO practica_vehiculos.aseguradora(id_aseguradora, nombre_aseguradora) VALUES ('A50926987', 'AXA SEGUROS GENERALES, S. A');
-- dml-end --

-- Table revision --
INSERT INTO practica_vehiculos.revision(id_revision, descripcion) VALUES (1, 'primer año');
INSERT INTO practica_vehiculos.revision(id_revision, descripcion) VALUES (2, 'segundo año');
INSERT INTO practica_vehiculos.revision(id_revision, descripcion) VALUES (3, 'tercer año');
INSERT INTO practica_vehiculos.revision(id_revision, descripcion) VALUES (4, 'cuarto año');
INSERT INTO practica_vehiculos.revision(id_revision, descripcion) VALUES (5, 'quinto año');
INSERT INTO practica_vehiculos.revision(id_revision, descripcion) VALUES (6, 'sextoo año');
INSERT INTO practica_vehiculos.revision(id_revision, descripcion) VALUES (7, 'septimo año');
INSERT INTO practica_vehiculos.revision(id_revision, descripcion) VALUES (8, 'octavo año');
INSERT INTO practica_vehiculos.revision(id_revision, descripcion) VALUES (9, 'noveno año');
INSERT INTO practica_vehiculos.revision(id_revision, descripcion) VALUES (10, 'decimo año');
INSERT INTO practica_vehiculos.revision(id_revision, descripcion) VALUES (11, 'descontinuado');
-- dml-end --

-- Table divisa --
INSERT INTO practica_vehiculos.divisa(id_divisa, nombre_divisa, sigla) VALUES (1, 'dólar estadounidense', '(USD)');
INSERT INTO practica_vehiculos.divisa(id_divisa, nombre_divisa, sigla) VALUES (2, 'euro', '(EUR)');
INSERT INTO practica_vehiculos.divisa(id_divisa, nombre_divisa, sigla) VALUES (3, 'yen japonés', '(JPY)');
INSERT INTO practica_vehiculos.divisa(id_divisa, nombre_divisa, sigla) VALUES (4, 'libra esterlina', '(GBP)');
INSERT INTO practica_vehiculos.divisa(id_divisa, nombre_divisa, sigla) VALUES (5, 'dólar australiano', '(AUD)');
INSERT INTO practica_vehiculos.divisa(id_divisa, nombre_divisa, sigla) VALUES (6, 'dólar canadiense', '(CAD)');
INSERT INTO practica_vehiculos.divisa(id_divisa, nombre_divisa, sigla) VALUES (7, 'franco suizo', '(CHF)');
INSERT INTO practica_vehiculos.divisa(id_divisa, nombre_divisa, sigla) VALUES (8, 'renminbi chino ', '(CNH)');
INSERT INTO practica_vehiculos.divisa(id_divisa, nombre_divisa, sigla) VALUES (9, 'dólar hongkonés', '(HKD)');
INSERT INTO practica_vehiculos.divisa(id_divisa, nombre_divisa, sigla) VALUES (10, 'dólar neozelandés', '(NZD)');
-- dml-end --

-- Table poliza_empresa --
INSERT INTO practica_vehiculos.poliza_empresa(codigo_poliza, id_aseguradora, matricula, fecha_poliza, kilometraje, id_divisa, importe_poliza) VALUES (8542, 'A60917978', '0262-JKT', '01/09/20200', 50000, 1, 20);
INSERT INTO practica_vehiculos.poliza_empresa(codigo_poliza, id_aseguradora, matricula, fecha_poliza, kilometraje, id_divisa, importe_poliza) VALUES (2534, 'A70918979', '1027-JLF', '01/09/2022', 80000, 1, 20);
INSERT INTO practica_vehiculos.poliza_empresa(codigo_poliza, id_aseguradora, matricula, fecha_poliza, kilometraje, id_divisa, importe_poliza) VALUES (4893, 'A80919980', '2324-JGL', '02/09/2022', 70000, 2, 30);
INSERT INTO practica_vehiculos.poliza_empresa(codigo_poliza, id_aseguradora, matricula, fecha_poliza, kilometraje, id_divisa, importe_poliza) VALUES (1674, 'A90920981', '8580-HYV', '02/09/2022', 86666, 2, 30);
INSERT INTO practica_vehiculos.poliza_empresa(codigo_poliza, id_aseguradora, matricula, fecha_poliza, kilometraje, id_divisa, importe_poliza) VALUES (2548, 'A10921982', '3488-DTM', '03/09/2022', 96666, 3, 40);
INSERT INTO practica_vehiculos.poliza_empresa(codigo_poliza, id_aseguradora, matricula, fecha_poliza, kilometraje, id_divisa, importe_poliza) VALUES (4839, 'A11092983', '5157-DVS', '03/09/2022', 106666, 3, 40);
INSERT INTO practica_vehiculos.poliza_empresa(codigo_poliza, id_aseguradora, matricula, fecha_poliza, kilometraje, id_divisa, importe_poliza) VALUES (6438, 'A12093984', '0011-KDJ', '04/09/2022', 116666, 4, 50);
INSERT INTO practica_vehiculos.poliza_empresa(codigo_poliza, id_aseguradora, matricula, fecha_poliza, kilometraje, id_divisa, importe_poliza) VALUES (5975, 'A30924985', '0276-KHP', '04/09/2022', 126666, 4, 50);
INSERT INTO practica_vehiculos.poliza_empresa(codigo_poliza, id_aseguradora, matricula, fecha_poliza, kilometraje, id_divisa, importe_poliza) VALUES (4801, 'A40925986', '0336-CNK', '05/09/2022', 136666, 5, 60);
INSERT INTO practica_vehiculos.poliza_empresa(codigo_poliza, id_aseguradora, matricula, fecha_poliza, kilometraje, id_divisa, importe_poliza) VALUES (4828, 'A50926987', '0670-JBP', '05/09/2022', 146666, 5, 60);
INSERT INTO practica_vehiculos.poliza_empresa(codigo_poliza, id_aseguradora, matricula, fecha_poliza, kilometraje, id_divisa, importe_poliza) VALUES (4855, 'A60917978', '0760-CCW', '06/09/2022', 156666, 6, 70);
INSERT INTO practica_vehiculos.poliza_empresa(codigo_poliza, id_aseguradora, matricula, fecha_poliza, kilometraje, id_divisa, importe_poliza) VALUES (4882, 'A80919980', '1468-JRC', '06/09/2022', 166666, 6, 70);
INSERT INTO practica_vehiculos.poliza_empresa(codigo_poliza, id_aseguradora, matricula, fecha_poliza, kilometraje, id_divisa, importe_poliza) VALUES (4909, 'A70918979', '1889-CJS', '07/09/2022', 176666, 7, 80);
INSERT INTO practica_vehiculos.poliza_empresa(codigo_poliza, id_aseguradora, matricula, fecha_poliza, kilometraje, id_divisa, importe_poliza) VALUES (4936, `A90920981`, '2160-GHF', '07/09/2022', 186666, 7, 80);
-- dml-end --

-- Table empresa_revision --
INSERT INTO practica_vehiculos."empresa_revision"(consecutivo, id_revision, fecha_refision, matricula, kilometraje_revision, id_divisa, importe_revision) VALUES (1, 1, '01/12/2022', '0262-JKT', 60000, 1, 5);
INSERT INTO practica_vehiculos."empresa_revision"(consecutivo, id_revision, fecha_refision, matricula, kilometraje_revision, id_divisa, importe_revision) VALUES (2, 1, '01/12/2022', '1027-JLF', 90000, 1, 5);
INSERT INTO practica_vehiculos."empresa_revision"(consecutivo, id_revision, fecha_refision, matricula, kilometraje_revision, id_divisa, importe_revision) VALUES (3, 2, '02/12/2022', '2324-JGL', 80000, 2, 6);
INSERT INTO practica_vehiculos."empresa_revision"(consecutivo, id_revision, fecha_refision, matricula, kilometraje_revision, id_divisa, importe_revision) VALUES (4, 2, '02/12/2022', '8580-HYV', 96666, 2, 6);
INSERT INTO practica_vehiculos."empresa_revision"(consecutivo, id_revision, fecha_refision, matricula, kilometraje_revision, id_divisa, importe_revision) VALUES (5, 3, '03/12/2022', '3488-DTM', 106666, 3, 7);
INSERT INTO practica_vehiculos."empresa_revision"(consecutivo, id_revision, fecha_refision, matricula, kilometraje_revision, id_divisa, importe_revision) VALUES (6, 4, '03/12/2022', '5157-DVS', 116666, 3, 7);
INSERT INTO practica_vehiculos."empresa_revision"(consecutivo, id_revision, fecha_refision, matricula, kilometraje_revision, id_divisa, importe_revision) VALUES (7, 5, '04/12/2022', '0011-KDJ', 126666, 4, 8);
INSERT INTO practica_vehiculos."empresa_revision"(consecutivo, id_revision, fecha_refision, matricula, kilometraje_revision, id_divisa, importe_revision) VALUES (8, 6, '04/12/2022', '0276-KHP', 136666, 4, 8);
INSERT INTO practica_vehiculos."empresa_revision"(consecutivo, id_revision, fecha_refision, matricula, kilometraje_revision, id_divisa, importe_revision) VALUES (9, 6, '05/12/2022', '0336-CNK', 146666, 5, 9);
INSERT INTO practica_vehiculos."empresa_revision"(consecutivo, id_revision, fecha_refision, matricula, kilometraje_revision, id_divisa, importe_revision) VALUES (10, 7, '05/12/2022', '0670-JBP', 156666, 5, 9);
INSERT INTO practica_vehiculos."empresa_revision"(consecutivo, id_revision, fecha_refision, matricula, kilometraje_revision, id_divisa, importe_revision) VALUES (11, 8, '06/12/2022', '0760-CCW', 166666, 6, 10);
INSERT INTO practica_vehiculos."empresa_revision"(consecutivo, id_revision, fecha_refision, matricula, kilometraje_revision, id_divisa, importe_revision) VALUES (12, 9, '06/12/2022', '1468-JRC', 176666, 6, 10);
INSERT INTO practica_vehiculos."empresa_revision"(consecutivo, id_revision, fecha_refision, matricula, kilometraje_revision, id_divisa, importe_revision) VALUES (13, 10, '07/12/2012', '1889-CJS', 186666, 7, 11);
INSERT INTO practica_vehiculos."empresa_revision"(consecutivo, id_revision, fecha_refision, matricula, kilometraje_revision, id_divisa, importe_revision) VALUES (14, 11, '07/12/2022', '2160-GHF', 196666, 7, 11);
-- dml-end --

