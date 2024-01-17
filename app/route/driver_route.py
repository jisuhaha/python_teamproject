from flask import Blueprint, render_template
from app.service.driver_service import *

driver_page = Blueprint('driver_page', __name__, url_prefix='/driver')

driver_page.add_url_rule("/price", methods=['GET','POST'], view_func=driver_view_service)
driver_page.add_url_rule("/table", methods=['GET','POST'], view_func=driver_table_service)