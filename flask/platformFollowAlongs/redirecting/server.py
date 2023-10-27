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

#added
@app.route('/show')
def show_user():
      print('Showing the User Info From the Form')
      print(request.form)
      return render_template('show.html')

if __name__ == "__main__":
      app.run(debug=True, host="localhost", port=8000)