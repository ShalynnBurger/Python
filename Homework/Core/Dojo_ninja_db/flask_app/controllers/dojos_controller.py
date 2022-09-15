from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo_model import Dojo

#GET ALL
@app.route('/')
def index():
    all_dojos = Dojo.get_all()
    return render_template("index.html", all_dojos=all_dojos)


#GET ONE DOJO  
@app.route('/dojos/<int:id>')
def one_dojo(id):
    uno_dojo = Dojo.dojo_show_ninjas({'id':id})
    return render_template('show_dojo.html', one_dojo=uno_dojo)


#NEW DOJO FORM 
@app.route('/')
def new_dojo_form():
    return render_template("index.html")

#ADD NEW DOJO
@app.route('/dojos/create', methods=['post'])
def create_dojo():
    Dojo.create(request.form)
    return redirect('/')



