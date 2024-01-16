from flask import Flask, render_template, request, jsonify, session
from app.route.cust_route import cust_page
from app.route.board_route import board_page
from app.route.user_route import user_page
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'TeAmPrOJecTPy1'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)

app.register_blueprint(board_page)
app.register_blueprint(cust_page)
app.register_blueprint(user_page)

@app.route('/')
def home():
    return 'test001'

@app.route('/login')
def login():
    return render_template('login.html')
