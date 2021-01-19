SELECT * FROM buytbl
	INNER JOIN usertbl
	ON buytbl.userID=usertbl.userID
ORDER BY buytbl.userid;


SELECT
userID , name, prodName , addr , CONCAT(mobile1, mobile2) AS '연락처'
FROM buyTBL
	INNER JOIN userTBL
	ON buyTBL.userID = userTBL.userID;
	
	
SELECT
distinct U.userID , U.name, U.addr FROM usertbl AS U
	INNER JOIN buytbl As B
	ON U.userID = B.userID;
	
	
-- M:N관계 예제

CREATE TABLE stdTBL(
	stdName VARCHAR(10) NOT NULL PRIMARY KEY,
	addr CHAR(4) NOT NULL
);

CREATE TABLE clubTBL(
	clubName VARCHAR(10) NOT NULL PRIMARY KEY,
	roomNo CHAR(4) NOT NULL
);

CREATE TABLE stdclubTBL(
	num INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
	stdName VARCHAR(10) NOT NULL,
	clubName VARCHAR(10) NOT NULL,
	FOREIGN KEY(stdName) REFERENCES stdTBL(STDName),
	FOREIGN KEY(clubName) REFERENCES clubTBL(clubName)
);

INSERT INTO stdTBL VALUES 
('김범수', '경남'), ('성시경', '서울'), ('조용필', '경기'),
('은지원', '경북'), ('바비킴', '서울');

INSERT INTO clubtbl VALUES
('수영', '101호'), ('바둑', '102호'), ('축구', '103호'),
('봉사', '104호');

INSERT INTO stdclubtbl VALUES
(NULL, '김범수', '바둑'), (NULL, '김범수', '축구'),
(NULL, '조용필', '축구'), (NULL, '은지원', '축구'),
(NULL, '은지원', '봉사'), (NULL, '바비킴', '봉사');

SELECT S.stdName, S.addr, C.clubName, C.roomNo FROM stdtbl S
	INNER JOIN stdclubtbl SC
		ON S.stdName = SC.stdName
	INNER JOIN clubtbl C
		ON SC.clubName = C.clubName
ORDER BY S.stdName;

SELECT U.userid, U.name, B.prodName, U.addr,
	CONCAT(U.mobile1, U.mobile2) AS '연락처'
FROM usertbl U
	right OUTER JOIN buytbl B
	ON u.userid=B.userid
ORDER BY USERid;


CREATE TABLE empTbl (emp CHAR(3), manager CHAR(3), empTel VARCHAR(8));

INSERT INTO emptbl VALUES
('나사장', NULL, '0000'),
('김재무','나사장','2222'),
('김부장','김재무','2222-1'),
('이부장','김재무','2222-2'),
('우대리','이부장','2222-2-1'),
('지사원','이부장','2222-2-2'),
('이영업','나사장','1111'),
('한과장','이영업','1111-1'),
('최정보','나사장','3333'),
('윤차장','최정보','3333-1'),
('이주임','윤차장','3333-1-1');

SELECT A.emp '부하직원', B.emp '직속상관', B.empTel '직속상관 연락처'
FROM emptbl A
	INNER JOIN emptbl B
		ON A.manager=B.emp
WHERE A.emp = '우대리';




