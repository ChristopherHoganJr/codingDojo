from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash
import re


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_new_user(cls, data):
        query = 'INSERT INTO user (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());'
        return connectToMySQL('recipes_assignment').query_db(query, data)

    @classmethod
    def check_email_db(cls,data):
        query = 'SELECT * FROM user WHERE email = %(email)s;'
        results = connectToMySQL('recipes_assignment').query_db(query, data)
        print('im checking')
        return results

    @classmethod
    def get_user_by_email(cls, data):
        query = 'SELECT * FROM user WHERE email = %(email)s;'
        result = connectToMySQL('recipes_assignment').query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])

    @staticmethod
    def validate_form(data):
        is_valid = True
        if not EMAIL_REGEX.match(data['email']):
            flash('invalid email address!')
            is_valid = False
        if len(data['first_name']) < 2 and len(data['first_name']) <= 255:
            flash('first name needs to be more than 2 characters')
            is_valid = False
        if len(data['last_name']) < 2 and len(data['last_name']) <= 255:
            flash('last name needs to be more than 2 characters')
            is_valid = False
        if data['password'] != data['confirm_password']:
            flash('Passwords must match')
        if len(data['password']) <= 5 and len(data['password']) >= 20:
            flash('passwords must be between 8 and 20 characters')
            is_valid = False
        
        return is_valid