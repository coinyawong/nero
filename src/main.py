#-*- coding:utf-8 -*-
import pymysql.cursors

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for, session, abort, flash

import os

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html', msg="page not found"), 404

@app.errorhandler(500)
def page_server_error(error):
    return render_template('error.html', msg="error"), 500

@app.errorhandler(400)
def page_bad_request(error):
    return render_template('error.html', msg="bad request"), 400

@app.route('/')
def index():
     session['admin'] = False
     conn = pymysql.connect(host='localhost', user='coinyawong2', password='10-10893', db='yawong', charset='utf8mb4')
     cur = conn.cursor()
     sql= 'select cycle, roll, total from cycle where cycle = (select max(cycle)-5 from cycle)'
     cur.execute(sql)
     result = cur.fetchall()
     templateData = {'data' : result}
     return render_template("main.html",**templateData)
     cur.close()
     conn.close()

@app.route('/notice')
def notice():
     return render_template("notice.html")
     cur.close()
     conn.close()

@app.route('/admin', methods=['GET']) # 계정정보 부분이라 post로 변경
def admin():
     if not session.get('admin'):
        return redirect(url_for('index'))
     else:
        opt = request.args.get('opt')
        conn = pymysql.connect(host='localhost', user='coinyawong2', password='10-10893', db='yawong', charset='utf8mb4')
        cur = conn.cursor()
        sql= 'select a.name, (select max(cycle) from cycle) cycle, concat(format(sum(b.balance), 0), "ꜩ") balance, b.address from user a, user_info b where a.address = b.address and b.cycle+7 <= (select max(cycle) cycle from cycle) group by a.name, b.address'
        cur.execute(sql)
        result = cur.fetchall()
        cur2 = conn.cursor()
        if opt == 'a':
          sql2= 'insert into cycle values(%s, %s, %s, "X")'
          n1 = request.args.get('cycle')
          n3 = request.args.get('reward')
          n2 = request.args.get('roll')
          cur2.execute(sql2, (n1, n2, n3))
	  cur2.close()
          conn.commit()
        elif opt == 'b':
          sql2= 'update cycle set roll=%s, total=%s where cycle = %s'
          n3 = request.args.get('cycle')
          n2 = request.args.get('reward')
          n1 = request.args.get('roll')
          cur2.execute(sql2, (n1, n2, n3))
	  cur2.close()
          conn.commit()
        elif opt == 'c':
          sql2= 'insert into user_info values(%s, %s, %s, sysdate())'
          n1 = request.args.get('address')
          n2 = request.args.get('cycle')
          n3 = request.args.get('bal')
          cur2.execute(sql2, (n1, n2, n3))
	  cur2.close()
          conn.commit()
        elif opt == 'd':
          sql2= 'insert into user_info values(%s, %s, %s, sysdate())'
	  sql3 = 'insert into user values(%s, %s)'
          n1 = request.args.get('address')
          n2 = request.args.get('cycle')
          n3 = request.args.get('bal')
          n4 = request.args.get('name')
          cur2.execute(sql2, (n1, n2, n3))
          cur2.close()
	  cur3= conn.cursor()
	  cur3.execute(sql3, (n4, n1))
	  cur3.close()
          conn.commit()
        templateData = {'data' : result}
        return render_template("admin.html",**templateData)
        conn.close()

@app.route('/admin_ck', methods=['POST'])
def admin_ck():
     md = request.form['opt']
     pwe= request.form['pw']
     conn = pymysql.connect(host='localhost', user='coinyawong2', password='10-10893', db='yawong', charset='utf8mb4')
     cur = conn.cursor()
     sql= 'select count(*) cnt from admin where passwd=%s'
     cur.execute(sql, pwe)
     result= cur.fetchone()
     cur.close()
     conn.close()
     cnt = result[0]
     if cnt < 1:
       return redirect(url_for('index'))
     else:
       session['admin'] = True
       if md == 'a':
         return redirect(url_for('admin'))
       elif md == 'b':
	 return redirect(url_for('reward', cycle=''))

