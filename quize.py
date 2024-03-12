from flask import Blueprint, render_template

from models import Question

quize = Blueprint('quize', __name__)


@quize.route("/questions", methods=['GET'])
def questions():
    questions = Question.query.all()
    return render_template('questions.html', title="Вопросы", questions=questions)
