from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_dojos(cls):
        query = 'SELECT * FROM dojos'
        results = connectToMySQL('dojos_and_ninjas').query_db(query)

        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))

        return dojos

    @classmethod
    def create_new_dojo(cls, data):
        query = 'INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW())'
        return connectToMySQL('dojos_and_ninjas').query_db(query,data)

    @classmethod
    def show_ninjas_in_dojo(cls, data):
        query = 'SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojos_id = dojos.id WHERE dojos.id = %(id)s' 
        return connectToMySQL('dojos_and_ninjas').query_db(query,data)