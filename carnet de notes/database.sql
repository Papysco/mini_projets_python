
CREATE TABLE Notes (
	id int NOT NULL,
	titre VARCHAR(255) NOT NULL,
	description VARCHAR(255),
	date_creation DATE
);

ALTER TABLE Notes 
	ADD CONSTRAINT pk_Notes PRIMARY KEY(id);


