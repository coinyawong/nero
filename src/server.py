from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "dd"

if __name__ == "__main__":
   app.run(host='192.168.0.136', port=8306)
