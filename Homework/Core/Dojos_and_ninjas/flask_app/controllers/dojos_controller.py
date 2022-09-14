from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.dojo_model import Dojo

@app.route('/dojos')
def index():
    all_dojos = Dojo.get_all()
    print(all_dojos)
    return render_template("dojos.html", all_dojos=all_dojos)