from flask import Flask, render_template, request, jsonify
from app.route.board_route import board_page
from app.route.user_route import user_page

app = Flask(__name__)

app.register_blueprint(board_page)
app.register_blueprint(user_page)

@app.route('/')
def home():
    return 'test001'

@app.route('/login')
def login():
    return render_template('login.html')
