
import pymysql
#from contextlib import closing
from flask import *

app = Flask(__name__)

def db_con(sql_sentence='select * from new_table;'):
    db = pymysql.connect(
        host = 'localhost',
        user = 'root',
        password = 'admin',
        db = 'testdb',
        charset = 'utf8',
        autocommit = True
    )

    cur = db.cursor(cursor=pymysql.cursors.DictCursor)
    cur.execute(sql_sentence)
    result = cur.fetchall()
    cur.close()
    db.close()
    
    return result

@app.route('/cust_info', methods=['GET', 'POST'])
def cust_info():
    if request.method == 'GET':
        return render_template('cust_info.html', cust=db_con())
    elif request.method == 'POST':
        select_switch = request.form['select_search']
        text_form = request.form['text_form'].strip()
        date_value = request.form['date_search']
        
        # 날짜값이 존재하지 않는 경우 : 텍스트 입력 or 아무 입력도 없음
        if date_value == '' and text_form == '':
            sql_sentence = 'select * from new_table;'
        
        elif select_switch == 'start_date':
            sql_sentence = f'''select * from new_table where start_date = 
                "{date_value}"'''
        
        elif select_switch == 'finish_date':
            sql_sentence = f'''select * 
            from new_table
            where finish_date = "{date_value}"'''

        elif select_switch == 'driver_name':
            sql_sentence = f'''select * from new_table where driver_name like 
            "%{text_form}%"'''

        else:
            sql_sentence = 'select * from new_table;'
        print("="*30)
        print()
        print(sql_sentence)
        print()
        print("="*30)

    return render_template('cust_info.html', cust=db_con(sql_sentence))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register_user')
def register_user():
    return render_template('register_form.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login_form.html')
    elif request.method == 'POST':
        # session['login_info'] = request.form['email']
        return redirect(url_for('profile'))


@app.route('/work_list/<int:work_id>')
def work_detail(work_id):
    sql_sentence = f'''select * from new_table where work_id = {work_id}'''
    return render_template('work_info.html', detail=db_con(sql_sentence))


@app.route('/button/<int:btn_id>')
def bt_test(btn_id):
    return render_template('bt_test_page.html', btn_id=btn_id)



if __name__ =='__main__':
    app.run(debug=True)