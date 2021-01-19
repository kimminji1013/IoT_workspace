-- SELECT name, height FROM usertbl 
-- WHERE height > (SELECT height FROM usertbl where NAME=('김경호'));
-- 
-- SELECT NAME, height FROM usertbl
-- ORDER BY height DESC, NAME ASC; 
-- 
-- SELECT addr FROM usertbl ORDER BY addr;
-- 
-- SELECT DISTINCT addr FROM usertbl;


-- SELECT userID '사용자 ID', sum(price*amount) '총 구매 개수'
-- FROM buytbl
-- GROUP BY userID
-- ORDER BY userID;


-- SELECT addr, MAX(height), MIN(height) FROM usertbl
-- GROUP BY addr;

-- SELECT name, MAX(height), MIN(height) FROM usertbl;
-- --GROUP BY addr;

-- SELECT userID '사용자', SUM(price *amount) '총구매액'
-- FROM buytbl
-- GROUP BY userID
-- HAVING SUM(price*amount) > 1000;

-- CREATE TABLE testtbl4(
-- 	id INT,
-- 	Fname VARCHAR(50),
-- 	Lname VARCHAR(50)
-- );
-- 
-- INSERT INTO testtbl4 
-- SELECT emp_no, first_name, last_name
-- FROM employees.employees;
-- 
-- 
-- 
-- CREATE TABLE testtbl6
-- (SELECT emp_no id, first_name fname, last_name lname FROM employees.employees);
-- 


-- UPDATE testtbl4
-- SET Lname='없음'
-- WHERE Fname = 'Kyoichi';
-- 
-- 
-- DELETE FROM testtbl4 
-- WHERE fname='Aamer';


SELECT AVG(amount) AS '평균 구매 개수' FROM buytbl;
SELECT CAST(AVG(amount) AS SIGNED INTEGER) 
AS '평균 구매 개수' FROM buytb;  
-- 정수로 바꿔줄 때 반올림

SELECT CONVERT(AVG(amount), SIGNED INTEGER) 
AS '평균 구매 개수' FROM buytbl;

SELECT CAST('2021/10/13' AS DATE);


--문자열과 숫자를 같이 사용 못하므로 다음과 같이 하나의 형으로 사용 
SELECT num, 
CONCAT(CAST(price AS CHAR(10)),'x',CAST(amount AS CHAR(4)),'=')
AS '단가x 수량', price*amount AS '구매액' FROM buytbl;


SELECT 
	case 10
		when 1 then '일'
		when 2 then '이'
		when 10 then '십'
	END;
	
SELECT BIT_LENGTH('가나다'),
CHAR_LENGTH('가나다'),
LENGTH('가나다');


select INSTR('하나둘섹둘둘셋', '둘');
SELECT * FROM buytbl WHERE prodname LIKE '%터%';

SELECT INSERT('abcdefghi',3,4,'****'), 
INSERT('abcdefghi',3,2,'****');

SELECT REPLACE ('이것이 MariaDB다','이것이','This is');

SELECT SUBSTRING('대한민국만세',3,2);

SELECT first_name, SUBSTRING(hire_date,1,4) FROM employees; 

SELECT first_name, birth_date FROM employees 
where SUBSTRING(birth_date,6,2)='01';


SELECT DATE(NOW()), TIME(NOW());


CREATE TABLE board(
	num INTEGER AUTO_INCREMENT PRIMARY KEY,
	title varchar(255),
	reg_date DATETIME,
	update_date DATETIME
);

INSERT INTO board
(title, reg_date, update_date) VALUES ('첫번째 글', NOW(),NOW());

UPDATE board
SET
	title = '타이틀 수정',
	update_date = NOW()
WHERE num=1;


--오늘이 생일인 사원을 찾기 
SELECT first_name, birth_date FROM employees
WHERE substring(birth_date,6,5)=substring(DATE(NOW()),6,5);
