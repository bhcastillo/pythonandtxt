BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "usuario" (
	"Tipo_identidica"	TEXT,
	"Num_identifica"	INTEGER,
	"Nombre"	TEXT,
	"Direccion"	TEXT,
	"Cod_Ciudad"	INTEGER,
	"Cod_depart"	INTEGER,
	"Celular"	INTEGER,
	"Cod_profesion"	INTEGER,
	"Saldo"	INTEGER,
	PRIMARY KEY("Num_identifica")
);
INSERT INTO "usuario" VALUES ('c.c.',12,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "usuario" VALUES ('c.c',34243243,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
COMMIT;
