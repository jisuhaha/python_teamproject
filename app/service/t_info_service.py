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
    return render_template('/t_info/t_info_detail.html') 