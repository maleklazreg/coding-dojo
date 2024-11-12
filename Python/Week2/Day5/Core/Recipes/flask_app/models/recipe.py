from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User
from flask_app import DATABASE
from flask import flash

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instruction = data['instruction']
        self.date_cooked = data['date_cooked']
        self.under_30 = data['under_30']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.owner = ""

    @classmethod
    def save(cls,data):
        query = """insert into recipes (name, description, instruction, date_cooked,
        under_30, user_id) values (%(name)s,%(description)s,%(instruction)s,
        %(date_cooked)s,%(under_30)s,%(user_id)s)"""
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query = """
                SELECT * FROM recipes
                JOIN users ON recipes.user_id = users.id;
                """
        results = connectToMySQL(DATABASE).query_db(query)
        recipes = []
        for row in results:
            recipe = cls(row)
            recipe.posted_by= f'{row["first_name"]}{row["last_name"]}'
            recipes.append(recipe)
        return recipes
    
    
    @classmethod
    def get_by_id(cls,data):
        query = """
                SELECT * FROM recipes
                JOIN users ON recipes.user_id = users.id
                WHERE recipes.id = %(id)s
                """
        result = connectToMySQL(DATABASE).query_db(query,data)
        recipe = cls(result[0])
        recipe.posted_by = f'{result[0]["first_name"]}{result[0]["last_name"]}'
        return recipe
    
    @classmethod
    def update(cls, data):
        query = """
        UPDATE recipes 
        SET name=%(name)s, 
        description=%(description)s, 
        instruction=%(instruction)s, 
        date_cooked=%(date_cooked)s, 
        under_30=%(under_30)s
        WHERE id = %(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query, data)

    
    @classmethod
    def delete(cls,data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @staticmethod
    def validate_recipe(recipe_data):
        is_valid = True
        if len(recipe_data['name']) < 3:
            flash("Recipe name must be at least 3 characters.","recipe_name")
            is_valid = False
        if len(recipe_data['description']) < 3:
            flash("Description must be at least 3 characters.","description")
            is_valid = False
        if len(recipe_data['instruction']) < 3:
            flash("instruction must be at least 3 characters.","instruction")
            is_valid = False
        if not recipe_data['date_cooked']:
            flash("Please select a date.")
            is_valid = False
        if 'under_30' not in recipe_data:
            flash("Please specify if the recipe takes less than 30 minutes.","date")
            is_valid = False
        return is_valid
    



    
    

    