-- Create by Tomas de Castro for Holberton School 2021

SELECT id, name FROM cities WHERE state_id IN (SELECT id FROM states WHERE name = "California") ORDER BY id;
