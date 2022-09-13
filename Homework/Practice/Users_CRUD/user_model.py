from mysqlconnection import connectToMySQL
DATABASE = 'users_schema'
class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)
        print("======================")
        print(results)
        print("======================")
        all_users = []
        for row_from_db in results:
            all_users.append(cls(row_from_db))
        return all_users

    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result 

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id=%(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) > 0:
            user_instance = cls(results[0])
            return user_instance
        return False

    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name =  %(last_name)s, email = %(email)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
