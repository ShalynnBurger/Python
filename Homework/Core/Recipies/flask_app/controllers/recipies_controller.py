from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user_model import User
from flask_app.models.recipe_model import Recipe

@app.route('/recipies/new')
def new_recipe_form():
    if 'user_id' not in session:
        return redirect('/')
    return render_template("recipe_new.html")

@app.route('/recipies/create', methods=['post'])
def process_recipe():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        **request.form,
        'user_id': session['user_id']
    }
    id = Recipe.create(data)
    return redirect(f'/recipies/{id}')

@app.route('/recipies/<int:id>/delete')
def del_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    recipe = Recipe.get_by_id({'id':id})
    if not int(session['user_id']) == recipe.user_id:
        flash("Ope, not yours!")
        return redirect('/welcome')
    Recipe.delete({'id': id})
    return redirect('/welcome')

@app.route('/recipies/<int:id>/edit')
def edit_recipe_form(id):
    if 'user_id' not in session:
        return redirect('/')
    recipe = Recipe.get_by_id({'id':id})
    if not int(session['user_id']) == recipe.user_id:
        flash("Ope, not yours!")
        return redirect('/welcome')
    recipe = Recipe.get_by_id({'id':id})
    return render_template("recipies_edit.html", recipe=recipe)

@app.route('/recipies/<int:id>/update', methods=['post'])
def update_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    recipe = Recipe.get_by_id({'id':id})
    if not int(session['user_id']) == recipe.user_id:
        flash("Ope, not yours!")
        return redirect('/welcome')
    if not Recipe.validator(request.form):
        return redirect(f"/recipies/{id}/edit")
    data = {
        **request.form,
        'id':id
    }
    Recipe.update(data)
    return redirect('/welcome')

@app.route('/recipies/<int:id>')
def show_recipe(id):
    recipe = Recipe.get_by_id({'id':id})
    return render_template("recipies_one.html", recipe=recipe)

# @app.route('/my_recipies')
# def my_recipies():
#     if 'user_id' not in session:
#         return redirect('/')
#     user = User.get_by_id({'id': session['user_id']})
#     return render_template("my_recipies.html", logged_user=user)