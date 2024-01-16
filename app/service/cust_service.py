from flask import render_template, request,session
from app.db import DB


def cust_price_service():
    carinfo = request.args["carinfo"]
    start = request.args["start"][0:2]
    end = request.args["end"][0:2]
    SQL = "SELECT DISTANCE FROM DISTANCE_LOC WHERE STARTLOC = '{0}' and endloc = '{1}' ".format(start,end)
    conn = DB('dict')
    result = conn.select_all(SQL,None)
    print(result)
    print(result[0])
    print(result[0].get("DISTANCE"))
    return result[0].get("DISTANCE")
def cust_reg_service():
    print('111')
    return render_template('/cust/register.html')