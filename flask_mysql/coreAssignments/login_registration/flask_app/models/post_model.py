from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
from flask_app.models import user_model




class Post:
    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.title = data['title']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = None

    @classmethod
    def create_post(cls, title, content, session):
        user_id = session.get('user_id')
        print('\n\n\n user_id ------------->', user_id, '\n\n\n')
        data = {'title': title, 'content': content, 'user_id': user_id}
        query = """
    INSERT INTO posts (title, content, user_id, created_at, updated_at)
    VALUES (%(title)s, %(content)s, %(user_id)s, NOW(), NOW())
    """

        id_of_created_entry = connectToMySQL('logintests').query_db(query, data)
        return id_of_created_entry


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM posts"
        results = connectToMySQL('your_database_name').query_db(query)

        all_posts = []

        for row in results:
            new_post = cls(row)
            all_posts.append(new_post)

        return all_posts


    @classmethod
    def get_posts_with_authors(cls):
        query = """
        SELECT * FROM posts
        JOIN users ON posts.user_id = users.id
        """
        results = connectToMySQL('logintests').query_db(query)
        print('\n\n\n RESULTS FROM GET POST-------->>>', results, '\n\n')
        posts = []
        for row in results:
            new_post = cls(row)
            userdata = {
                'id': row['users.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'dob': row['dob'],
                'email': row['email'],
                'passwordhash': row['passwordhash'],
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at']
                        }
            userobject = user_model.User(userdata)
            new_post.user = userobject
            posts.append(new_post)

        return posts



