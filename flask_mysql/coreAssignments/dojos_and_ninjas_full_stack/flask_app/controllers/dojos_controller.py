from flask import render_template, request, redirect

from flask_app import app

from flask_app.models.dojo_model import Dojo

@app.route('/')
def index():
      dojos = Dojo.get_all()
      return render_template ('index.html', dojos=dojos, dojo_id = Dojo.get_one(id))

@app.route('/newdojo')
def newdojo():
      return render_template('dojocreate.html')

@app.route('/takedojoinfo', methods=["POST"])
def dojoformrequest():
      Dojo.create(request.form)
      return redirect('/')