import pymysql.cursors

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/list/<int:cycle>')
def list(cycle):

	conn = pymysql.connect(host='127.0.0.1', user='coinyawong2', password='1010893!', db='yawong', charset='utf8mb4')
	cur = conn.cursor()
	sql= 'select a.id, a.name, a.i_address, a.cycle, a.balance, truncate(a.balance/(b.roll*10000)*100,3) as percent, truncate(a.balance/(b.roll*10000)*b.total*0.945,3) as reward from user a, cycle b where a.cycle+7 <= %s and b.cycle = %s'

	if(cycle<10):
	  cur.execute(sql, (10, 10))
	else:
	  cur.execute(sql, (cycle, cycle))
	result = cur.fetchall()
	templateData = {'data' : result}
	return render_template('user.html',**templateData)
	cur.close()
	conn.close()

if __name__ == "__main__":
   app.run(host='192.168.0.100', debug=True)
