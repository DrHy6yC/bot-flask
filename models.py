from flask_login import UserMixin

from create_app import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    login = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    answer = db.relationship('AnswerUser', backref='user', lazy='dynamic')

    def get_id(self):
        return str(self.id)


class AnswerUser(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    # Изначально хотель сделать через Foreign key но при удалении вопросов невозможно было бы посмотреть ответы пользователя
    question = db.Column(db.String(100), nullable=False, unique=True)
    answer_user = db.Column(db.String(100), nullable=False)


class Question(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    question = db.Column(db.String(100), nullable=False, unique=True)
