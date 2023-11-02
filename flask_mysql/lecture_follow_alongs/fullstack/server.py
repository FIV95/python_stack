from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# from mysqlconnection import connectToMySQL
from user_model import User


@app.route('/')
def index():

      users = User.get_all()
      # print(connectToMySQL('users8_db').query_db("SELECT * FROM users"))
      return render_template('index.html', users=users)

@app.route('/new')
def new_user():
      return render_template('user_form.html')

@app.route('/create_user', methods=["POST"])
def create_user():
      # print(request.form)
      User.create(request.form)
      return redirect('/')

@app.route('/edit/<int:id>', methods=["POST"])
def edit_user(id):
      return render_template("edit_form.html", user=User.get_one(id))

@app.route('/applyedit', methods=["POST"])
def apply_updates():
      User.update(request.form)
      return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
      User.deleteJob(id)
      # User.deleteAddress(id)
      # User.deleteUser(id)
      return redirect('/')


if __name__ == "__main__":
      app.run(debug=True, host="localhost", port=8000)