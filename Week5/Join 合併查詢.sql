SHOW DATABASES;
USE mydb;
SHOW TABLES;
CREATE TABLE product(
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL
);
CREATE TABLE varient(
	id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT,
    size VARCHAR(2) NOT NULL,
    price INT NOT NULL DEFAULT 30
);

INSERT INTO product(name) VALUES('美式');
INSERT INTO product(name) VALUES('拿鐵');
INSERT INTO product(name) VALUES('奶茶');

SELECT * FROM product;

INSERT INTO varient(product_id, size, price) VALUES(1, '中杯', 40);
INSERT INTO varient(product_id, size, price) VALUES(1, '大杯', 50);
INSERT INTO varient(product_id, size, price) VALUES(2, '中杯', 50);
INSERT INTO varient(product_id, size, price) VALUES(2, '大杯', 60);
INSERT INTO varient(product_id, size, price) VALUES(3, '中杯', 45);
INSERT INTO varient(product_id, size, price) VALUES(3, '大杯', 55);

SELECT * FROM varient;

SELECT product.name, varient.size, varient.price FROM product 
INNER JOIN varient ON product.id=varient.product_id;

DROP TABLE product;