from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import user_model

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date = data['date']
        self.cook_time = data['cook_time']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def create(cls, data):
        query = "INSERT INTO parties (name, description, instructions, date, cook_time, user_id) VALUES (%(name)s,%(description)s, %(instructions)s,%(date)s, %(cook_time)s,%(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipies JOIN users on recipies.user_id;"
        results = connectToMySQL(DATABASE).query_db(query)
        if results:
            all_recipies = []
            for row in results:
                this_recipe = cls(row)
                user_data = {
                    **row,
                    'id': row['users.id'],
                    'created_at': row['users_created_at'],
                    'updated_at': row['users.updated_at']
                }
                this_user = user_model.User(user_data)
                this_recipe.planer = this_user
                all_recipies.append(this_recipe)
            return all_recipies
        return []

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM recipies WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM recipies JOIN users on user.id = recipies.user_id WHERE recipies.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        if len(results) < 1:
            return False
        row = results[0]
        this_recipe = cls(row)
        user_data = {
            **row,
            'id': row['users_id'],
            'created_at': row['users.created_at'],
            'updated_at': row['users.updated_at']
        }
        planner = user_model.User(user_data)
        this_recipe.planner=planner
        return this_recipe

    @classmethod
    def update(cls,data):
        query = "UPDATE recipies SET name = %(name)s, description = %(description)s,date = %(date)s,cook_time = %(cook_time)s,instructions = %(instructions)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validator(form_data):
        is_valid = True
        if len(form_data['name'])<1:
            flash("name required")
            is_valid = False
        if len(form_data['description'])<1:
            flash("description required")
            is_valid = False
        if len(form_data['instructions'])<1:
            flash("instructions required")
            is_valid = False
        if len(form_data['date'])<1:
            flash("date required")
            is_valid = False
        if "cook_time" not in form_data:
            flash("cook time required")
            is_valid = False
        return is_valid 