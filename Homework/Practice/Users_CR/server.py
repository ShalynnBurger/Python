from flask import Flask, render_template, request, redirect
from user_model import User
app = Flask(__name__)


@app.route('/users')
def index():
    all_users = User.get_all()
    print(all_users)
    return render_template("users.html", all_users=all_users)


@app.route('/users/new')
def new_user_form():
    return render_template("create_user.html")

@app.route('/users/create', methods=['POST'])
def create_user():
    User.create(request.form)
    return redirect('/users')

if __name__=="__main__":
    app.run(debug=True) 