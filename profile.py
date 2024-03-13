from icecream import ic

from flask import Blueprint, render_template, flash, request
from flask_login import current_user

from create_app import db
from models import AnswerUser

profile = Blueprint('profile', __name__)


@profile.route("/user", methods=['GET', 'POST'])
def user():
    answers_user = AnswerUser.query.filter_by(id_user=current_user.id)
    if request.method == 'POST':

        db.session.add()
        db.session.commit()
        flash("Вопрос добавлен", 'info')
    return render_template('profile.html', title=f"Профиль {current_user.login}", answers_user=answers_user)
