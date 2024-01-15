from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'test001'

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/call/<param>')
def get_echo(param):
    if request.method=='GET':
        return jsonify({'param':param})

@app.route('/call',methods=['POST'])
def post_call():
    req_json = request.get_json()
    print(type(req_json))
    print(req_json)
    return jsonify(req_json)

