from icecream import ic

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Bot.db'
db = SQLAlchemy(app)

SECRET_KEY = 'edsgntu74nf$%@h3jUQ,slfkdccfde4232[q[e[dxldc.vlkekeokzkaiqkwm432kse'


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    login = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(250), nullable=False)


@app.route("/")
def index():
    return render_template('index.html', title="Главная")


@app.route("/create_db", methods=['POST', 'GET'])
def create_db():
    if request.method == 'POST':
        ic(bool(request.get_data(as_text=True)))
        if request.get_data(as_text=True):
            db.create_all()
    return render_template('create_db.html')


@app.route("/auth", methods=['POST', 'GET'])
def auth():
    ic(request, type(request))
    if request.method == 'POST':
        passwd = generate_password_hash(request.form['password'], 'pbkdf2')
        ic(request.form['login'])
        ic(request.form['password'])
        ic(passwd)
        user = User(login=request.form['login'], password=passwd)
        db.session.add(user)
        db.session.commit()

    return render_template('auth.html', title="Вход в приложение")


if __name__ == "__main__":
    app.run(debug=True, port=3000)
