SHOW DATABASES;
CREATE DATABASE website;
USE website;
SHOW TABLES;
CREATE TABLE member(
	id BIGINT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL ,
    follower_count INT UNSIGNED NOT NULL DEFAULT 0,
    time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE message(
	id BIGINT PRIMARY KEY AUTO_INCREMENT,
    member_id BIGINT NOT NULL, /* 外鍵對應 */
	content VARCHAR(255) NOT NULL,
    like_count INT UNSIGNED NOT NULL DEFAULT 0,
    time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO member(name, username, password,follower_count, time) VALUES('Andy', 'test', 'test', 1, CURRENT_TIMESTAMP);
INSERT INTO member(name, username, password,follower_count, time) VALUES('Bndy', 'test2', 'test2', 2, CURRENT_TIMESTAMP);
INSERT INTO member(name, username, password,follower_count, time) VALUES('Cndy', 'test3', 'test3', 3, CURRENT_TIMESTAMP);
INSERT INTO member(name, username, password,follower_count, time) VALUES('Dndy', 'test4', 'test4', 4, CURRENT_TIMESTAMP);
INSERT INTO member(name, username, password,follower_count, time) VALUES('Endy', 'test5', 'test5', 5, CURRENT_TIMESTAMP);

SELECT * FROM member;
SELECT * FROM member ORDER BY time;
SELECT * FROM member ORDER BY time LIMIT 3 OFFSET 1;
SELECT * FROM member WHERE username='test';
SELECT * FROM member WHERE username='test' and password='test';
SET SQL_SAFE_UPDATES=0;
UPDATE member SET name='test2' WHERE username='test';

SELECT COUNT(name) FROM member;
SELECT COUNT(follower_count) FROM member;
SELECT AVG(follower_count) FROM member;

INSERT INTO message(member_id, content, like_count, time) VALUES('01', '哈哈哈', 12, CURRENT_TIMESTAMP);
INSERT INTO message(member_id, content, like_count, time) VALUES('02', '呵呵呵', 1, CURRENT_TIMESTAMP);
INSERT INTO message(member_id, content, like_count, time) VALUES('03', '讚讚讚', 21, CURRENT_TIMESTAMP);
INSERT INTO message(member_id, content, like_count, time) VALUES('04', '爛爛爛', 3, CURRENT_TIMESTAMP);
INSERT INTO message(member_id, content, like_count, time) VALUES('05', 'ZZZZZZ', 100, CURRENT_TIMESTAMP);

ALTER TABLE message ADD FOREIGN KEY(member_id) REFERENCES member(id);

SELECT member.name, message.content FROM member INNER JOIN message ON member.id=message.member_id;
SELECT member.name, message.content FROM member INNER JOIN message ON member.id=message.member_id WHERE username='test';
SELECT AVG(message.like_count) FROM member INNER JOIN message ON member.id=message.member_id WHERE username='test';


DROP TABLE member;
DROP TABLE message;
DROP DATABASE website;
