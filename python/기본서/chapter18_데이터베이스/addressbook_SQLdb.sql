DROP TABLE if EXISTS addressbook; 
CREATE TABLE addressbook(
	num  INT AUTO_INCREMENT PRIMARY KEY,
	NAME VARCHAR(50) NOT NULL,
	phone VARCHAR(20) NOT NULL,
	email VARCHAR(60) NOT NULL,
	addr VARCHAR(60) NOT NULL
);
	
INSERT INTO addressbook(NAME, phone, email, addr)
SELECT CONCAT(first_name,' ',last_name), '010-1111-1111', CONCAT(first_name, '@mail.com'), '서울'
FROM employees;

SELECT * FROM addressbook
ORDER BY NAME
LIMIT 120,20;



