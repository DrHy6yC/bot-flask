from icecream import ic

from flask import Blueprint, render_template, flash, request
from flask_login import current_user
from sqlalchemy import select, func

from create_app import db
from models import AnswerUser

profile = Blueprint('profile', __name__)


@profile.route("/user", methods=['GET', 'POST'])
def user():
    # db.session.query()
    answers_user = AnswerUser.query.filter_by(id_user=current_user.id)
    ic(answers_user)
    return render_template('profile.html', title=f"Профиль {current_user.login}", answers_user=answers_user)
