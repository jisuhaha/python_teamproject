from flask import Blueprint, render_template
from app.service.user_service import *

user_page = Blueprint('user_page', __name__, url_prefix='/user')


user_page.add_url_rule("/", methods=['GET','POST'], view_func=user_login_service)
user_page.add_url_rule("/login", methods=['GET','POST'], view_func=user_login_service)
user_page.add_url_rule("/join", methods=['GET','POST'], view_func=user_join_service)
user_page.add_url_rule("/profile", methods=['GET','POST'], view_func=user_profile_service)

