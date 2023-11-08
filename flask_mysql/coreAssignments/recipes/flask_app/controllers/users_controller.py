from flask import render_template, request, redirect, session, get_flashed_messages, flash
from flask_app import app

from flask_app.models.user_model import User

##
## we need a home page / this wil be a welcome
@app.route('/recipeworld')
def welcome():
      return render_template('index.html')


##
## we need a serve route for our login and registration
## this page will have our login and registration form
@app.route('/recipeworld/loginandregistration')
def loginandregistration():
    if "form_data" not in session:
        print("NOTHING IN SESSION...")
        session['form_data'] = {
            "first_name" : "",
            "last_name" : "",
            "dob" : "",
            "email" : ""
        }
    print("\n\n\n LINE 28 IN USER CONTROLLER",session['form_data']['email'],"\n\n\n")
    return render_template('loginandregistration.html')


@app.route('/register', methods=['POST'])
def registration_attempt():
    if not User.validate(request.form):
        session['form_data'] = request.form
        print('\n\n\n --------> session',session, '\n\n')
        # print("\n\n\n getflashed message ------------->", get_flashed_messages())
        return redirect('/recipeworld/loginandregistration')
    else:
        User.create(request.form)
        return redirect('/regsuccess')


## this route will be taking that form data - IF registration...
@app.route('/validate', methods=['POST'])
def login_attempt():
    print('\n\n\n--------- LINE 57 USER_CONTROLLER: Session ',session, '\n\n')
    l_email = request.form.get('l_email')
    print('\n\n\n results for l_email========', l_email)
    l_password = request.form.get('l_password')
    user = User.select_id_by_email(l_email)
    if not user:
        session.pop('user_id', None)
        return redirect('/recipeworld/loginandregistration')
    if not User.login(l_email, l_password):
        session.pop('user_id', None)
        return redirect('/recipeworld/loginandregistration')

    else:
        session['user_id'] = User.select_id_by_email(l_email)
        session.pop('form_data', None)
        return redirect(f'/recipeworld/recipedashboard')


@app.route('/regsuccess')
def registration_success():
    session.pop('form_data', None)
    return  render_template('regsuccess.html')



@app.route ('/logout')
def logout():

    session.pop('user_id', None)
    session.clear()
    return redirect('/recipeworld/loginandregistration')



## check out the recipe controllers from here on out



