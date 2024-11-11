from flask import render_template, redirect, request, session, flash # type: ignore
from flask_app import app
from flask_app.models.recipe import Recipe
from flask_app.models.user import User

@app.route('/recipes')
def recipes():
    if 'user_id' not in session:
        return redirect('/')
    recipes = Recipe.get_all()
    user = User.get_user_by_id({'id': session["user_id"]})
    return render_template('recipes.html', recipes=recipes, user=user)

@app.route('/recipes/new')
def new_recipe():
    if 'user_id' not in session:
        return redirect('/')
    return render_template("add_recipe.html")

@app.route('/recipes/create', methods=['POST'])
def create_recipe():
    if 'user_id' not in session:
        return redirect('/')
    if Recipe.validate_recipe(request.form):
            data = {
            **request.form,
            "user_id":session["user_id"]
    }
    Recipe.save(data)
    return redirect('/recipes')

@app.route('/recipes/view/<int:id>')
def show_one(id):
    if "user_id"not in session:
        return redirect('/')
    recipe = Recipe.get_by_id({"id":id})
    logged_user = User.get_user_by_id({"id":session["user_id"]})
    return render_template("view_recipe.html",recipe = recipe,user = logged_user)



@app.route('/recipes/edit/<int:id>')    
def edit_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    recipe = Recipe.get_by_id({'id': id})
    return render_template("edit_recipce.html", recipe=recipe)


#Action Route for the edit
@app.route("/recipes/update",methods=["POST"])
def update():
    if Recipe.validate_recipe(request.form):
        Recipe.update(request.form)
        return redirect('/recipes')
    return redirect(f'/recipes/edit/{id}')

@app.route("/recipes/delete/<int:id>",methods = ["POST"])
def delete(id):
    Recipe.delete({"id": id})
    return redirect('/recipes')

