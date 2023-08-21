SHOW DATABASES;
USE mydb;
SHOW TABLES;
CREATE TABLE PRODUCT(
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    price INT NOT NULL DEFAULT 30
);

INSERT INTO product(id, name, price) VALUES(1, '拿鐵', 50);
INSERT INTO product(id, name, price) VALUES(2, '美式', 40);
INSERT INTO product(id, name, price) VALUES(3, '奶茶', 30);
INSERT INTO product(name, price) VALUES('綠茶', 30);
INSERT INTO product(name, price) VALUES('綠乃茶', 40);
INSERT INTO product(name) VALUES('青茶');
SELECT * FROM product;
DROP TABLE product;
SELECT * FROM product WHERE price=40;
SELECT * FROM product WHERE price>30;
SELECT * FROM product WHERE price<>50 and name='美式';
SELECT * FROM product WHERE name='青茶';
SELECT * FROM product WHERE name='奶茶' or price=30;
 
SELECT name FROM product WHERE price=40;
SELECT name,price FROM product WHERE price=40;