from flask import Blueprint, render_template
from app.service.t_info_service import *

t_info_page = Blueprint('t_info_page', __name__, url_prefix='/t_info')


t_info_page.add_url_rule("/", methods=['GET','POST'], view_func=t_info_main_service)
t_info_page.add_url_rule("/detail", methods=['GET','POST'], view_func=t_info_detail_service)
