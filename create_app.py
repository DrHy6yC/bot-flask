from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Bot.db'
app.config['SECRET_KEY'] = 'p?ikvBmp6@'

db = SQLAlchemy(app)
