from flask import render_template, request, redirect, session, get_flashed_messages
from flask_app import app

from flask_app.models.recipe_model import Recipe
from flask_app.models.favorite_model import Favorite


##
## our nav bar will have|Home|Favorites|LoggedInAs|LogOut|
## this app will show the main page and the table of recipes
## |recipeName|Time2Cook|PostedBy|Actions->view,edit,delete
@app.route('/recipeworld/recipedashboard')
def recipemain():
    user_id = session.get('user_id')
    print('\n\n\n------------>user_id from session -- LINE 14 recipe_controller', user_id,'\n\n\n')
    print('\n\n\n------------>Session dictionary from session -- LINE 16 recipe_controller', session,'\n\n\n')
    if not 'user_id' in session:
        return redirect('/recipeworld/loginandregistration')
    else:
      recipes = Recipe.recipe_creators()
      print('\n\n\n LINE 21 Recipe Controller->recipe',recipes,'\n\n')
      return render_template('recipedashboard.html', recipes=recipes)

###### from here we have to setup multiple routes depending on what the user selects on this main page

##
## route will display that users favorite recipes
@app.route('/recipeworld/recipedashboard/<user_id>/favorites')
def user_favorites(user_id):
      print('\n\n\n------------>',user_id)
      return render_template('userfavorties.html')


##
## route takes user to create recipe page / this will serve our form to to recieve recipe information
@app.route('/recipeworld/newrecipe')
def newrecipe():
      # check if user is logged in via session [id]
      if not 'user_id' in session:
            return redirect ('/recipeworld/loginandregistration')
      else:
           return render_template('recipecreation.html')


## this route will process the recipe form
@app.route('/recipeworld/createrecipe', methods=['POST'])
def createrecipe():
      if not Recipe.validate(request.form):
            session['recipe_form_data'] = request.form
            print('\n\n\n---- LINE 47 VALIDATION FOR CREATE --- flash message',get_flashed_messages(), '\n\n')
            return redirect ('/recipeworld/newrecipe')
      Recipe.create(request.form)
      return redirect('/recipeworld/createrecipe/success')
      ## take in form data for recipe data
      ## validate data
      ## if not successful
      ## redirect to ('/recipeworld/newrecipe')
      ## if successful
      ## return redirect('/recipeworld/createrecipe/success')

##
## this will render a message simply saying creation successful and will create a button that can direct the user back to the dashboard
@app.route('/recipeworld/createrecipe/success')
def createsuccess():
      ## render template with the new button
      return render_template('recipecreatesuccess.html')


## this route will direct the user to a edit page depending on the recipe selected.
@app.route('/recipeworld/createrecipe/edit/<int:recipe_id>')
def editrecipe(recipe_id):
      print('\n\n----->LINE 72 - Recipes_controller.py - recipe_id', recipe_id, '\n\n')
      if not 'user_id' in session:
            return redirect ('/recipeworld/loginandregistration')
      else:
      ## check if user is logged in using session id
      ## if not redirect
      ##render exact same template as the create template
      ## this template will request the data of the selected id
      ## data will pre-populate form fields
            return render_template('updaterecipe.html', recipe=Recipe.select_one(recipe_id))

##
## this route will handle the edit requests
@app.route('/recipeworld/editrecipe/<int:recipe_id>', methods=['POST'])
def updatedrecipe(recipe_id):

      if not Recipe.validate(request.form):
            session['recipe_form_data'] = request.form
            return redirect ('/recipeworld/createrecipe/edit/<int:recipe_id>')
      Recipe.edit_one(request.form, recipe_id)
      return redirect('/recipeworld/updaterecipe/success')

      ## take in data from edit request
      ## validate data
      ## if not successful redirect to '/recipeworld/createrecipe/edit/<int:recipe_id' w/ errors
      ## if successful
      # return redirect ('/recipeworld/updaterecipe/success')

## this will render a message simply saying edit successful and will create a button that can direct the user back to the dashboard
@app.route('/recipeworld/updaterecipe/success')
def updatesuccees():
      # render template with the new button
      return render_template('updatesuccess.html')

@app.route('/dashboard/delete/recipe/<int:recipe_id>')
def deleterecipe(recipe_id):
      Recipe.delete_one(recipe_id)
      return redirect ('/recipeworld/recipedashboard')

@app.route('/recipeworld/createrecipe/view/<int:recipe_id>')
def viewrecipe(recipe_id):
      recipe=Recipe.one_by_user(recipe_id)
      print('\n\n\n ---------> LINE 114 recipe_controller RECIPE',recipe, '\n\n')
      return render_template('recipeview.html', recipe=recipe)

# @app.route('/test/<int:recipe_id>')
# def test(recipe_id):
#       Recipe.all_recipes_by_one_user_id(recipe_id)
#       return redirect('/recipeworld/recipedashboard')
##
## route will display selected recipe via id
## route will display Recipe Name and creator name as headers
## route will also display who has favorited that recipe
## route will display recipe description, time2cook, instructions,created_at
# @app.route('/recipeworld/viewrecipe/<int:recipe_id')
# def select(recipe_id):
#       return render_template('recipeview.html')
