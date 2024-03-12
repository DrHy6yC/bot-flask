from flask import render_template, request, flash, redirect, url_for, Blueprint
from flask_login import LoginManager, login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from create_app import app, db
from models import User


auth = Blueprint('auth', __name__)


login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message = "Для просмотра страницы нужно войти в свой аккаунт"
login_manager.login_message_category = 'info'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, user_id)


@auth.route("/registration", methods=['GET'])
def registration():
    return render_template('registration.html', title="Войти")


@auth.route("/registration", methods=['POST'])
def registration_post():
    email = request.form.get('email')
    user_login = request.form.get('login')
    password = request.form.get('password')

    user_with_email = User.query.filter_by(
        email=email).first()

    user_with_login = User.query.filter_by(
        login=user_login).first()

    if user_with_email:
        flash('Пользователь с такой почтой уже существует', 'error')
        return redirect(url_for('auth.registration'))
    elif user_with_login:
        flash('Пользователь с таким логином уже существует', 'error')
        return redirect(url_for('auth.registration'))
    else:
        try:
            new_user = User(email=email, login=user_login, password=generate_password_hash(password, method='pbkdf2'))
        except Exception as error:
            flash(f'Ошибка БД: {error}', 'error')

    db.session.add(new_user)
    db.session.commit()
    login_user(new_user)

    return redirect(url_for('auth.login', title="Регистрация"))


@auth.route("/login", methods=['GET'])
def login():
    return render_template('login.html', title="Войти")


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('Введен неверный логин и пароль', 'error')
        return redirect(url_for('auth.login'))

    login_user(user, remember=remember)
    return redirect(url_for('index', title='Войти'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
