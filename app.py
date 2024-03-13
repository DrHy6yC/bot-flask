from icecream import ic

from flask import render_template
from flask_login import login_required

from create_app import app, db, DB_OWERWRITE
from api import api, api_blueprint
from authorization import auth as auth_blueprint
from quize import quize as quize_blueprint
from profile import profile as profile_blueprint


app.register_blueprint(auth_blueprint)
app.register_blueprint(quize_blueprint)
app.register_blueprint(profile_blueprint)
app.register_blueprint(api_blueprint)

api.init_app(app)


@app.route("/")
def index():
    return render_template('index.html', title="Главная")


@app.route("/test")
@login_required
def test():
    return render_template('test.html', title="Мемчик")


if __name__ == "__main__":
    with app.app_context():
        ic(DB_OWERWRITE)
        if DB_OWERWRITE:
            db.drop_all()
            db.create_all()
            ic("Таблицы пересозданы")
    app.run(debug=True, port=3000)
