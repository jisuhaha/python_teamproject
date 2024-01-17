from flask import render_template, request,session, redirect
from flask_paginate import Pagination, get_page_args
from app.db import DB
import hashlib, pymysql
#from flask_jwt_extended import create_access_token, set_access_cookies, create_refresh_token


def t_info_main_service():
    SQL = '''
    SELECT
    b.groupOID as group_id,
    b.groupname as group_name,
    b.loadingtime as departure_time,
    b.unloadingtime as arrival_time,
    b.loadingoid as departure_code,
    b.unloadingoid as arrival_code,
    b.weight_t as weight_info,
    m.telphone as driver_tel,
    m.name as driver_name,
    m.info as driver_car_num
    FROM board b
    INNER JOIN xmember m on b.driverid = m.memberid;   
    '''
    conn = DB('dict')
    result = conn.select_all(SQL,None)
    return render_template('/t_info/t_info_main.html', data=result)


def t_info_detail_service():
    SQL = '''
    SELECT
    b.groupOID as group_id,
    b.groupname as group_name,
    b.loadingtime as departure_time,
    b.unloadingtime as arrival_time,
    b.loadingoid as departure_code,
    b.unloadingoid as arrival_code,
    b.weight_t as weight_info,
    m.telphone as driver_tel,
    m.name as driver_name,
    m.info as driver_car_num
    FROM board b
    INNER JOIN xmember m on b.driverid = m.memberid
       
    '''
    if request.method == 'POST':
        # select_search = 검색창 위에 선택지
        select_search = request.form['select_option']  
        # 출발 혹은 도착 날짜/시간 검색할 때. 그 외에는 ''
        search_datetime = request.form['search_datetime']
        # 날짜/시간 정보 이외를 검색할 때. 그 외에는 ''
        search_text = request.form['search_text'].strip()
        
        # 아무것도 안 넣고 검색 버튼 눌렀을 때
        if search_datetime == '' and search_text == '':
            pass
        else:
            match select_search:
                case "dep_datetime":
                    # 입력한 시간과 같거나 나중 시간의 정보
                    SQL += f''' where
                    b.loadingtime >= "{search_datetime}"; '''
                case "arr_datetime":
                    SQL += f''' where
                    b.unloadingtime >= "{search_datetime}"; '''
                case "driver_name":
                    SQL += f''' where m.name like "%{search_text}%" '''
                case "dep_code":
                    SQL += f''' where b.loadingoid = {search_text} '''
                case "arr_code":
                    SQL += f''' where b.unloadingoid = {search_text} '''
                case "weight_info":
                    SQL += f''' where b.weight_t = "{search_text}" '''
                case "driver_car_num":
                    SQL += f''' where m.info = "{search_text}" '''
                case "driver_tel":
                    SQL += f''' where m.telphone = "{search_text}" '''
        
    conn = DB('dict')
    result = conn.select_all(SQL,None)
    return render_template('/t_info/t_info_detail.html', data = result) 