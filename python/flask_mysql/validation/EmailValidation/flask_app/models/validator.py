from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Validator:
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def add(cls, data):
        query = 'INSERT INTO emails (email, created_at, updated_at) VALUES (%(email)s, NOW(), NOW())'
        return connectToMySQL('email_validation').query_db(query,data)

    @classmethod
    def get_emails(cls):
        query = 'SELECT * FROM emails'
        results = connectToMySQL('email_validation').query_db(query)
        email_list = []
        for email in results:
            email_list.append(cls(email))
        return email_list

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM emails WHERE id = %(id)s'
        return connectToMySQL('email_validation').query_db(query,data)

    @classmethod
    def check_email(cls, data):
        query = 'SELECT * FROM emails WHERE email = %(email)s;'
        results = connectToMySQL('email_validation').query_db(query, data)
        return results

    @staticmethod
    def validate_email(email):
        is_valid = True
        if not EMAIL_REGEX.match(email['email']):
            flash("invalid email address!")
            is_valid = False
        return is_valid