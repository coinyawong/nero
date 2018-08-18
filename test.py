from flask import Flask, render_template, request
from flask.logging import create_logger
from flask_mysqldb import MySQL
from mysql.connector import connection

mysql = MySQL()
app = Flask(__name__)

@app.route('/')
@app.route('/insert')
def insert():
    return render_template('insert.html')

@app.route('/insert_result', methods=['POST'])
def get_insert_result() :
     cnx = connection.MySQLConnection(user='coinyawong2', password='1010893!', host='127.0.0.1', database='yawong')
     cursor = cnx.cursor()
     insert_db = ("INSERT INTO cycle" "(cycle, roll, total)"
                                   "VALUES (%s, %s, %s)")

     value1 = request.form['value1']
     value2 = request.form['value2']
     value3 = request.form['value3']

     data_db = (value1, value2, value3)
     cursor.execute(insert_db, data_db)
     cnx.commit()
     cnx.close()
     return render_template('insert_result.html', value1 = value1)

@app.route('/list')
def list():
     return render_template('list.html')

@app.errorhandler(400)
def internal_error(exception):
     app.logger.error(exception)
     return render_template('400.html'), 400

# @app.errorhandler(500)
# def internal_error(exception):
#      app.logger.error(exception)
#      return render_template('500.html'), 500
if __name__ == "__main__":
   app.run()

