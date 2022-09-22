from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import user_model

class Car:
    def __init__(self, data):
        self.id = data['id']
        self.price = data['price']
        self.model = data['model']
        self.make = data['make']
        self.year = data['year']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def create(cls, data):
        query = "INSERT INTO cars (price, model, make, year, description, user_id) VALUES (%(price)s,%(model)s, %(make)s,%(year)s, %(description)s,%(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cars JOIN users on cars.user_id = users.id;"
        results = connectToMySQL(DATABASE).query_db(query)
        if len(results) > 0:
            all_cars = []
            for row in results:
                this_car = cls(row)
                user_data = {
                    **row,
                    'id': row['users.id'],
                    'created_at': row['users.created_at'],
                    'updated_at': row['users.updated_at']
                }
                this_user = user_model.User(user_data)
                this_car.seller = this_user
                all_cars.append(this_car)
            return all_cars
        return []

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM cars WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM cars JOIN users on users.id = cars.user_id WHERE cars.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        if len(results) < 1:
            return False
        row = results[0]
        this_car = cls(row)
        user_data = {
            **row,
            'id': row['users.id'],
            'created_at': row['users.created_at'],
            'updated_at': row['users.updated_at']
        }
        seller = user_model.User(user_data)
        this_car.seller = seller
        return this_car

# ; in query 
    @classmethod
    def update(cls,data):
        query = "UPDATE cars SET price = %(price)s, model = %(model)s, make = %(make)s, year = %(year)s, description = %(description)s WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validator(form_data):
        is_valid = True
        if len(form_data['price']) < 1:
            flash("Price is required")
            is_valid = False
        if len(form_data['model'])<1:
            flash("Model is required")
            is_valid = False
        if len(form_data['make'])<1:
            flash("Make is required")
            is_valid = False
        if len(form_data['year'])<1:
            flash("Year is required")
            is_valid = False
        if len(form_data['description'])<1:
            flash("Description is required")
            is_valid = False
        return is_valid 