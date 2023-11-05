from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
import random, string
from flask_bcrypt import Bcrypt
EMAIL_REGEX = re.compile(r'^[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+')
PASSWORD_REGEX = re.compile(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$')

# Initialize Bcrypt
bcrypt = Bcrypt()

db = 'db'

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.dob = data['dob']
        self.email = data['email']
        self.passwordhash = data['passwordhash']
        self.salt = data['salt']  # Include salt if needed
        self.salted_password = data['salted_password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate(user_data):
        is_valid = True

        print('\n\n\n results ------------->', user_data, '\n\n\n')

        if len(user_data['first_name']) < 2 or len(user_data['first_name']) > 255:
            flash('Min # of Chars: 2, Max # of Chars: 255', 'fname_err')
            is_valid = False

        if len(user_data['last_name']) < 2 or len(user_data['last_name']) > 255:
            flash('Min # of Chars: 2, Max # of Chars: 255', 'lname_err')
            is_valid = False
        dobvalue = user_data.get('dob')
        if not dobvalue:
            flash('Please Enter your date of birth', 'dob_err')
            is_valid = False

        if not EMAIL_REGEX.match(user_data['email']):
            flash('Please Enter a valid email address', 'email_err')
            is_valid = False

        if not PASSWORD_REGEX.match(user_data['password']):
              flash('***Minimum eight characters, at least one upper case English letter, one lower case English letter, one number and one special character***', 'pass_err')
              is_valid = False

        password = user_data.get('password')
        cpassword = user_data.get('c_password')
        if password != cpassword:
              flash('Ensure both passwords are matching', 'match_err')
              is_valid = False

        return is_valid

    @classmethod
    def create(cls, form):
        # Generate a hashed password
        hashed_password = bcrypt.generate_password_hash(form['password']).decode('utf-8')

        query = """
        INSERT INTO users
        (first_name, last_name, dob, email, passwordhash, salt, created_at, updated_at)
        VALUES
        (%(first_name)s, %(last_name)s, %(dob)s, %(email)s, %(passwordhash)s, %(salt)s %(salted_password)s, NOW(), NOW())
        """

        # Generate a random salt
        salt = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        salted_password = hashed_password + salt

        data = {
            'first_name': form['first_name'],
            'last_name': form['last_name'],
            'dob': form['dob'],
            'email': form['email'],
            'passwordhash': hashed_password,
            'salt': salt,  # Include the generated salt
            'salted_password': salted_password
        }

        try:
            id_of_created_entry = connectToMySQL('db').query_db(query, data)
            return id_of_created_entry
        except Exception as e:
            flash('An error occurred while creating the user', 'error')
            return None
