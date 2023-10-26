from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def index():
      x=3
      return render_template("index.html", x=x)

@app.route('/play/<int:x>')
def boxMultiply(x):
      return render_template("index.html", x=x)

@app.route('/play/<int:x>/<boxcolor>')
def boxCountWithColor(x,boxcolor):
      return render_template("index.html", x=x, boxcolor=boxcolor)



app.run(debug=True, host="localhost", port=8000)