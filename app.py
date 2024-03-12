from icecream import ic

from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, UserMixin, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Bot.db'
app.config['SECRET_KEY'] = 'p?ikvBmp6@'
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.login_message = "Для просмотра страницы нужно войти в свой аккаунт"
login_manager.login_message_category = 'info'
login_manager.init_app(app)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    login = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)

    def get_id(self):
        return str(self.id)


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, user_id)


@app.route("/")
def index():
    return render_template('index.html', title="Главная")


@app.route("/create_db", methods=['POST', 'GET'])
@login_required
def create_db():
    if request.method == 'POST':
        if request.get_data(as_text=True):
            db.drop_all()
            db.create_all()
    return render_template('create_db.html')


@app.route("/test")
@login_required
def test():
    return render_template('test.html', title="Главная")


@app.route("/registration", methods=['GET'])
def registration():
    return render_template('registration.html', title="Войти")


@app.route("/registration", methods=['POST'])
def registration_post():
    email = request.form.get('email')
    user_login = request.form.get('login')
    password = request.form.get('password')

    user = User.query.filter_by(
        email=email).first()

    if user:
        flash('Пользователь с такой почтой уже существует', 'error')
        return redirect(url_for('registration'))
    try:
        new_user = User(email=email, login=user_login, password=generate_password_hash(password, method='pbkdf2'))
    except Exception as error:
        flash(f'Ошибка БД: {error}', 'error')

    db.session.add(new_user)
    db.session.commit()
    login_user(new_user)

    return redirect(url_for('login', title="Регистрация"))


@app.route("/login", methods=['GET'])
def login():
    return render_template('login.html', title="Войти")


@app.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('Введен неверный логин и пароль', 'error')
        return redirect(url_for('login'))

    login_user(user, remember=remember)
    return redirect(url_for('index', title='Войти'))


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True, port=3000)
