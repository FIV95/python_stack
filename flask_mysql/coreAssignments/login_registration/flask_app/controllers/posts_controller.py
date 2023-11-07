from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.user_model import User
from flask_app.models.post_model import Post

# Route to process form submission for creating a new post
@app.route('/post', methods=['POST'])
def create_post():
    if 'user_id' not in session:
        return redirect('/')

    # Handle the form submission
    title = request.form['title']
    content = request.form['content']

    Post.create_post(title, content, session)
    return redirect(f'/dashboard/{session["user_id"]}')


## return redirect(f'/dashboard/{user.id}')