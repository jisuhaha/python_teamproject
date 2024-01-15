/* 차량 출고 차고 time 담당자 금액  금액
등록 수정 삭제 조회
paging 10

고객사(loadingpoint관리, board 등록)
운송사관리자 (차량정보 관리, 운송사 기사님 등록관리)

member회원 기사 관리자
systemid oid		int	pk
memberid	id 	varchar16 
PW	pssword		varchar256
소속	groupName	varchar24
소속ID 	groupid		int	group .oid	FK
연락처	telphone		varchar13
이름	name 		varchar24
상태	status		varchar2
차번호	carnum		varchar(40)
차량톤수	carinfo		varchar(10)
등록일	createdate	date


group 업체
systemid	oid		int 	pk
업체명	groupname 	varchar(30)
상태	status		varchar2
등록일	createdate	date


board	게시물
systemid oid	int pk
업체ID	groupOID	int	group.oid
업체명	groupname	varchar(30) group.groupname 
상차일	loadingdate	date
하차일	unloadingdate	date
상차시간	loadingtime	date
상차지	loadingoid	int	loadingpoint.oid
하차지	unloadingoid	int	loadingpoint.oid
무게    weight_t      int   >> 톤당 1만원 
거리    distance_km    int  >>  10km 당 1만원




loadingpoint
systemid 	oid	int
지명	name	varchar(100)
주소	address	varchar(200) */




create database python_teamproject default character set utf8 collate utf8_general_ci;

create user 'board'@'%' identified by 'boardqwe!@#';
grant all privileges on python_teamproject.* TO 'board'@'%';

use python_teamproject;

DROP TABLE IF EXISTS xMember;
create table xMember(
    oid         INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    memberid    varchar(16),
    pssword		varchar(256),
    groupName	varchar(24),
    groupid		INT,
    telphone	varchar(13),
    name 		VARCHAR(10),
    status		VARCHAR(2),
    carnum		varchar(40),
    carinfo		varchar(10),
    createdate	date
)default character set utf8 collate utf8_general_ci;


DROP TABLE IF EXISTS xGroup;
create table xGroup(
	oid			INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	groupname 	varchar(30),
	status		VARCHAR(2),
	createdate	date
)default character set utf8 collate utf8_general_ci;

DROP TABLE IF EXISTS board;
create table board(
	oid				INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	groupOID			INT,
	groupname		varchar(30),
	loadingdate		DATE,
	unloadingdate	DATE,
	reservetime		DATE,
	loadingtime		DATE,
	loadingoid		INT,
	unloadingoid	int
)default character set utf8 collate utf8_general_ci;

DROP TABLE IF EXISTS cost;
create table cost(
    oid				INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    boardoid		INT,
    defaultcost	INT,
    laborcost		INT,
    loadingcost	INT,
    staycost		INT,
    othercost		INT,
    stuats VARCHAR(2)
)default character set utf8 collate utf8_general_ci;



DROP TABLE IF EXISTS loadingpoint;
CREATE TABLE loadingpoint(
	oid	INT,
	name	VARCHAR(100),
	address	varchar(200)
)default character set utf8 collate utf8_general_ci;
