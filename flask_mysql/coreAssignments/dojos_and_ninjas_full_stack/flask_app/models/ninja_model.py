from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.dojo_model import Dojo

class Ninja:
      def __init__(self, data):
            self.id = data['id']
            self.first_name = data['first_name']
            self.last_name = data['last_name']
            self.age = data['age']
            self.created_at = data['created_at']
            self.updated_at = data['updated_at']
            self.dojo_id = data['dojo_id']



      @classmethod
      def get_all(cls):

            query = 'SELECT * FROM ninjas'

            results = connectToMySQL('dojos_and_ninjas').query_db(query)
            all_ninjas = []

            for row in results:
                  new_class = cls(row)
                  all_ninjas.append(new_class)
            return all_ninjas

      @classmethod
      def create(cls, form):

            query = """
            INSERT INTO ninjas
            (first_name, last_name, age, dojo_id)
            VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s)
            """
            id_of_created_entry = connectToMySQL("dojos_and_ninjas").query_db(query, form)
            return id_of_created_entry

      @classmethod
      def get_one(cls, id):

            data = {"id": id}

            query = """
            SELECT * FROM ninjas
            WHERE id = (%(id)s)
            """
            results = connectToMySQL("dojos_and_ninjas").query_db(query,data)
            if results:
                  new_ninja = cls(results[0])
                  return new_ninja
            else:
                  return False

      @classmethod
      def update(cls, form):

            query = """
            UPDATE users set
            first_name = %(first_name)s,
            last_name = %(last_name)s,
            age = %(age)s,
            dojo_id = %(dojo_id)s
            WHERE id = %(id)s
            """
            connectToMySQL("users8_db").query_db(query, form)

      @classmethod
      def delete(cls, id):

            data = {"id": id}

            query = "DELETE from ninjas WHERE id = %(id)s"
            connectToMySQL("dojos_and_ninjas").query_db(query,data)

      @classmethod
      def select(cls,form):

            query = """

            SELECT * FROM ninjas
            JOIN dojos
            ON dojos.id = ninjas.dojo_id
            WHERE ninjas.id = %(id)s

            """
            results = connectToMySQL("dojos_and_ninjas").query_db(query,form)

            all_ninjas = []
            for ninja in results:
                  new_ninja = cls(ninja)

                  dojo_data = {
                        **ninja,
                        "id" : ninja["dojos.id"],
                  }
                  new_dojo = Dojo(dojo_data)
                  new_ninja.ninja = new_dojo

                  all_ninjas.append(new_ninja)

            return all_ninjas