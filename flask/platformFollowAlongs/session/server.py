from flask import Flask, render_template, request, redirect, session ## ADDED SESSION
app = Flask(__name__)
app.secret_key ='keep it secret, keep it safe'

@app.route('/')
def index():
      return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
      print('Got Post Info')
      ## Here we added two properties to session to store the name and email
      session['username'] = request.form['name']
      session['useremail'] = request.form['email']
      ##### NEVER RENDER A TEMPLATE ON A POST REQUEST
      ## INSTEAD WE WE WILL REDIRECT TO OUR INDEX ROUTE
      return redirect('/show')

#added
@app.route('/show')
def show_user():
      ## now that we have added session we can use those variables on LINE 13 / LINE 14 in this function
      return render_template('show.html', name_on_template=session['username'], email_on_template=session['useremail'])
###################IF I DELETE THIS STUFF ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
## AFTER SUBMITTING IT STILL IS THERE!!! CUZ WERE ON THE SAME SESSION!!!!!

if __name__ == "__main__":
      app.run(debug=True, host="localhost", port=8000)