from icecream import ic

from flask import Blueprint, render_template
from flask_login import current_user, login_required

from models import AnswerUser

profile = Blueprint('profile', __name__)


@profile.route("/user", methods=['GET', 'POST'])
@login_required
def user():
    answers_user = AnswerUser.query.filter_by(id_user=current_user.id)
    ic(answers_user)

    is_not_answers = False
    if answers_user.count() == 0:
        is_not_answers = True
    ic(is_not_answers)
    return render_template(
        'profile.html',
        title=f"Профиль {current_user.login}",
        answers_user=answers_user,
        is_not_answers=is_not_answers
    )
