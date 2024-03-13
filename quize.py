from flask_login import current_user
from icecream import ic

from flask import Blueprint, render_template, flash, request

from create_app import db
from models import Question, AnswerUser

quize = Blueprint('quize', __name__)


@quize.route("/questions", methods=['GET', 'POST'])
def questions():
    questions = Question.query.order_by(Question.id).all()
    if request.method == 'POST':
        for key in request.form.keys():
            question_text = Question.query.get(int(key)).question
            ic(key, request.form.get(key), current_user.id)
            new_answer = AnswerUser(id_user=current_user.id, question=question_text, answer_user=request.form.get(key))
            db.session.add(new_answer)
            db.session.commit()
        flash(f"Ответы {current_user.login} записаны, можно посмотреть в профиле.")

    return render_template('questions.html', title="Вопросы", questions=questions)


@quize.route("/add_question", methods=['GET', 'POST'])
def add_question():
    if request.method == 'POST':
        text_question = request.form.get('question')
        new_question = Question(question=text_question)
        db.session.add(new_question)
        db.session.commit()
        flash("Вопрос добавлен", 'info')
    return render_template('add_question.html', title="Вопросы")
