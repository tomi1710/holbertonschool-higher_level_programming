-- creates the table unique_id on your MySQL server

CREATE TABLE IF NOT EXISTS unique_id (UNIQUE(id INT(1)) ,
name VARCHAR(256) NOT NULL);