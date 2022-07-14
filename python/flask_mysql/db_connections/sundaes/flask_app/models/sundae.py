from flask_app.config.mysqlconnection import connectToMySQL

class Sundae:
    def __init__(self, data):
        self.id = data['id']
        self.flavor = data['flavor']
        self.scoops = data['scoops']
        self.sauce = data['sauce']
        self.topping1 = data['topping1']
        self.topping2 = data['topping2']
        self.container = data['container']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM sundaes'

        results = connectToMySQL('sundaes_schema_july2022').query_db(query)

        sundaes = []

        for sundae in results:
            sundaes.append(cls(sundae))
        return sundaes

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO sundaes (flavor, sauce, scoops, topping1, topping2, created_at, updated_at) VALUE (%(flavor)s, %(sauce)s, %(scoops)s, %(topping1)s, %(topping2)s, NOW(), NOW())'
        return connectToMySQL('sundaes_schema_july2022').query_db(query, data)