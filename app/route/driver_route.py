from flask import Blueprint, render_template
from app.service.driver_service import *

driver_page = Blueprint('driver_page', __name__, url_prefix='/driver')

driver_page.add_url_rule("/price", methods=['GET','POST'], view_func=driver_view_service)
driver_page.add_url_rule("/mytable", methods=['GET','POST'], view_func=driver_mytable_service)
driver_page.add_url_rule("/assignable", methods=['GET','POST'], view_func=assignable_table_service)
driver_page.add_url_rule("/assign", methods=['GET','POST'], view_func=driver_assign_service)