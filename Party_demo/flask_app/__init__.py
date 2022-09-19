from flask import Flask

app = Flask(__name__)

app.secret_key = "shhhhh"
DATABASE = 'party_demo_db'