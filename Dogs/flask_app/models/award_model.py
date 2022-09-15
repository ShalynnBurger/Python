from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import dog_model

class Award:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dog_id = data['dog_id']

    @classmethod
    def create(cls, data):
        query = "INSERT INTO awards (title, dog_id) VALUES (%(title)s, %(dog_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)