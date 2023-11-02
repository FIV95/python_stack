from flask_app.config.mysqlconnection import connectToMySQL

class User:
      def __init__(self, data):
            self.id = data['id']
            self.name = data['name']
            self.phone = data['phone']
            self.email = data['email']
            self.created_at = data['created_at']
            self.updated_at = data['updated_at']



      @classmethod
      def get_all(cls):

            query = 'SELECT * FROM users'

            results = connectToMySQL('users8_db').query_db(query)
            all_users = []

            for row in results:
                  new_class = cls(row)
                  all_users.append(new_class)
            return all_users

      @classmethod
      def create(cls, form):

            query = """
            INSERT INTO users
            (name, phone, email)
            VALUES (%(name)s, %(phone)s, %(email)s)
            """
            id_of_created_row = connectToMySQL("users8_db").query_db(query, form)
            return id_of_created_row

      @classmethod
      def get_one(cls, id):

            data = {"id": id}

            query = """
            SELECT * FROM users
            WHERE id = (%(id)s)
            """
            results = connectToMySQL("users8_db").query_db(query,data)
            if results:
                  new_user = cls(results[0])
                  return new_user
            else:
                  return False

      @classmethod
      def update(cls, form):

            query = """
            UPDATE users set
            name = %(name)s,
            phone = %(phone)s,
            email = %(email)s
            WHERE id = %(id)s
            """
            connectToMySQL("users8_db").query_db(query, form)

      @classmethod
      def deleteJob(cls, id):

            data = {"id": id}

            query = "DELETE from jobs WHERE user_id = %(id)s;"
            connectToMySQL("users8_db").query_db(query, data)

            query = "UPDATE addresses set user_id = NULL WHERE user_id = %(id)s"
            connectToMySQL("users8_db").query_db(query,data)

            query = "DELETE from users WHERE id = %(id)s"
            connectToMySQL("users8_db").query_db(query,data)

      @classmethod
      def deleteAddress(cls, id):

            data = {"id": id}

            query = "UPDATE addresses set user_id = NULL WHERE user_id = %(id)s"
            connectToMySQL("users8_db").query_db(query,data)

      @classmethod
      def deleteUser(cls, id):

            data = {"id": id}

            query = "DELETE from users WHERE id = %(id)s"
            connectToMySQL("users8_db").query_db(query,data)

            ## Deletes job of user
            ## make address Nullable
            ## then delete user