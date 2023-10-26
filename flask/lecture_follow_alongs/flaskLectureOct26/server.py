from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
      return "Welcome to my website!"

@app.route('/word/<string>')
def word(string):
      return string

@app.route('/calc/<int:x>/<int:y>')
def calc(x,y):
      return f"{x+y}"

@app.route('/coolstuff')
def cool():
      my_sting = "cool " + "stuff"
      return my_sting

app.run(debug=True, host="localhost", port=8000)
# app.run(debug=True, port=5001, host="0.0.0.0")  = LAN