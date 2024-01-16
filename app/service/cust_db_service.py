from flask import render_template, request,session
from app.db import DB
import hashlib

def user_register_service():
    if request.method=='GET':
        SQL = 'SELECT oid, groupname FROM XGROUP WHERE STATUS = \'a\''
        conn = DB('dict')
        groups = conn.select_all(SQL,None)
        return render_template('/user/join.html',groups=groups)
    