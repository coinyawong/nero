import pymysql.cursors

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for

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

@app.route('/notice')
def notice():
     return render_template("notice.html")
     cur.close()
     conn.close()

@app.route('/admin', methods=['GET'])
def admin():
     opt = request.args.get('opt')
     chv = request.args.get('chv')
     conn = pymysql.connect(host='localhost', user='coinyawong2', password='10-10893', db='yawong', charset='utf8mb4')
     cur = conn.cursor()
     sql= 'select a.name, (select max(cycle) from cycle) cycle, sum(b.balance) balance, b.address from user a, user_info b where a.address = b.address and b.cycle+7 <= (select max(cycle) cycle from cycle) group by a.name, b.address'
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
     templateData = {'data' : result, 'chv' : chv}
     if chv != '1' :
	return redirect(url_for('index'))
     else :
        return render_template("admin.html",**templateData)
     conn.close()

@app.route('/admin_ck', methods=['GET'])
def admin_ck():
     md = request.args.get('type')
     pwe= request.args.get('pw')
     conn = pymysql.connect(host='localhost', user='coinyawong2', password='10-10893', db='yawong', charset='utf8mb4')
     cur = conn.cursor()
     sql= 'select count(*) cnt from admin where passwd=%s'
     cur.execute(sql, pwe)
     result= cur.fetchone()
     cur.close()
     conn.close()
     if md == 'a':
        return redirect(url_for('admin', chv = result))
     elif md == 'b':
	return redirect(url_for('reward', cycle='', chv = result))

@app.route('/payout', methods=['GET'])
def payout():
     cycle = request.args.get('cycle')
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
	if len(cycle) == 0:
	  cycle = 10
	conn = pymysql.connect(host='localhost', user='coinyawong2', password='10-10893', db='yawong', charset='utf8mb4')
	cur = conn.cursor()
	sql= 'select a.name name, a.address address, b.cycle cycle, b.balance balance, truncate(b.balance/(c.roll*10000)*100,3) as percent, truncate(b.balance/(c.roll*10000)*c.total*0.945,3) as reward, c.chk from user a, user_info b, cycle c where a.address = b.address and b.cycle+7 <= %s and c.cycle = %s and b.balance > 0 order by b.cycle'
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
	chv = request.args.get('chv')
        conn = pymysql.connect(host='localhost', user='coinyawong2', password='10-10893', db='yawong', charset='utf8mb4')
        cur = conn.cursor()
	if len(cycle) ==0:
	   sql= 'select cycle, roll, total, chk from cycle order by cycle'
	   cur.execute(sql)
	else:
	   sql='select cycle, roll, total, chk from cycle where cycle=%s'
           cur.execute(sql, cycle)
        result = cur.fetchall()
        templateData = {'data' : result, 'cycle' : cycle, 'chv': chv}
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
   app.run(host='', port=, debug=True)
