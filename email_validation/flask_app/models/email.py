from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

class Email:
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(csl, data):
        # return id of newly created data 
        query = """
            INSERT INTO emails (email)
            VALUES (%(email)s);
        """
        return connectToMySQL("emails_schema").query_db(query, data)
        
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails;"
        results = connectToMySQL("emails_schema").query_db(query)

        all_emails = []
        for row in results:
            all_emails.append(cls(row))
        return all_emails

        
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM emails WHERE id = %(id)s;"
        results = connectToMySQL("emails_schema").query_db(query, data)
        return cls(results[0])


    import re
    @staticmethod
    def email_validate(post_data):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        is_valid = True
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(post_data['email']):
            flash("Email is not valid!")
            is_valid = False
        return is_valid
