-- Create by Tomas de Castro for Holberton School 2021

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(PRIMARY KEY(id), id INT NOT NULL AUTO_INCREMENT, 
state_id INT NOT NULL, name VARCHAR(256) NOT NULL, FOREIGN KEY(state_id) REFERENCES states(id)
);
