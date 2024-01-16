from flask import render_template, request,session
from app.db import DB

def driver_view_service():
    SQL = "select 'danger','Moe', 'mary@example.com' from dual"
    conn = DB('dict')
    result = conn.select_all(SQL,None)
    return render_template('/driver/vehicle_information.html', result=result)