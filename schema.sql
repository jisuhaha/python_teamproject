create database python_teamproject default character set utf8 collate utf8_general_ci;

create user 'board'@'%' identified by 'boardqwe!@#';
grant all privileges on python_teamproject.* TO 'board'@'%';

use python_teamproject;


DROP TABLE IF EXISTS xMember;
create table xMember(
    oid         INT      NOT NULL AUTO_INCREMENT PRIMARY KEY,
    memberid    varchar(16),
    password		varchar(256),
    telphone	varchar(13),
    name 		VARCHAR(10),
    grade		VARCHAR(2),
    info		varchar(40),
    carinfo		varchar(10)
)default character set utf8 collate utf8_general_ci;


DROP TABLE IF EXISTS loadingpoint;
CREATE TABLE loadingpoint(
	oid	INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name	VARCHAR(100),
	address	varchar(200)
)default character set utf8 collate utf8_general_ci;


DROP TABLE IF EXISTS board;
create table board(
	oid				INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	groupOID			INT,
	groupname		varchar(30),
	loadingtime		DATETIME,
	unloadingtime	DATETIME,
	loadingoid		INT,
	unloadingoid	INT,
    weight_t        int,
    cost            int,
    driverid        varchar(10),   
    FOREIGN KEY(loadingoid) REFERENCES loadingpoint(oid),
    FOREIGN KEY(unloadingoid) REFERENCES loadingpoint(oid)
)default character set utf8 collate utf8_general_ci;


DROP TABLE IF EXISTS distance_loc;
create table distance_loc(
    loadingpoint     varchar(10),
    unloadingpoint   varchar(10),
    distance      int    
)default character set utf8 collate utf8_general_ci;

