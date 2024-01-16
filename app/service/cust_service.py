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
    if request.method=='POST':
        SQL = 'SELECT * FROM board WHERE STATUS = \'a\''
        conn = DB('dict')
        groups = conn.save_one(SQL,None)
        loadingdate = request.form.get["loadingdate"] 
        groupname = request.form.get["xGroup.groupname"]
        name = request.form.get["startpoint.name"]
        
        
        
        
        
        
        return render_template('/user/join.html',groups=groups)

    else:
        return render_template('/cust/register.html')

