from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


def charge_card(card_number):
      print(f'charging {card_number} $200.00...')

@app.route('/welcome')
def main():
      return render_template("index.html")

@app.route('/welcome')
def welcome():
      return redirect('/welcome')

@app.route('/buy')
def buy():
      return render_template("form.html")


# this route returns the form
@app.route('/accept_form', methods=["POST"])
def accept():
      print(f"Name {request.form['user_name']} ")
      print(f"Qty: {request.form['qty']} ")
      print(f"Card: {request.form['user_card']} ")

      session['user_name'] = request.form['user_name']

      request_copy = {
            **request.form
      }

      print(request.form)
      ###

      ###
      charge_card(request.form['user_card'])
      return render_template("thanks.html", name=request.form['user_name'])



app.run(debug=True, host="localhost", port=8000)