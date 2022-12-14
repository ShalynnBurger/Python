from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import recipe_model
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.password = data['password']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (first_name, last_name, password, email) VALUES (%(first_name)s,%(last_name)s, %(password)s,%(email)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) <1:
            return False
        return cls(results[0])

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM users LEFT JOIN recipies on users.id = recipies.user_id WHERE users.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) <1:
            return False
        user =  cls(results[0])
        list_of_recipies = []
        for row in results:
            if row['recipies.id'] == None:
                break
            recipe_data = {
                **row,
                'id': row['recipies.id'],
                'created_at': row['recipies.created_at'],
                'updated_at': row['recipies.updated_at']
            }
            this_party = recipe_model.Recipe(recipe_data)
            list_of_recipies.append(this_party)
        user.recipies = list_of_recipies
        return user


    @staticmethod
    def validate(user_data):
        is_valid = True
        if len(user_data['first_name']) < 1:
            flash("First name required", 'reg')
            is_valid = False
        if len(user_data['last_name']) < 1:
            flash("Last name required", 'reg')
            is_valid = False
        if len(user_data['email']) < 1:
            flash("Email required", 'reg')
            is_valid = False
        elif not EMAIL_REGEX.match(user_data['email']):
            flash("Invalid email format", 'reg')
            is_valid = False
        else:
            data = {
                'email':user_data['email']
            }
            potential_user = User.get_by_email(data)
            if potential_user:
                flash("Email is already registered.", 'reg')
                is_valid = False
        if len(user_data['first_name']) < 1:
            flash("First name required", 'reg')
            is_valid = False
        if len(user_data['password']) < 8:
            flash("Password > 8 characters", 'reg')
            is_valid = False
        elif not user_data['password'] == user_data['password2']:
            flash("Passwords do not match", 'reg')
            is_valid = False
        return is_valid