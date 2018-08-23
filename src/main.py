import pymysql.cursors

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("main.html")

@app.route('/list/<int:cycle>')
def list(cycle):

	conn = pymysql.connect(host='localhost', user='coinyawong2', password='10-10893', db='yawong', charset='utf8mb4')
	cur = conn.cursor()
	sql= 'select a.name name, a.address address, b.cycle cycle, b.balance balance, truncate(b.balance/(c.roll*10000)*100,3) as percent, truncate(b.balance/(c.roll*10000)*c.total*0.945,3) as reward from user a, user_info b, cycle c where a.address = b.address and b.cycle+7 <= %s and c.cycle = %s'

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
   app.run(host='192.168.0.136', port=8306, debug=True)
