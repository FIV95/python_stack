from flask import render_template, request, redirect, flash
from flask_app import app
from flask_app.models.surveyUser_model import SurveyUser

@app.route('/')
def main():
      return render_template ('index.html')

@app.route('/submit', methods=['post'])
def result():
      SurveyUser.create(request.form)
      return redirect('/resultsofsubmit')

@app.route('/resultsofsubmit')
def showresults():
      results = SurveyUser.get_one()
      print("\n\n\n get one results ------->", results.coolcheck)
      return render_template('results.html', results=results)