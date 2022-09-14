# from flask_app.config.mysqlconnection import connectToMySQL
# DATABASE = 'dojos_and_ninjas_schema'

# class Ninja:
#     def __init__(self, data):
#         self.id = data['id']
#         self.first_name = data['first_name']
#         self.last_name = data['last_name']
#         self.age = data['age']
#         self.created_at = data['created_at']
#         self.updated_at = data['updated_at']
#         self.dojo_id = data['dojo_id']

#     @classmethod
#     def get_all(cls):
#         query = "SELECT * FROM ninjas;"
#         results = connectToMySQL(DATABASE).query_db(query)
#         print("======================")
#         print(results)
#         print("======================")
#         all_ninjas = []
#         for row_from_db in results:
#             all_ninjas.append(cls(row_from_db))
#         return all_ninjas
    
#     @classmethod
#     def create(cls, data):
#         query = "INSERT INTO users (first_name, last_name, age) VALUES (%(first_name)s, %(last_name)s, %(age)s);"
#         result = connectToMySQL(DATABASE).query_db(query, data)
#         return result 