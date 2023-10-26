from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
      return "Welcome to my Website!"

@app.route('/html')
def html():
      return render_template("index.html")

@app.route('/90s')
def nine():
      return render_template("90s.html")

@app.route('/<color>')
def color(color):
      return render_template("color.html", color=color)

@app.route('/names')
def names():
      instructor = "Kyle"
      names_from_server = ["colby", "mycal", "Jon", "judah", "sara"]
      return render_template("my_data.html", names_to_jinja=names_from_server)

@app.route('/word/<string>')
def word(string):
      return string

@app.route('/calc/<int:x>/<int:y>')
def calc(x,y):
      return render_template("calc.html", x=x, y=y)

@app.route('/coolstuff')
def cool():
      my_sting = "cool " + "stuff"
      return my_sting

app.run(debug=True, host="localhost", port=8000)
# app.run(debug=True, port=5001, host="0.0.0.0")  = LAN