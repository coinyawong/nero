from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "야웅 베이킹"

if __name__ == "__main__":
   app.run()
