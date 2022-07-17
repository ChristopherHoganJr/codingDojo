from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Survey:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_last_entry(cls):
        query = 'SELECT * FROM dojo_survey ORDER BY id DESC LIMIT 1'
        results = connectToMySQL('dojo_survey_schema').query_db(query)
        survey_info = []
        for survey in results:
            survey_info.append(cls(survey))
        return survey_info

    @classmethod
    def create_new_info(cls, data):
        query = 'INSERT INTO dojo_survey (name, location, language, comment, created_at, updated_at) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s, NOW(), NOW())'
        return connectToMySQL('dojo_survey_schema').query_db(query,data)

    @staticmethod
    def validate_survey(survey):
        is_valid = True
        if len(survey['name']) < 3:
            flash("Name must be at least 3 characters")
            is_valid = False
        if survey['location'] == 'none':
            flash("You did not select a dojo location")
            is_valid = False
        if survey['language'] == 'none':
            flash("You did not select a favorite language")
            is_valid = False
        return is_valid

