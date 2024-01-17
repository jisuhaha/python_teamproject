from flask import render_template, request,session, redirect, url_for
from flask_paginate import Pagination, get_page_args
from app.db import DB
from datetime import datetime
import logs.loggings as logs



def cust_price_service():
    carinfo = request.args["carinfo"]
    start = request.args["start"][0:2]
    end = request.args["end"][0:2]
    SQL = "SELECT DISTANCE FROM DISTANCE_LOC WHERE LOADINGPOINT = '{0}' AND UNLOADINGPOINT = '{1}' ".format(start,end)
    conn = DB('dict')
    result = conn.select_all(SQL,None)
    result = str(result[0].get("DISTANCE"))
    return result


def cust_reg_service():
    if request.method=='POST':
        loadingtime = request.form.get("loadingtime")
        loadingtime_obj = datetime.strptime(loadingtime, '%Y-%m-%dT%H:%M')
        unloadingtime = request.form.get("unloadingtime")
        unloadingtime_obj = datetime.strptime(unloadingtime, '%Y-%m-%dT%H:%M')
        groupname = request.form.get("groupname")
        startpoint_name = request.form.get("startpointName")
        startpoint_address = request.form.get("startpointAddress")
        endpoint_name = request.form.get("endpointName")
        endpoint_address = request.form.get("endpointAddress")
        carinfo = request.form.get("carinfo")
        cost = request.form.get("cost")
        loading_start = "INSERT INTO LOADINGPOINT (NAME, ADDRESS) VALUES ('{0}','{1}')".format(startpoint_name, startpoint_address)
        conn = DB('dict')
        start_id = conn.save_one_getid(loading_start,None)
        loading_end = "INSERT INTO LOADINGPOINT (NAME, ADDRESS) VALUES ('{0}','{1}')".format(endpoint_name, endpoint_address)
        conn = DB('dict')
        end_id = conn.save_one_getid(loading_end,None)
        board_sql = '''insert into board(groupoid, groupname, loadingtime, unloadingtime, loadingoid, unloadingoid, weight_t, cost ) values 
        ('{0}','{1}',%s,%s,'{2}','{3}','{4}',{5})'''.format(session['userInfo'][0].get('oid'), groupname, start_id, end_id,carinfo, cost)
        conn = DB('dict')
        print(board_sql)
        groups = conn.save_one(board_sql,(loadingtime_obj,unloadingtime_obj))
        logs.logger.info(f'고객사 운송 정보가 입력되었습니다. - {groupname}')   
        return redirect(url_for('cust_page.cust_table_service'))
    else:
        return render_template('/cust/register.html')

def cust_table_service():
    per_page = 5
    page = request.args.get('page', 1, type=int)
    user_oid = str(session['userInfo'][0].get('oid'))
    page, _, offset = get_page_args(per_page=per_page)
    dbcon = DB('dict')
    cur = dbcon.cur
    cur.execute("select count(0) as page FROM BOARD WHERE groupOID = {0}".format(user_oid))
    total = cur.fetchone().get('page')
    cur.execute(
        """SELECT 
        groupname AS groupname,
        (SELECT loadingpoint.name FROM loadingpoint WHERE loadingpoint.oid = board.loadingoid)AS loadingname,  
        (SELECT loadingpoint.address FROM loadingpoint WHERE loadingpoint.oid = board.loadingoid)AS loadingaddress,  
        board.loadingtime,
        (SELECT loadingpoint.name FROM loadingpoint WHERE loadingpoint.oid = board.unloadingoid)AS unloadingname,  
        (SELECT loadingpoint.address FROM loadingpoint WHERE loadingpoint.oid = board.unloadingoid)AS unloadingaddress,  
        board.unloadingtime ,
        board.weight_t AS car,
        board.cost,
        ifnull((select xmember.name FROM xmember WHERE xmember.oid = board.driverid),'') as name,
        ifnull((select xmember.telphone FROM xmember WHERE xmember.oid = board.driverid),'') as telphone ,
        ifnull((select xmember.info FROM xmember WHERE xmember.oid = board.driverid),'') as info ,
        ifnull((select xmember.carinfo FROM xmember WHERE xmember.oid = board.driverid),'') as carinfo
        FROM BOARD
        WHERE GROUPOID = {0} LIMIT {1} OFFSET {2}""".format(user_oid, per_page, offset)
    )
    posts = cur.fetchall()
    cur.close()

    SQL = """SELECT 
        groupname AS groupname,
        (SELECT loadingpoint.name FROM loadingpoint WHERE loadingpoint.oid = board.loadingoid)AS loadingname,  
        (SELECT loadingpoint.address FROM loadingpoint WHERE loadingpoint.oid = board.loadingoid)AS loadingaddress,  
        board.loadingtime,
        (SELECT loadingpoint.name FROM loadingpoint WHERE loadingpoint.oid = board.unloadingoid)AS unloadingname,  
        (SELECT loadingpoint.address FROM loadingpoint WHERE loadingpoint.oid = board.unloadingoid)AS unloadingaddress,  
        board.unloadingtime ,
        board.weight_t AS car,
        board.cost,
        ifnull((select xmember.name FROM xmember WHERE xmember.oid = board.driverid),'') as name,
        ifnull((select xmember.telphone FROM xmember WHERE xmember.oid = board.driverid),'') as telphone ,
        ifnull((select xmember.info FROM xmember WHERE xmember.oid = board.driverid),'') as info ,
        ifnull((select xmember.carinfo FROM xmember WHERE xmember.oid = board.driverid),'') as carinfo
        FROM BOARD WHERE groupOID = {0} LIMIT {1} OFFSET {2}""".format(user_oid, per_page, (page-1)*per_page)
    conn = DB('dict')
    result = conn.select_all(SQL, None)
    print(SQL)
    return render_template('/cust/table.html' ,boards=posts, pagination=Pagination(
            page=page,
            total=total,
            per_page=per_page,
            prev_label="<<",
            next_label=">>",
            format_total=True,
        ),
        search=True
                        )