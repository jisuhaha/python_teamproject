from flask import render_template, request,session
from app.db import DB
import hashlib
#from flask_jwt_extended import create_access_token, set_access_cookies, create_refresh_token

def user_main_service():
    return render_template('/user/main.html')

def user_login_service():
    if request.method=='GET':
        return render_template('/user/login.html')
    else :
        memberid = request.form.get("memberid")
        password = request.form.get("password")
        password = encrypt_pw(memberid,password)
        SQL = "SELECT * FROM XMEMBER where memberid = '{0}' and password = '{1}'".format(memberid,password)
        conn = DB('dict')
        result = conn.select_all(SQL,None)
        if len(result)==0:
            return render_template('/user/login.html')
        else:
            session['userInfo'] = result
            print(session['userInfo'][0])
            print(session['userInfo'][0].get('memberid'))
            return render_template('/user/main.html', user=result)

def user_join_service():
    if request.method=='GET':
        SQL = 'SELECT oid, groupname FROM XGROUP WHERE STATUS = \'a\''
        conn = DB('dict')
        groups = conn.select_all(SQL,None)
        return render_template('/user/join.html',groups=groups)
    else:
        memberid=request.form.get("memberid")
        password=request.form.get("password")
        password = encrypt_pw(memberid,password)
        telphone=request.form.get("telphone")
        groupid=request.form.get("groupid")
        name=request.form.get("name")
        carnum=request.form.get("carnum")
        carinfo=request.form.get("carinfo")
        status=request.form.get("status")
        SQL = '''INSERT INTO XMEMBER 
        (memberid, PASSWORD, telphone, groupid, NAME, carnum, carinfo, STATUS, groupname, createdate)
        VALUES('{0}','{1}','{2}',{3},'{4}','{5}','{6}','{7}', (select groupname from xgroup where oid={3}), now() )'''.format(memberid, password, telphone, groupid, name, carnum, carinfo, status)
        conn = DB('dict')
        groups = conn.save_one(SQL,None)
        return render_template('/user/join.html')

def user_profile_service():
    return render_template('/user/profile.html')

def user_manage_service():
    page = request.args.get('page', 1, type=int)
    per_page = 10

    PAGING_SQL = "select (count(0)/10) as max_page from xmember"
    conn = DB('dict')
    max_page = conn.select_one(PAGING_SQL)
    print(max_page)

    SQL = "SELECT * FROM XMEMBER LIMIT %s OFFSET %s"
    conn = DB('dict')
    result = conn.select_all(SQL,(per_page, (page-1)*per_page))
    return render_template('/user/manage.html' ,users=result)

def encrypt_pw(id, password):
    password = password+id
    password = hashlib.sha256(password.encode()).hexdigest()
    return password