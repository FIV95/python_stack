from flask import render_template, request, redirect

from flask_app import app

from flask_app.models.dojo_model import Dojo
from flask_app.models.ninja_model import Ninja


@app.route('/ninjaregistration')
def ninjaform():
      dojos = Dojo.get_all()
      return render_template('ninjaregistration.html', dojos=dojos)

@app.route('/createninja', methods=["POST"])
def ninjacreation():
      dojos = Dojo.get_all()
      Ninja.create(request.form)
      return redirect('/')

@app.route('/dojocontents/<int:id>')
def dojoinfo(id):
      Ninja.get_all()
      return render_template('dojocontents.html', dojo=Dojo.get_one(id))






# @app.route('/takedojoinfo', methods=["POST"])
# def dojoformrequest():
#       Dojo.create(request.form)
#       return redirect('/')