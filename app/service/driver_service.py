from flask import render_template, request, session, redirect, url_for
from flask_paginate import Pagination, get_page_args
from app.db import DB

def driver_view_service():
    SQL = "select 'danger','Moe', 'mary@example.com' from dual"
    conn = DB('dict')
    result = conn.select_all(SQL,None)
    return render_template('/driver/vehicle_information.html', result=result)


def driver_mytable_service():
    per_page = 5
    page = request.args.get('page', 1, type=int)
    user_oid = str(session['userInfo'][0].get('oid'))
    page, _, offset = get_page_args(per_page=per_page)
    dbcon = DB('dict')
    cur = dbcon.cur
    cur.execute("select count(0) as page FROM BOARD WHERE driverid = {0}".format(user_oid))
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
        WHERE driverid = {0} LIMIT {1} OFFSET {2}""".format(user_oid, per_page, offset)
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
        FROM BOARD WHERE driverid = {0} LIMIT {1} OFFSET {2}""".format(user_oid, per_page, (page-1)*per_page)
    conn = DB('dict')
    result = conn.select_all(SQL, None)
    print(SQL)
    return render_template('/driver/mytable.html1' ,boards=posts, pagination=Pagination(
            page=page,
            total=total,
            per_page=per_page,
            prev_label="<<",
            next_label=">>",
            format_total=True,
        ),
        search=True
                        )


def assignable_table_service():
    per_page = 5
    page = request.args.get('page', 1, type=int)
    user_oid = str(session['userInfo'][0].get('oid'))
    page, _, offset = get_page_args(per_page=per_page)
    dbcon = DB('dict')
    cur = dbcon.cur
    cur.execute("select count(0) as page FROM BOARD WHERE driverid is null")
    total = cur.fetchone().get('page')
    cur.execute(
        """SELECT 
        oid,
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
        WHERE driverid is null LIMIT {0} OFFSET {1}""".format(per_page, offset)
    )
    posts = cur.fetchall()
    cur.close()

    SQL = """SELECT 
        oid,
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
        FROM BOARD WHERE driverid is null LIMIT {0} OFFSET {1}""".format(per_page, (page-1)*per_page)
    conn = DB('dict')
    result = conn.select_all(SQL, None)
    print(SQL)
    return render_template('/driver/assignable.html' ,boards=posts, pagination=Pagination(
            page=page,
            total=total,
            per_page=per_page,
            prev_label="<<",
            next_label=">>",
            format_total=True,
        ),
        search=True
                        )


def driver_assign_service():
    user_oid = str(session['userInfo'][0].get('oid'))
    boardOID = request.form.get("boardOID")
    conn = DB('dict')
    SQL = "UPDATE board SET driverid = {0} where oid = {1}".format(user_oid, boardOID)
    conn.save_one(SQL, None)
    return redirect(url_for('driver_page.driver_mytable_service'))