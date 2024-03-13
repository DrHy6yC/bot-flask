from icecream import ic

from flask import Blueprint, render_template, flash, request, redirect, url_for
from flask_login import current_user, login_required
from sqlalchemy import desc


from create_app import db
from models import Question, AnswerUser

quize = Blueprint('quize', __name__)


@quize.route("/questions", methods=['GET', 'POST'])
@login_required
def question_quize():
    questions = Question.query.order_by(Question.id).all()
    if request.method == 'POST':
        answer_user_last = AnswerUser.query.filter_by(id_user=current_user.id).\
            order_by(desc(AnswerUser.attempt_user)).first()
        ic(answer_user_last)
        if answer_user_last:
            attempt_user = answer_user_last.attempt_user + 1
        else:
            attempt_user = 1
        for key in request.form.keys():
            question_text = Question.query.get(int(key)).question

            ic(key, request.form.get(key), current_user.id, attempt_user)
            new_answer = AnswerUser(
                id_user=current_user.id,
                question=question_text,
                answer_user=request.form.get(key),
                attempt_user=attempt_user
            )
            db.session.add(new_answer)
            db.session.commit()
        flash(f"Ответы {current_user.login} записаны, можно посмотреть в профиле.")

    return render_template('questions.html', title="Вопросы", questions=questions)


@quize.route("/add_question", methods=['GET', 'POST'])
@login_required
def add_question():
    if request.method == 'POST':
        text_question = request.form.get('question')
        ic(text_question)
        ic()
        if bool(Question.query.filter_by(question=text_question).first()):
            flash("Такой вопрос уже есть в БД", 'info')
        else:
            new_question = Question(question=text_question)
            db.session.add(new_question)
            db.session.commit()
            flash("Вопрос добавлен", 'info')

    return render_template('add_question.html', title="Добавляем вопросы")


@quize.route("/delete_answer", methods=['POST'])
@login_required
def delete_answer():
    ic(url_for('quize.delete_answer'))
    ic(request.form.items())
    id_answer = request.form['id']
    answer = AnswerUser.query.get(id_answer)
    ic(id_answer)
    ic(answer)
    if answer:
        ic()
        db.session.delete(answer)
        db.session.commit()
        ic("Удален ответ")
        flash("Удален ответ")
    else:
        ic()
        ic("Ответ не удален")
        flash("Ответ не удален")
    return redirect(url_for('profile.user'))


@quize.route("/change_answer", methods=['POST'])
@login_required
def change_answer():
    id_answer = request.form['id']
    text_answer = request.form['answer']
    ic(id_answer, text_answer)
    answer = AnswerUser.query.get(id_answer)
    answer.answer_user = text_answer
    ic(answer.__dict__)
    db.session.add(answer)
    db.session.commit()
    return redirect(url_for('profile.user'))


@quize.route("/delete_question", methods=['POST', 'GET'])
@login_required
def delete_question():
    if request.method == 'POST':
        id_question = request.form['id']
        question = Question.query.get(id_question)
        if question:
            db.session.delete(question)
            db.session.commit()
            flash("Вопрос удален")
        else:
            flash("Вопрос не удален")
    questions = Question.query.order_by(Question.id).all()
    return render_template('delete_questions.html', title="Удаление вопросов", questions=questions)
