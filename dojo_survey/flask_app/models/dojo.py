from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def create(cls, data):
        # return id of the newly created dojo
        query = """
            INSERT INTO dojos(name, location, language, comment)
            VALUES(%(name)s, %(location)s, %(language)s, %(comment)s);
        """
        return connectToMySQL("dojo_survey_schema").query_db(query, data)


    @classmethod
    def get_all(cls):
        # return a list of objects
        query = "SELECT * FROM dojos;"
        results = connectToMySQL("dojo_survey_schema").query_db(query)

        # convert list of dicts to list of objects
        all_dojos = []
        for row in results:
            all_dojos.append(cls(row))
        return all_dojos


    @classmethod
    def get_one(cls, data):
        # return an object
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        results = connectToMySQL("dojo_survey_schema").query_db(query, data)
        return cls(results[0])
    
    # using static method: it doesn't need a class reference or an object reference 
    # put the static method in Dojo class since it validates dojos
    @staticmethod
    def validate(post_data):
        is_valid = True
        # attributes: name, location, language, comment

        if "name" not in post_data:
            flash("Stop changing the attribute in the website")
            is_valid = False
        elif len(post_data['name']) < 3:
            flash("Your name must be at least 3 characters.")
            is_valid = False

        if "location" not in post_data:
            flash("Stop changing the attribute in the website")
            is_valid = False
        # elif len(post_data['location']) < 3:
        #     flash("Dojo Location must be at least 3 characters.")
        #     is_valid = False
        
        if "location" not in post_data:
            flash("Stop changing the attribute in the website")
            is_valid = False
        # elif len(post_data['language'])< 3:
        #     flash("language must be at least 3 characters.")
        #     is_valid = False
        
        if "comment" not in post_data:
            flash("Stop changing the attribute in the website")
            is_valid = False
        elif len(post_data['comment']) < 5:
            flash("comment must be at least 5 characters.")
            is_valid = False

        return is_valid
    
