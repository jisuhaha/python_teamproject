<기사>
1. 운송정보조회 : 고객사 운송정보와 동일하게 만들되 radio 형태로 선택할수 있도록 한다.
    선택된 정보는 기사/고객사 운송정보조회 페이지에 최신화 된다.


<고객사>
1. 운송정보등록 : board 테이블에 원하는 운송 요청을 입력
    - 고객사ID, 고객사명, 상차시간, 하차시간, 상차지, 하차지, 요청챠랑
2. 운송정보수정 : 입력했던 것들을 수정 가능하도록 해야한다
3. 운송정보조회 : 운송정보가 입력되고, 기사가 배정된다면 추가적인 정보가 필요함(고객사 id 제외)
    - 기사연락처, 기사이름, 차량번호(미지정시 공란)
    - 기사 지정이 되면 xmember에서 해당 기사의 name, info, telphone 출력

<관리자>
1. 회원정보 페이지 -- 리스트형식으로 보이게
    - memberid, 이름, 연락처, 등급, 차량번호/고객사주소, 차량정보
2. 운송정보 페이지 -- 고객사 운송정보조회랑 동일
    - 고객사명, 상차시간, 하차시간, 상차지, 하차지, 요청차량,
      기사이름, 차량번호, 연락처

=====================================테이블 관리============================================
<Xmember>  -- 회원가입시 입력되는 정보가 저장되는 DB
systemid    oid		    int	pk              // index용
memberid	id  	    varchar16           // 사용자 아이디
PW	        password	varchar256
연락처	    telphone	varchar13
이름	    name 		varchar24           // 기사이름 또는 고객사명
등급	    grade		varchar2            // 00 : 관리자 , 10 : 기사, 20 : 고객사
차량번호 or 
고객사주소	info		varchar(40)         // 기사면 차량번호, 고객사면 상차지 지명 입력
차량정보	carinfo		varchar(10)         // 차량의 적재 t수를 입력(int type)


<board>  -- 고객사가 운송 요청시 입력된 정보가 저장되는 DB
systemid        oid	            int pk              // index용
고객사ID	    groupOID	    int	                // Xmember.memberid
고객사명	    groupname	    varchar(30)         // Xmember.name
상차시간	    loadingtime	    date    
하차시간	    unloadingtime	date
상차지	        loadingoid	    int	                // loadingpoint.oid
하차지	        unloadingoid	int	                // loadingpoint.oid
요청차량        weight_t        int                 // 운송해야하는 화물의 무게(단위:t)
운임            cost            int,
배정기사        driverid        varchar(10)


<distance_loc>    -- 운송거리 정보에 관한 내용이 저장되는 DB
상차지          loadingpoint    varchar(10)
하차지          unloadingpoint  varchar(10)
운송거리        distance        int
// 운송거리 값을 기준으로 10km 당 1만원으로 책정
 {운송거리계산}
    서울 -> 인천(20km), 대전(150km), 울산(300km) ,대구(250km), 광주(350km), 부산(400km)
    인천 -> 서울(20km), 대전(200km), 울산(400km) ,대구(300km), 광주(250km), 부산(450km)
    대전 -> 서울(150km), 인천(200km), 울산(250km) ,대구(200km), 광주(250km), 부산(300km)
    울산 -> 서울(300km), 인천(400km), 대전(250km), 대구(150km), 광주(200km), 부산(100km)
    광주 -> 서울(350km) 인천(250km), 대전(250km), 울산(200km), 대구(150km), 부산(300km)
    대구 -> 서울(250km), 인천(300km), 대전(200km), 울산(150km), 광주(150km), 부산(100km)
    부산 -> 서울(400km), 인천(450km), 대전(300km), 울산(100km) ,대구(100km), 광주(300km)


<loadingpoint> -- 상, 하차지의 정보를 임의로 넣어둠 각 도시별 2개씩
systemid 	oid	        int
지명	    name	    varchar(100)        // 서울등 7개 도시
주소	    address	    varchar(200)        // 주소는 임의로 2개씩 넣어두었음.






========================================주 요 변 경 사 항=====================================
1. xgroup 테이블 삭제 -> xmember 테이블에 해당 내용을 포함하여 작성
2. cost 테이블 삭제 -> distance_loc 테이블에 운송거리 계산표를 통하여 운송거리를 작성하고
    board에 있는 요청차량의 t수에 따라 운임 계산
3. xmember 에서 groupName, groupid, email, createdate 은 삭제, 
   status -> grade로 carnum -> info로 변경, 외래키 삭제(groupid)
4. board 테이블에서 reservetime, loadingdate 삭제, unloadingdate -> unloadintdate, 변경
    weight_t 추가