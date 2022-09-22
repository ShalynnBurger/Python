from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user_model import User
from flask_app.models.car_model import Car

#add a new car
@app.route('/new/car')
def new_car_form():
    if 'user_id' not in session:
        return redirect('/')
    return render_template("new_car.html")

#add a new car behind the scenes
@app.route('/create/car', methods=['post'])
def process_car():
    if 'user_id' not in session:
        return redirect('/')
    if not Car.validator(request.form):
        return redirect('/new/car')
    data = {
        **request.form,
        'user_id': session['user_id']
    }
    id = Car.create(data)
    return redirect('/welcome')

#delete a car
@app.route('/delete/<int:id>/car')
def delete_car(id):
    if 'user_id' not in session:
        return redirect('/')
    car = Car.get_by_id({'id':id})
    Car.delete({'id': id})
    return redirect('/welcome')

#edit a car
@app.route('/edit/<int:id>/car')
def edit_car_form(id):
    if 'user_id' not in session:
        return redirect('/')
    car = Car.get_by_id({'id':id})
    if not int(session['user_id']) == car.user_id:
        flash("Ope, not yours!")
        return redirect('/welcome')
    car = Car.get_by_id({'id':id})
    return render_template("edit_car.html", car=car)

#edit a car behind the scenes 
@app.route('/update/<int:id>/car', methods=['post'])
def update_car(id):
    if 'user_id' not in session:
        return redirect('/')
    car = Car.get_by_id({'id':id})
    if not int(session['user_id']) == car.user_id:
        flash("Ope, not yours!")
        return redirect('/welcome')
    if not Car.validator(request.form):
        return redirect(f"/edit/{id}/car")
    data = {
        **request.form,
        'id':id
    }
    Car.update(data)
    return redirect('/welcome')

#view one car
@app.route('/car/<int:id>')
def show_car(id):
    car = Car.get_by_id({'id':id})
    return render_template("one_car.html", car=car)