@app.route('/payout', methods=['POST'])
def payout():
     cycle = request.form['cycle']
     conn = pymysql.connect(host='localhost', user='coinyawong2', password='10-10893', db='yawong', charset='utf8mb4')
     cur = conn.cursor()
     sql= 'insert into payout select a.address address, c.cycle cycle, sum(truncate(b.balance/(c.roll*10000)*c.total*0.945,3)) as reward, sysdate() from user a, user_info b, cycle c where a.address = b.address and b.cycle+7 <= %s and c.cycle = %s and b.balance > 0 group by a.address, c.cycle'
     sql2='update cycle set chk = "O" where cycle=%s'
     cur.execute(sql, (cycle, cycle))
     cur.close()
     cur2 = conn.cursor()
     cur2.execute(sql2, cycle)
     cur2.close()
     conn.commit()
     conn.close()
     return redirect(url_for('reward', cycle = cycle))


@app.route('/list', methods=['GET'])
def list():
	cycle = request.args.get('cycle')
	conn = pymysql.connect(host='localhost', user='coinyawong2', password='10-10893', db='yawong', charset='utf8mb4')
        cur = conn.cursor()
	if len(cycle) == 0:
	  sql3 = 'select max(cycle)-5 cycle from cycle'
	  cur3 = conn.cursor()
	  cur3.execute(sql3)
          result3 = cur3.fetchone()
          cycle = result3[0]
          cur3.close()
	sql= 'select a.name, a.address, b.cycle, concat(format(b.balance, 0), "ꜩ") balance, format(b.balance/(c.roll*10000)*100, 1) percent, concat(format(b.balance/(c.roll*10000)*c.total*0.945, 3), "ꜩ") reward, c.chk from user a, user_info b, cycle c where a.address = b.address and b.cycle+7 <= %s and c.cycle = %s and b.balance > 0 order by b.cycle'
	cur.execute(sql, (cycle, cycle))
	result = cur.fetchall()
	cur.close()
	cur2 = conn.cursor()
	sql2= 'select cycle from cycle'
	cur2.execute(sql2)
	result2 = cur2.fetchall()
	cur2.close()
	templateData = {'data' : result, 'cycle' : cycle, 'data2' : result2}
	return render_template('user.html',**templateData)
	conn.close()

@app.route('/reward', methods=['GET'])
def reward():
	cycle = request.args.get('cycle')
        conn = pymysql.connect(host='localhost', user='coinyawong2', password='10-10893', db='yawong', charset='utf8mb4')
        cur = conn.cursor()
	if len(cycle) ==0:
	   sql= 'select cycle, roll, concat(truncate(total/roll, 3), "ꜩ") r_reward, concat(total, "ꜩ") total, chk from cycle order by cycle'
	   cur.execute(sql)
	else:
	   sql='select cycle, roll, concat(truncate(total/roll, 3), "ꜩ") r_reward, concat(total, "ꜩ") total, chk from cycle where cycle=%s'
           cur.execute(sql, cycle)
        result = cur.fetchall()
	cur2 = conn.cursor()
	sql2 = 'select sum(total) a from cycle group by chk'
	cur2.execute(sql2)
	result2 = cur2.fetchall()
        templateData = {'data' : result, 'cycle' : cycle, 'data2' : result2}
        return render_template('reward.html',**templateData)
        cur.close()
        conn.close()

@app.route('/user_reward', methods=['GET'])
def user_reward():
        id = request.args.get('id')
        conn = pymysql.connect(host='localhost', user='coinyawong2', password='10-10893', db='yawong', charset='utf8mb4')
        cur = conn.cursor()
        sql='select a.cycle, a.address, concat((select format(sum(balance), 0) from user_info where address=a.address and cycle+7<=a.cycle), "ꜩ") balance, concat(a.reward, "ꜩ") from payout a where a.address=%s'
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
	  sql3='select truncate(sum(total)*0.055, 3) fee from cycle where chk="O"'
	  cur3.execute(sql3)
	  result3 = cur3.fetchall()
          cur3.close()
	  templateData = {'data' : result, 'total' : result2, 'fee' : result3}
	else:
          templateData = {'data' : result, 'total' : result2}
        return render_template('user_reward.html',**templateData)
        conn.close()


if __name__ == "__main__":
   app.secret_key = os.urandom(12)
   app.run(host='192.168.0.136', port=8306, debug=True)
