from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
      return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
      print('Got Post Info')
      session['username'] = request.form['name']
      session['useremail'] = request.form['email']
      return redirect('/show')

@app.route('/show')
def show_user():
      return render_template('show.html', name_on_template=session['username'], email_on_template=session['useremail'])


# DISCLAIMER: Hidden Input Field Usage
@app.route('/process', methods=['POST'])
def process_form():
      which_form = request.form['which_form']

      # if which_form == 'register':
      # Handle the registration process
      # Retrieve form data like name, email, and password
      # Perform registration logic

      # elif which_form == 'login':
      # Handle the login process
      # Retrieve form data like email and password
      # Perform login logic

      return redirect('/')  # Redirect to the main page

if __name__ == "__main__":
      app.run(debug=True, host="localhost", port=8000)
