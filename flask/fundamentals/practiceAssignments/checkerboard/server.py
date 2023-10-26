from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def checkboardMain():
      x=8
      y=4
      return render_template('index.html', x=8, y=4)

@app.route('/4')
def checkboard8by4():
      x=8
      y=2
      return render_template("index.html", x=x, y=y)

@app.route('/<int:x>/<int:y>')
def checkboardByUser(x,y):
      y = (y // 2)
      return render_template("index.html", x=x, y=y)



app.run(debug=True, host="localhost", port=8000)

      # <!-- {% for i in range(0,y,2)%} -->

                        # {%for i in range(0,y)%}