CREATE VIEW v_userbuyTBL
AS
SELECT U.userid, U.name, B.prodName, U.addr,
	CONCAT(U.mobile1, U.mobile2) AS '연락처'
FROM usertbl U
	INNER JOIN buytbl B
	ON U.userID=B.userid;
	
SELECT * FROM v_userbuyTBL; 



ALTER VIEW v_userbuyTBL
AS 
	SELECT U.userid AS '아이디', U.name AS '이름',
			 B.prodName AS '제품이름', U.addr AS '주소',
			CONCAT(U.mobile1, U.mobile2) AS '연락처'
	FROM usertbl U
		INNER JOIN buytbl B
			ON U.userID=B.userid;
SELECT * FROM v_userbuyTBL;