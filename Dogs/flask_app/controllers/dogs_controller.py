from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dog_model import Dog


#GET ALL
@app.route('/')
def index():
    all_dogs = Dog.get_all()
    return render_template("index.html", all_dogs=all_dogs)

#NEW DOG FORM 
@app.route('/dogs/new')
def new_dog_form():
    return render_template("/dogs_new.html")

#ADD NEW DOG
@app.route('/dogs/create', methods=['post'])
def create_dog():
    Dog.create(request.form)
    return redirect('/')

#UPDATE DOG FORM
@app.route('/dogs/<int:id>/edit')
def edit_dog_form(id):
    data = {
        'id':id
    }
    this_dog = Dog.get_one(data)
    return render_template("dogs_edit.html", this_dog = this_dog)

#EDIT DOG
@app.route('/dogs/<int:id>/update', methods=['post'])
def update_dog(id):
    data = {
        **request.form,
        'id':id
    }
    Dog.update(data)
    return redirect('/')

#DELETE DOG
@app.route('/dogs/<int:id>/delete')
def delete_dog(id): 
    data = {
        'id':id
    }
    Dog.delete(data)
    return redirect('/')

#GET ONE DOG
@app.route('/dogs/<int:id>')
def one_dog(id):
    one_dog = Dog.get_one_with_awards({'id':id})
    return render_template('one_dog.html', one_dog=one_dog)
