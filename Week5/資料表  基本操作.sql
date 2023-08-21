SHOW DATABASES;
CREATE DATABASE mydb;
DROP DATABASE mydb;
USE mydb;
SHOW TABLES;
CREATE TABLE PRODUCT(
	id INT,
    name VARCHAR(255),
    price INT
);
SELECT * FROM product;
INSERT INTO product(id, name ,price) VALUES(1, '拿鐵', 50);
INSERT INTO product(id, name ,price) VALUES(2, '美式', 40);