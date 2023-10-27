from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def main():
      if not 'count' in session:
            session['count'] = 0
      session['count'] +=1
      return render_template('index.html')

@app.route('/countIncrease')
def countIncrease():
      session['count'] += 1
      return redirect('/')

@app.route('/countReset')
def countReset():
      session['count'] = 0
      return redirect('/')

@app.route('/submit', methods=["post"])
def countRequest():
      session['count'] = int(request.form['user_text'])
      return redirect('/')
# Hey we need to convert the usertext to a str???/

if __name__ == "__main__":
      app.run(debug=True, host="localhost", port=8000)