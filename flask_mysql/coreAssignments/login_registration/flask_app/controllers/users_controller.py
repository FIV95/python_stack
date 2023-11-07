from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.user_model import User
from flask_app.models.post_model import Post

@app.route('/')
def main():
    form_data = session.get('form_data', {})  # Get the form data from the session
    return render_template('index.html', form_data=form_data)


@app.route('/register', methods=['POST', 'GET'])
def registration_attempt():
    form_data = request.form
    # print('\n\n\n ----------> form_data =\n', form_data, '\n\n\n')

    if not User.validate(request.form):
        session['form_data'] = form_data
        print('\n\n\n ----------> =\n', session, '\n\n\n')
        return redirect('/')
    else:
        session['form_data'] = form_data
        User.create(request.form)
        return redirect('/regsuccess')

@app.route('/regsuccess')
def registration_success():
    session.pop('form_data', None)
    return  render_template('regsuccess.html')

@app.route('/validate', methods=['POST'])
def login_attempt():
    l_email = request.form.get('l_email')
    print('\n\n\n results for l_email========', l_email)
    l_password = request.form.get('l_password')
    user = User.select_by_email(l_email)
    if user and User.login(l_email, l_password):
        session['user_id'] = user.id
        session.pop('form_data', None)
        return redirect(f'/dashboard/{user.id}')
    else:
        session.pop('user_id', None)
        return redirect('/')

@app.route ('/dashboard/<int:user_id>')
def dashboard(user_id):
    user_id = session.get('user_id')
    print('\n\n\n user_id ----------->', user_id, '\n\n\n')
    if not 'user_id' in session:
        return redirect('/')
    posts = Post.get_posts_with_authors()
    print('\n\n\n post-------->>', posts[0].user.first_name, '\n\n\n')
    return render_template('dashboard.html', posts=posts, user_id = user_id)

@app.route ('/logout')
def logout():

    session.pop('user_id', None)
    return redirect('/')

