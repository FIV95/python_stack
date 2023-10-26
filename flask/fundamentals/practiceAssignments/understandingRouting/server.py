from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
      return 'Hello World'

@app.route('/dojo')
def dojo_response():
      return "Dojo!"

@app.route('/say/<string:name>')
def helloName(name):
      return f"Hello {name}"

@app.route('/repeat/<int:num>/<string:word>')
def repeater(num, word):
      return f"{word * num}"

@app.errorhandler(404)
def page_not_found(e):
      return "Sorry! No rresponse. Try again"

if __name__=="__main__": # Ensure this file is being run directly and not from a different omdule
      app.run(debug=True, host="localhost", port=8000)