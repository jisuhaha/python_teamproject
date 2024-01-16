from flask import render_template, request, jsonify, make_response,redirect, url_for
from app.db import DB
import hashlib
#from flask_jwt_extended import create_access_token, set_access_cookies, create_refresh_token


def group_main_service():
    # 아직 고객사 고르는 방법을 구현하지 않았기 때문에 고객사 id는 1로 적어둠.
    SQL = f'''SELECT
    b.oid as board_id, 
    l.name as departure_point,
    ul.name as arrival_point,
    b.loadingdate as departure_date,
    b.unloadingdate as arrival_date,
    from xGroup g
    inner join board b on g.oid = b.groupOID
    inner join loadingpoint l on b.loadingoid = l.oid
    inner join loadingpoint ul on b.unloadingoid = ul.oid;
    '''
    conn = DB('dict')
    result = conn.select_all(SQL,None)

    return render_template('/group/main.html', data = result)


def group_detail_service():
    # 아직 고객사 고르는 방법을 구현하지 않았기 때문에 고객사 id는 1로 적어둠.
    SQL = f'''SELECT
    b.oid as board_id, 
    l.name as departure_point,
    ul.name as arrival_point,
    b.loadingdate as departure_date,
    b.unloadingdate as arrival_date,
    c.defaultcost as default_cost,
    c.laborcost as labor_cost,
    c.loadingcost as loading_cost,
    c.staycost as stay_cost,
    c.othercost as other_cost,
    c.status as status
    from xGroup g
    inner join board b on g.oid = b.groupOID
    inner join loadingpoint l on b.loadingoid = l.oid
    inner join loadingpoint ul on b.unloadingoid = ul.oid
    inner join cost c on c.boardoid = b.oid; 
    '''
    if request.method == 'POST':
        select_switch = request.form['select_search']
        text_form = request.form['text_form'].strip()
        date_value = request.form['date_search']
        
        # 날짜값이 존재하지 않는 경우 : 텍스트 입력 or 아무 입력도 없음
        if date_value == '' and text_form == '':
            pass
        elif select_switch == 'start_date':
            SQL += f'''where b.loadingdate = "{date_value}"'''
        
        elif select_switch == 'finish_date':
            SQL += f'''where b.unloadingdate = "{date_value}"'''

        # # 현재 운전자 정보가 없음..
        # elif select_switch == 'driver_name':
        #     SQL += f'''and driver_name like "%{text_form}%"'''

 
    conn = DB('dict')
    result = conn.select_all(SQL,None)
    return render_template('/board/detail.html', data = result)


