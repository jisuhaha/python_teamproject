from flask import Blueprint, render_template
from app.service.cust_service import *

cust_page = Blueprint('cust_page', __name__, url_prefix='/cust')

cust_page.add_url_rule("/price", methods=['GET','POST'], view_func=cust_price_service)
cust_page.add_url_rule("/reg", methods=['GET','POST'], view_func=cust_reg_service)
cust_page.add_url_rule("/table", methods=['GET','POST'], view_func=cust_table_service)