from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.user_model import User

@app.route('/')
def main():
      return render_template('index.html')

@app.route ('/register', methods=['POST', 'GET'])
def registrationattempt():
      form_data = request.form
      if not User.validate(request.form):
            return render_template('index.html', form_data=form_data)
      User.create(request.form)
      return redirect('/dashboard')

@app.route ('/dashboard')
def dashboard():
      return render_template('dashboard.html')