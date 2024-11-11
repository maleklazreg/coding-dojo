from flask_app.config.mysqlconnection import connectToMySQL  # Import database connection from config file
from flask_app.models.user import User  # Import the User class
from flask_app import DATABASE  # Import the database
from flask import flash  # type: ignore # Import flash for displaying messages

class Recipe:
    def __init__(self, data):  # Initialize the Recipe class
        self.id = data['id']  # Set the recipe ID
        self.name = data['name']  # Set the recipe name
        self.description = data['description']  # Set the recipe description
        self.instruction = data['instruction']  # Set the recipe instructions
        self.date_cooked = data['date_cooked']  # Set the date the recipe was cooked
        self.under_30 = data['under_30']  # Set whether the recipe takes under 30 minutes
        self.user_id = data['user_id']  # Set the user ID associated with the recipe
        self.created_at = data['created_at']  # Set the creation timestamp
        self.updated_at = data['updated_at']  # Set the last updated timestamp
        self.owner = ""  # Initialize owner to an empty string

    @classmethod
    def save(cls, data):  # Save a new recipe to the database
        query = """insert into recipes (name, description, instruction, date_cooked,
        under_30, user_id) values (%(name)s,%(description)s,%(instructions)s,
        %(date_cooked)s,%(under_30)s,%(user_id)s)"""
        return connectToMySQL(DATABASE).query_db(query, data)  # Execute the query with provided data

    @classmethod
    def get_all(cls):  # Retrieve all recipes from the database
        query = """
                SELECT * FROM recipes
                JOIN users ON recipes.user_id = users.id;
                """
        results = connectToMySQL(DATABASE).query_db(query)  # Execute the query
        recipes = []  # Initialize an empty list to store recipes
        for row in results:  # Iterate over each row in results
            recipe = cls(row)  # Create a Recipe object for each row
            recipe.posted_by = f'{row["first_name"]} {row["last_name"]}'  # Set the posted by user's full name
            recipes.append(recipe)  # Add the recipe to the list
        return recipes  # Return the list of recipes

    @classmethod
    def get_by_id(cls, data):  # Retrieve a recipe by its ID
        query = """
                SELECT * FROM recipes
                JOIN users ON recipes.user_id = users.id
                WHERE recipes.id = %(id)s
                """
        result = connectToMySQL(DATABASE).query_db(query, data)  # Execute the query with the provided data
        recipe = cls(result[0])  # Create a Recipe object with the first result
        recipe.posted_by = f'{result[0]["first_name"]} {result[0]["last_name"]}'  # Set the posted by user's full name
        return recipe  # Return the recipe

    @classmethod
    def update(cls, data):  # Update a recipe's details in the database
        query = """
        UPDATE recipes 
        SET name=%(name)s, 
        description=%(description)s, 
        instruction=%(instruction)s, 
        date_cooked=%(date_cooked)s, 
        under_30=%(under_30)s
        WHERE id = %(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query, data)  # Execute the update query with the provided data

    @classmethod
    def delete(cls, data):  # Delete a recipe from the database
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)  # Execute the delete query with the provided data

    @staticmethod
    def validate_recipe(recipe_data):  # Validate recipe data
        is_valid = True  # Initialize validity as True
        if len(recipe_data['name']) < 3:  # Check if name length is less than 3
            flash("Recipe name must be at least 3 characters.", "recipe_name")  # Flash an error message
            is_valid = False  # Set validity to False
        if len(recipe_data['description']) < 3:  # Check if description length is less than 3
            flash("Description must be at least 3 characters.", "description")  # Flash an error message
            is_valid = False  # Set validity to False
        if len(recipe_data['instruction']) < 3:  # Check if instruction length is less than 3
            flash("Instructions must be at least 3 characters.", "instruction")  # Flash an error message
            is_valid = False  # Set validity to False
        if not recipe_data['date_cooked']:  # Check if date is not provided
            flash("Please select a date.")  # Flash an error message
            is_valid = False  # Set validity to False
        if 'under_30' not in recipe_data:  # Check if under_30 field is not provided
            flash("Please specify if the recipe takes less than 30 minutes.", "date")  # Flash an error message
            is_valid = False  # Set validity to False
        return is_valid  # Return the validity status
