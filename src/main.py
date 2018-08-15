import pymysql.cursors

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return "야웅 베이킹에 오신 것을 환영합니다."

@app.route('/select')
def select():
	conn = pymysql.connect(host='127.0.0.1', user='coinyawong2', password='1010893!', db='yawong', charset='utf8mb4')
	cur = conn.cursor()
	sql= 'SELECT id, name, i_address, cycle, balance FROM user'
	cur.execute(sql)
	result = cur.fetchall()
	templateData = {'data' : result}
	return render_template('user.html',**templateData)
	cur.close()
	conn.close()

if __name__ == "__main__":
   app.run()
