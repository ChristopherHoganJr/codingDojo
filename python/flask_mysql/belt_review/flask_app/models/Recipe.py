from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.User import User
from flask_app import app
from flask import flash

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date = data['date']
        self.under_30 = data['under_30']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.poster = None

    @classmethod
    def get_all_with_users(cls):
        query = 'SELECT * FROM recipe JOIN user ON recipe.user_id = user.id;'
        results = connectToMySQL('recipes_assignment').query_db(query)
        
        all_items = []

        for result in results:
            one_recipe = result

            user_data = {
                'id': one_recipe['user.id'],
                'name': one_recipe['name'],
                'under_30': one_recipe['under_30'],
                'first_name': one_recipe['first_name'],
                'last_name': one_recipe['last_name'],
                'email': one_recipe['email'],
                'password': one_recipe['password'],
                'created_at': one_recipe['user.created_at'],
                'updated_at': one_recipe['user.updated_at'],
            }

            all_items.append(user_data)

        print(all_items)
        return all_items
        
    @classmethod
    def create_new_recipe(cls, data):
        query = 'INSERT INTO recipe (name, description, instructions, date, under_30, created_at, updated_at, user_id) VALUES (%(name)s, %(description)s, %(instructions)s, %(date)s, %(under_30)s,NOW(), NOW(), %(user_id)s);'
        return connectToMySQL('recipes_assignment').query_db(query, data)

    @staticmethod
    def validate_recipe(data):
        is_valid = True
        if len(data['name']) < 3 and len(data['name']) <= 255:
            flash('Name needs to be at least 3 characters')
            is_valid = False
        if len(data['description']) < 3 and len(data['description']) <= 255:
            flash('Description needs to be at least 3 characters')
            is_valid = False
        if len(data['instructions']) < 3 and len(data['instructions']) <= 255:
            flash('Instructions needs to be at least 3 characters')
            is_valid = False
        if data['under_30'] != 'Yes' or data['under_30'] != 'No':
            flash('You need to select a time')
            is_valid = False
        if len(data['date']) < 3:
            flash('You must select a date')
            is_valid = False
        
        return is_valid