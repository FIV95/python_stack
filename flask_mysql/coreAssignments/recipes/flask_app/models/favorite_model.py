from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import recipe_model
from flask_app.models import user_model


class Favorite:
    def __init__(self, data):
        self.favorite_id = data['favorite_id']
        self.user_id = data['user_id']
        self.recipe_id = data['recipe_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_user_favorite_recipes(cls, user_id):
        data = {"user_id": user_id}

        query = """
        SELECT recipes.* FROM users
        JOIN favorites ON users.id = favorites.user_id
        JOIN recipes ON favorites.recipe_id = recipes.recipe_id
        WHERE users.id = %(user_id)s
        """

        results = connectToMySQL("recipes").query_db(query, data)

        user_favorite_recipes = []
        for recipe in results:
            new_recipe = Recipe(recipe.copy())  # this clones the dictionary
            user_favorite_recipes.append(new_recipe)

        return user_favorite_recipes


    @classmethod
    def get_users_who_favorited_recipe(cls, recipe_id):
        data = {"recipe_id": recipe_id}

        query = """
        SELECT users.* FROM recipes
        JOIN favorites ON recipes.recipe_id = favorites.recipe_id
        JOIN users ON favorites.user_id = users.id
        WHERE recipes.recipe_id = %(recipe_id)s
        """

        results = connectToMySQL("recipes").query_db(query, data)

        users_who_favorited_recipe = []
        for user in results:
            new_user = User(user.copy())  # this clones the dictionary
            users_who_favorited_recipe.append(new_user)

        return users_who_favorited_recipe

