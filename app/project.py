from flask import Flask, render_template, request, jsonify, session
from app.route.cust_route import cust_page
from app.route.board_route import board_page
from app.route.user_route import user_page
from app.route.driver_route import driver_page
from app.route.t_info_route import t_info_page
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'TeAmPrOJecTPy1'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)

app.register_blueprint(board_page)
app.register_blueprint(cust_page)
app.register_blueprint(user_page)
app.register_blueprint(driver_page)
app.register_blueprint(t_info_page)

@app.route('/')
def home():
    return render_template('user/login.html')

@app.route('/login')
def login():
    return render_template('login.html')
