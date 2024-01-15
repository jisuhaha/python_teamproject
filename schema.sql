차량 출고 차고 time 담당자 금액  금액
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
예약시간	reservetime	date
상차시간	loadingtime	date
상차지	loadingoid	int	loadingpoint.oid
하차지	unloadingoid	int	loadingpoint.oid

cost
systemid	oid	int	pk
board참조 boardoid	int 
기본비용 defaultcost	int
수작업비	laborcost		int
전일상차	loadingcost	int
대기비	staycost		int
기타비용	othercost		int
상태 (지급 or 청구)	stuats varchar2

loadingpoint
systemid 	oid	int
지명	name	varchar(100)
주소	address	varchar(200)