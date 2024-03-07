from icecream import ic

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Bot.db'
db = SQLAlchemy(app)

isDATABASE = False


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    login = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(20), nullable=False)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/create_db")
def create_db():
    # global isDATABASE
    # if not isDATABASE:
    #     app.app_context().push()
    #     db.create_all()
    #     isDATABASE = True
    return render_template('create_db.html')


@app.route("/auth", methods=['POST', 'GET'])
def auth():
    if request.method == 'POST':
        ic(request.form['login'])
        ic(request.form['password'])

    return render_template('auth.html')


if __name__ == "__main__":
    app.run(debug=True)
