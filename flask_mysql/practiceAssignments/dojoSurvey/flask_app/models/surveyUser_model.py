from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

# db = 'name'

class SurveyUser:
      def __init__(self, data):
            self.id = data['id']
            self.name = data['name']
            self.location = data['location']
            self.language_choice = data['language_choice']
            self.coolcheck = data['coolcheck']
            self.leetcheck = data['leetcheck']

      @staticmethod
      def validate_SurveyUser(SurveyUser):
            is_valid = True
            if len(SurveyUser['name']) < 3:
                  flash('Min # of Chars: 3, Max # of Chars: 255')
                  is_valid = False
            selected_location = SurveyUser.get('select_location')
            if not selected_location:
                  flash('Please select an option')
                  is_valid = False
            selected_language = SurveyUser.get('select_language')
            if not selected_location:
                  flash('Please select an option.')
                  is_valid = False

            return is_valid

      @classmethod
      def create(cls, form):
            coolcheck = form.get("coolcheck") == '1'
            leetcheck = "leetcheck" in form

            query = """
            INSERT INTO dojos
            (name, coolcheck, location, language_choice, leetcheck)
            VALUES
            (%(name)s, %(coolcheck)s, %(location)s, %(language_choice)s, %(leetcheck)s)
            """
            id_of_created_entry = connectToMySQL("dojo_survey").query_db(query, form)
            return id_of_created_entry

      @classmethod
      def get_all(cls):

            query = """
            SELECT * FROM dojos
            ORDER BY id DESC;
            """
            results = connectToMySQL('dojo_survey').query_db(query)
            print("\n\n\nresults ------->",results)
            all_dojos = []

            for row in results:
                  new_instance = cls(row)
                  all_dojos.append(new_instance)
            print("\n\n\nall dojos ------->",all_dojos)
            return all_dojos

      @classmethod
      def get_one(cls):

            # data = {"id": id}

            query = """

            SELECT * FROM dojos
            ORDER BY id DESC
            LIMIT 1
            """
            results = connectToMySQL('dojo_survey').query_db(query)
            print("\n\n\n getone classmethod results ------->",results)
            if results:
                  new_user = cls(results[0])
                  return new_user
            else:
                  return False