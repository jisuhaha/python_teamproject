from flask import Blueprint, render_template
from app.service.group_service import *

group_page = Blueprint('group_page', __name__, url_prefix='/group')


group_page.add_url_rule("/", methods=['GET','POST'], view_func=group_main_service)
group_page.add_url_rule("/detail", methods=['GET','POST'], view_func=group_detail)

