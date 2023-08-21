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

SET SQL_SAFE_UPDATES=0;

UPDATE product SET price=50 WHERE name='奶茶';
UPDATE product SET name='文山青茶', price=25 WHERE name='青茶';
UPDATE product SET price=35 WHERE price<=35;
UPDATE product SET price=price+5;

DELETE FROM product WHERE name='綠乃茶';
DELETE FROM product;

DROP TABLE product;