from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
      return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
      print('Got Post Info')
      print(request.form)
      ##### NEVER RENDER A TEMPLATE ON A POST REQUEST
      ## INSTEAD WE WE WILL REDIRECT TO OUR INDEX ROUTE
      return redirect('/')

if __name__ == "__main__":
      app.run(debug=True, host="localhost", port=8000)