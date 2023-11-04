from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
      def __init__(self, data):
            self.id = data['id']
            self.name = data['name']
            self.fighting_speciality = data['fighting_speciality']
            self.founded = data['created_at']

      @classmethod
      def get_all(cls):

            query = """
            SELECT * FROM dojos;
            """
            results = connectToMySQL('dojos_and_ninjas').query_db(query)
            all_dojos = []

            for dojo in results:
                  new_instance = cls(dojo)
                  all_dojos.append(new_instance)
            return all_dojos

      @classmethod
      def get_one(cls, id):

            data = {"id": id}

            query = """
            SELECT * FROM dojos
            WHERE id = %(id)s
            """

            results = connectToMySQL("dojos_and_ninjas").query_db(query, data)
            if results:
                  new_user = cls(results[0])
                  return new_user
            else:
                  return False

      @classmethod
      def updateName(cls, form):

            query = """
            UPDATE dojos set
            SET name %(name)s
            WHERE id = %(id)s
            """
            connectToMySQL("dojos_and_ninjas").query_db(query)

      @classmethod
      def updateFighting(cls, form):

            query = """
            UPDATE dojos set
            SET fighting_speciality = %(fighting_speciality)s
            WHERE id = %(id)s
            """
            connectToMySQL("dojos_and_ninjas").query_db(query)

      @classmethod
      def create(cls, form):

            query = """
            INSERT INTO dojos
            (name, fighting_speciality)
            VALUES
            (%(name)s, %(fighting_speciality)s)
            """
            id_of_created_entry = connectToMySQL("dojos_and_ninjas").query_db(query, form)
            return id_of_created_entry

      @classmethod
      def deleteDojo(cls, id):

            data = {"id": id}

            query = """
            DELETE FROM dojos where id = %(id)s
            """

            connectToMySQL("dojos_and_ninjas").query_db(query)
