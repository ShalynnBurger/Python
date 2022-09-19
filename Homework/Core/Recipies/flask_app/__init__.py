from flask import Flask

app = Flask(__name__)

app.secret_key = "shhhhh"
DATABASE = 'recipies_db'