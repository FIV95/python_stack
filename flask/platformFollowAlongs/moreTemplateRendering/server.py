from flask import Flask, render_template          # Import Flask to allow us to create our app
app = Flask(__name__) # Create a new instance of the Flask class called app
@app.route('/')  # the @ decorator associates this route with the function immedietly following
def index():
      return render_template("index.html")

@app.route('/success')
def success():
      return "Success"

@app.route('/hello/<string:banana>/<int:num>')
def hello(banana, num):
      return render_template("hello.html", banana=banana, num=num)

@app.route('/lists')
def render_lists():
      # soon enough we'll get data from a database, but for now, we're hard coding data
      student_info = [
      {'name' : 'Michael', 'age' : 35},
      {'name' : 'John', 'age' : 30 },
      {'name' : 'Mark', 'age' : 25},
      {'name' : 'KB', 'age' : 27}
      ]
      return render_template("lists.html", random_numbers = [3,1,5], students = student_info)

if __name__=="__main__": # Ensure this file is being run   directly and not from a different omdule
      app.run(debug=True, host="localhost", port=8000)

