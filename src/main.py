import pymysql.cursors

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
     conn = pymysql.connect(host='localhost', user='coinyawong2', password='10-10893', db='yawong', charset='utf8mb4')
     cur = conn.cursor()
     sql= 'select cycle, roll, total from cycle where cycle = (select max(cycle) from cycle)'
     cur.execute(sql)
     result = cur.fetchall()
     templateData = {'data' : result}
     return render_template("main.html",**templateData)
     cur.close()
     conn.close()

@app.route('/admin')
def admin():
        conn = pymysql.connect(host='localhost', user='coinyawong2', password='10-10893', db='yawong', charset='utf8mb4')
        return render_template('admin.html')
        conn.close()

@app.route('/list', methods=['GET'])
def list():
	cycle = request.args.get('cycle')
	if len(cycle) == 0:
	  cycle = 10
	conn = pymysql.connect(host='localhost', user='coinyawong2', password='10-10893', db='yawong', charset='utf8mb4')
	cur = conn.cursor()
	sql= 'select a.name name, a.address address, b.cycle cycle, b.balance balance, truncate(b.balance/(c.roll*10000)*100,3) as percent, truncate(b.balance/(c.roll*10000)*c.total*0.945,3) as reward, c.chk from user a, user_info b, cycle c where a.address = b.address and b.cycle+7 <= %s and c.cycle = %s and b.balance > 0 order by b.cycle'
	cur.execute(sql, (cycle, cycle))
	result = cur.fetchall()
	templateData = {'data' : result, 'cycle' : cycle}
	return render_template('user.html',**templateData)
	cur.close()
	conn.close()

@app.route('/reward', methods=['GET'])
def reward():
	cycle = request.args.get('cycle')
        conn = pymysql.connect(host='localhost', user='coinyawong2', password='10-10893', db='yawong', charset='utf8mb4')
        cur = conn.cursor()
	if len(cycle) ==0:
	   sql= 'select cycle, roll, total, chk from cycle order by cycle'
	   cur.execute(sql)
	else:
	   sql='select cycle, roll, total, chk from cycle where cycle=%s'
           cur.execute(sql, cycle)
        result = cur.fetchall()
        templateData = {'data' : result, 'cycle' : cycle}
        return render_template('reward.html',**templateData)
        cur.close()
        conn.close()

@app.route('/user_reward', methods=['GET'])
def user_reward():
        id = request.args.get('id')
        conn = pymysql.connect(host='localhost', user='coinyawong2', password='10-10893', db='yawong', charset='utf8mb4')
        cur = conn.cursor()
        sql='select a.cycle, a.address, (select sum(balance) from user_info where address=a.address and cycle+7<=a.cycle) balance, a.reward from payout a where a.address=%s'
        cur.execute(sql, id)
        result = cur.fetchall()
	cur.close()
	cur2 = conn.cursor()
	sql2='select a.name, truncate(sum(b.reward),3) reward from user a, payout b where a.address = b.address and a.address = %s'
	cur2.execute(sql2, id)
	result2 = cur2.fetchall()
	cur2.close()
	if id == '-':
	  cur3 = conn.cursor()
	  sql3='select truncate(sum(fee),3) fee from fee'
	  cur3.execute(sql3)
	  result3 = cur3.fetchall()
          cur3.close()
	  templateData = {'data' : result, 'total' : result2, 'fee' : result3}
	else:
          templateData = {'data' : result, 'total' : result2}
        return render_template('user_reward.html',**templateData)
        conn.close()


if __name__ == "__main__":
   app.run(host='192.168.0.136', port=8306, debug=True)
