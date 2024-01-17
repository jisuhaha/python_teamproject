from flask import render_template, request,session
from app.db import DB


def cust_price_service():
    carinfo = request.args["carinfo"]
    start = request.args["start"][0:2]
    end = request.args["end"][0:2]
    SQL = "SELECT DISTANCE FROM DISTANCE_LOC WHERE STARTLOC = '{0}' and endloc = '{1}' ".format(start,end)
    conn = DB('dict')
    result = conn.select_all(SQL,None)
    result = str(result[0].get("DISTANCE"))+'원'
    return result


def cust_reg_service():
    if request.method=='POST':
        loadingdate = request.form.get("loadingdate")
        unloadingdate = request.form.get("unloadingdate")
        groupname = request.form.get("groupname")
        startpoint_name = request.form.get("startpointName")
        startpoint_address = request.form.get("startpointAddress")
        endpoint_name = request.form.get("endpointName")
        endpoint_address = request.form.get("endpointAddress")
        carinfo = request.form.get("carinfo")
        hidden_price = request.form.get("hiddenPrice")
        loading_start = "INSERT INTO LOADINGPOINT (NAME, ADDRESS) VALUES ('{0}','{1}')".format(startpoint_name, startpoint_address)
        print(loading_start)
        conn = DB('dict')
        start_id = conn.save_one_getid(loading_start,None)
        loading_end = "INSERT INTO LOADINGPOINT (NAME, ADDRESS) VALUES ('{0}','{1}')".format(endpoint_name, endpoint_address)
        print(loading_end)
        conn = DB('dict')
        end_id = conn.save_one_getid(loading_end,None)
        board_sql = '''insert into board(groupoid, groupname, loadingdate, unloadingdate, loadingoid, unloadingoid, weight_t ) values 
        ('{0}','{1}','{2}','{3}','{4}','{5}','{6}')'''.format(session['userInfo'][0].get('memberid'), groupname,loadingdate,unloadingdate, start_id, end_id,carinfo)
        conn = DB('dict')
        print(board_sql)
        groups = conn.save_one(board_sql,None)
        return render_template('/user/join.html',groups=groups)

    else:
        return render_template('/cust/register.html')

