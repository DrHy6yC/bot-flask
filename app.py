from icecream import ic

from flask import render_template, request
from flask_login import login_required

from create_app import app, db
from authorization import auth as auth_blueprint
from quize import quize as quize_blueprint


app.register_blueprint(auth_blueprint)
app.register_blueprint(quize_blueprint)


@app.route("/")
def index():
    return render_template('index.html', title="Главная")


@app.route("/create_db", methods=['POST', 'GET'])
@login_required
def create_db():
    if request.method == 'POST':
        if request.get_data(as_text=True):
            ic(request.get_data(as_text=True))
            db.drop_all()
            db.create_all()
    return render_template('create_db.html')


@app.route("/test")
@login_required
def test():
    return render_template('test.html', title="Главная")


if __name__ == "__main__":
    app.run(debug=True, port=3000)


