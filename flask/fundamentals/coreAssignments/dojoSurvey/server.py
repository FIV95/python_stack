from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'solidus'

@app.route('/', methods=['get'])
def main():
      return render_template ('index.html')



@app.route('/submit', methods=['post'])
def result():
      session['username'] = request.form['username']
      session['location'] = request.form['location_input']
      session['language'] = request.form['language_input']
      session['coolchecker'] = request.form['coolchecker']
      session['leetness'] = request.form['leetness']
      leetness = session['leetness']
      coolness = session['coolchecker']
      name = session['username']
      location = session['location']
      language = session['language']
      return render_template('/results.html', name=name, location=location, language=language, coolness=coolness, leetness=leetness)

if __name__ == "__main__":
      app.run(debug=True, host="localhost", port=8000)


