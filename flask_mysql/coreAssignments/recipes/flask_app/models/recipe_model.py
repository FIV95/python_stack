from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user_model import User
from flask import flash, session

class Recipe:
    def __init__(self, data):
        self.recipe_id = data['recipe_id']
        self.user_id = data['user_id']
        self.name = data['Name']
        self.description = data['DESCRIPTION']
        self.instructions = data['INSTRUCTIONS']
        self.cooking_time = data['cooking_time']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    def __str__(self):
        return f"Recipe {self.recipe_id}: {self.name}"


    @classmethod
    def create(cls, form):
        print('\n\n', )
        user_id = session.get('user_id')
        data = {
                'user_id': user_id,
                **form
                }

        print('\n\n ---- Line 48 Recipe Model--- data', data,'\n\n')
        query = """INSERT INTO recipes
        (user_id, Name, DESCRIPTION, INSTRUCTIONS, cooking_time)
        VALUES (%(user_id)s, %(name)s, %(description)s, %(instructions)s, %(cookingTime)s)"""

        id_of_created_entry = connectToMySQL('recipes').query_db(query, data)
        return id_of_created_entry

    @classmethod
    def recipe_creators(cls):
        query = """
        SELECT * FROM USERS LEFT JOIN recipes ON recipes.user_id = users.id
        """
        results = connectToMySQL('recipes').query_db(query)
        recipes = []
        print('\n\n\n ---- Line 46 recipe_model', results)


        for row in results:
            new_recipe = cls(row)

            data = {
                **row,
                "user_id" : row['user.id'],
                "created_at" : row['created_at'],
                "updated_at" : row['updated_at'],
            }

            new_user = User(data)
            new_recipe.user = new_user

            recipes.append(new_recipe)
        return recipes
    @staticmethod
    def validate(form):

        is_valid = True

        if 'name' not in form:
            flash ('Please enter a recipe Name', 'name_err')
            is_valid = False

        if 'description' not in form:
            flash ('Please enter a recipe description', 'description_err')
            is_valid = False

        if 'instructions' not in form:
            flash('Please enter recipe instructions', 'instruction_err')
            is_valid = False

        if 'cookingTime' not in form:
            flash('Please enter a recipe cooking time', 'cooking_time_err')
            is_valid = False

        if len(form['name']) < 2:
            flash('Min # of Chars: 2', 'name_length_err')
            is_valid = False

        if len(form['description']) < 3:
            flash('Min # of chars: 3', 'description_length_err')
            is_valid = False
        print('\n\n\n LINE 57 RECIPE MODEL VALIDATION IS RUNNING', is_valid)
        return is_valid

    @classmethod
    def recipe_creators(cls):
        query = """
        SELECT * FROM recipes LEFT JOIN USERS ON recipes.user_id = users.id
        """
        results = connectToMySQL('recipes').query_db(query)
        recipes = []
        print('\n\n\n ---- Line 46 user_model', results)


        for row in results:
            new_recipe = cls(row)


            data = {
                **row,
                "id" : row['id'],
                "created_at" : row['created_at'],
                "updated_at" : row['updated_at'],
            }

            new_user = User(data)
            new_recipe.user = new_user

            recipes.append(new_recipe)
        print('\n\n\n LINE 217', recipes,'\n')
        print(f"Contents of new_recipe: {new_recipe.__dict__}")
        return recipes

    @classmethod
    def edit_one(cls, form, recipe_id):
        data = {
            **form,
            "recipe_id" : recipe_id
        }
        print('\n\n-- LINE 125 recipe_model',recipe_id, '\n\n')
        query = """

        UPDATE recipes set
        Name = %(name)s,
        DESCRIPTION = %(description)s,
        INSTRUCTIONS = %(instructions)s,
        cooking_time = %(cookingTime)s
        WHERE recipe_id = %(recipe_id)s
        """
        connectToMySQL("recipes").query_db(query,data)

    @classmethod
    def select_one(cls, recipe_id):
        data = {"recipe_id": recipe_id}
        query = """

        SELECT * FROM recipes
        WHERE recipe_id = %(recipe_id)s

        """

        results = connectToMySQL('recipes').query_db(query,data)
        if results:
            new_recipe = cls(results[0])
            return new_recipe

    @classmethod
    def delete_one(cls, recipe_id):
        data = {"recipe_id": recipe_id}

        query = """
        DELETE from recipes WHERE recipe_id =
        %(recipe_id)s
        """

        connectToMySQL('recipes').query_db(query,data)

    @classmethod
    def one_by_user(cls, recipe_id):
        data = {"recipe_id": recipe_id}
        query = """
        SELECT * FROM recipes LEFT JOIN users ON recipes.user_id = users.id WHERE recipe_id = %(recipe_id)s """

        results = connectToMySQL('recipes').query_db(query, data)
        if results:

            print('\n\n--------> LINE 179 recipe_model.py results:',results,'\n\n')
            new_recipe = cls(results[0])

            user_data ={
             **results[0],
                "id" : results[0]['id'],
                "created_at" : results[0]['created_at'],
                "updated_at" : results[0]['updated_at']
                }
            print('\n\n--------> LINE 186 recipe_model.py results:',user_data,'\n\n')

            new_user = User(user_data)
            print('\n\n--------> LINE 188 recipe_model.py results:',new_user,'\n\n')
            new_recipe.user = new_user

            return new_recipe





