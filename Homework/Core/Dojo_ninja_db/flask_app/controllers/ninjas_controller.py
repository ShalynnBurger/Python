from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.ninja_model import Ninja
from flask_app.models.dojo_model import Dojo


@app.route('/ninjas/new')
def new_ninja_form():
    dojos= Dojo.get_all()
    return render_template("new_ninja.html", all_dojos=dojos)


@app.route('/ninjas/create', methods=['post'])
def create_ninja():
    Ninja.create_ninja(request.form)
    return redirect('/')


#GET ALL
@app.route('/dojos/<int:id>')
def ninja_get_all(id):
    all_ninjas = Ninja.get_all()
    return render_template("show-dojo", all_ninjas=all_ninjas)