from flask_app.config.mysqlconnection import connectToMySQL
DATABASE = 'dojos_and_ninjas_schema'

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DATABASE).query_db(query)
        print("======================")
        print(results)
        print("======================")
        all_dojos = []
        for row_from_db in results:
            all_dojos.append(cls(row_from_db))
        return all_dojos