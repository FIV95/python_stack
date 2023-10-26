from flask import Flask, render_template          # Import Flask to allow us to create our app
app = Flask(__name__) # Create a new instance of the Flask class called app
@app.route('/')  # the @ decorator associates this route with the function immedietly following
def index():
      return render_template("index.html") #Return the string "hello world" as a response

@app.route('/success')
def success():
      return "Success"

@app.route('/hello/<string:banana>/<int:num>')
def hello(banana, num):
      return f"Hello {banana * num}"

if __name__=="__main__": # Ensure this file is being run directly and not from a different omdule
      app.run(debug=True, host="localhost", port=8000)

