from flask import render_template, request,session
from app.db import DB


def cust_price_service():
    carinfo = request.args["carinfo"]
    start = request.args["start"]
    end = request.args["end"]
    return 'returned Server'
def cust_reg_service():
    print('111')
    return render_template('/cust/register.html')