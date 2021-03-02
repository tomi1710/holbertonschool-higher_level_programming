-- creates the table unique_id on your MySQL server

CREATE TABLE IF NOT EXISTS unique_id (id INT(DEFAULT VALUE 1) NOT NULL UNIQUE ,
name VARCHAR(256) NOT NULL);