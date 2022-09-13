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


@app.route('/users/<int:id>')
def one_user(id):
    one_user = User.get_one({'id':id})
    return render_template("show_user.html", one_user=one_user)


@app.route('/users/<int:id>/edit')
def edit_user_form(id):
    data = {'id':id}
    one_user = User.get_one(data)
    return render_template("edit_user.html", one_user=one_user)

@app.route('/users/<int:id>/update', methods=['POST'])
def update_user(id):
    data = {
        **request.form,
        'id':id
    }
    User.update(data)
    return redirect('/users')


@app.route('/users/<int:id>/delete')
def delete_user(id):
        data = {
        **request.form,
        'id':id
        }
        User.delete(data)
        return redirect('/users')





if __name__=="__main__":
    app.run(debug=True) 