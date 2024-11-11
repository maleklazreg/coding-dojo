from flask import render_template, redirect, request, session, flash  # Import necessary Flask modules for routing and session management
from flask_app import app  # Import the Flask app instance
from flask_app.models.recipe import Recipe  # Import the Recipe model for database operations
from flask_app.models.user import User  # Import the User model to manage user data

@app.route('/recipes')
def recipes():
    if 'user_id' not in session:  # Check if the user is logged in
        return redirect('/')  # Redirect to the login page if not logged in
    recipes = Recipe.get_all()  # Fetch all recipes from the database
    user = User.get_user_by_id({'id': session["user_id"]})  # Fetch the logged-in user's details
    return render_template('recipes.html', recipes=recipes, user=user)  # Render the recipes page with recipes and user data

@app.route('/recipes/new')
def new_recipe():
    if 'user_id' not in session:  # Ensure the user is logged in
        return redirect('/')  # Redirect to the login page if not logged in
    return render_template("add_recipe.html")  # Render the form to add a new recipe

@app.route('/recipes/create', methods=['POST'])
def create_recipe():
    if 'user_id' not in session:  # Check if the user is logged in
        return redirect('/')  # Redirect if not logged in
    if Recipe.validate_recipe(request.form):  # Validate recipe form data
        data = {
            **request.form,
            "user_id": session["user_id"]  # Include user_id from the session
        }
        Recipe.save(data)  # Save the new recipe in the database
        return redirect('/recipes')  # Redirect to the recipes page
    return redirect('/recipes/new')  # Redirect back to the form if validation fails

@app.route('/recipes/view/<int:id>')
def show_one(id):
    if "user_id" not in session:  # Check if the user is logged in
        return redirect('/')  # Redirect if not logged in
    recipe = Recipe.get_by_id({"id": id})  # Get recipe details by ID
    logged_user = User.get_user_by_id({"id": session["user_id"]})  # Get the logged-in user's details
    return render_template("view_recipe.html", recipe=recipe, user=logged_user)  # Render the view page with recipe and user data

@app.route('/recipes/edit/<int:id>')
def edit_recipe(id):
    if 'user_id' not in session:  # Ensure the user is logged in
        return redirect('/')  # Redirect if not logged in
    recipe = Recipe.get_by_id({'id': id})  # Get the recipe by ID for editing
    return render_template("edit_recipe.html", recipe=recipe)  # Render the edit page with the recipe data

# Action route to handle recipe update
@app.route("/recipes/update", methods=["POST"])
def update():
    if Recipe.validate_recipe(request.form):  # Validate the updated recipe data
        Recipe.update(request.form)  # Update the recipe in the database
        return redirect('/recipes')  # Redirect to the recipes page
    return redirect(f'/recipes/edit/{request.form.get("id")}')  # Redirect back to edit form if validation fails

@app.route("/recipes/delete/<int:id>", methods=["POST"])
def delete(id):
    Recipe.delete({"id": id})  # Delete the recipe by ID from the database
    return redirect('/recipes')  # Redirect to the recipes page
