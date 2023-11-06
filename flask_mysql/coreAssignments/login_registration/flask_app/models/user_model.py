from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
import random, string
from flask_bcrypt import Bcrypt
EMAIL_REGEX = re.compile(r'^[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+')
PASSWORD_REGEX = re.compile(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$')

# Initialize Bcrypt
bcrypt = Bcrypt()

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.dob = data['dob']
        self.email = data['email']
        self.passwordhash = data['passwordhash']
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

        if User.select_by_email(user_data['email']):
            flash('A user has already registered with that email address', 'email_dup')
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
        (first_name, last_name, dob, email, passwordhash, created_at, updated_at)
        VALUES
        (%(first_name)s, %(last_name)s, %(dob)s, %(email)s, %(passwordhash)s, NOW(), NOW())
        """


        data = {
            'first_name': form['first_name'],
            'last_name': form['last_name'],
            'dob': form['dob'],
            'email': form['email'],
            'passwordhash': hashed_password,
        }


        try:
            id_of_created_entry = connectToMySQL('logintests').query_db(query, data)
            return id_of_created_entry
        except Exception as e:
            flash('An error occurred while creating the user', 'error')
            return None

    @classmethod
    def select_by_email(cls, email):

        data = {"email": email}
        query = """

        SELECT * FROM  users
        WHERE email = %(email)s
        """

        results = connectToMySQL('logintests').query_db(query, data)
        if results:
            return cls(results[0])
        else:
            return False

    @classmethod
    def select_id_by_email(cls, l_email):

        data = {"l_email": l_email}

        query = """

        SELECT * FROM users
        WHERE EMAIL = %(l_email)s

        """
        results = connectToMySQL('logintests').query_db(query, data)
        if results:
            return (results[0]['id'])
        else:
            return None


    @classmethod
    def login(cls, l_email, l_password):
        is_valid = True
        found_user = cls.select_by_email(l_email)
        if found_user:
            user_details = found_user.as_dict()
            print('\n\n\n ---------->user_details=', user_details)
            stored_hashed_password = user_details.get('passwordhash')
            print('\n\n\n ------->stored_hashed_password =', stored_hashed_password, '\n')
            print('\n\n\n ------->l_password =', l_password, '\n')
            if bcrypt.check_password_hash(stored_hashed_password, l_password):
                print('\n ----------> IT WAS A MATCH!!!!!!!!!!!!!!!!!!\n\n\n')
                return True
            else:
                print('Incorrect password')
                flash('Incorrect Password, Please try again', 'inc_pw')
                return False
        else:
            print(f'User with email {l_email} not found in the database')
            flash('No user with email {l_email} was not found.','login_err' )
            is_valid = False

        return is_valid





    def as_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'dob': self.dob,
            'email': self.email,
            'passwordhash': self.passwordhash,
            'created_at': self.created_at,
            'updated_at': self.updated_at

        }
