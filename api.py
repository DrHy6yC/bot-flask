from icecream import ic
import json

from flask import Blueprint, request, abort, jsonify
from flask_restful import Api, Resource, reqparse

from create_app import db
from models import Question

api = Api()

api_blueprint = Blueprint('api', __name__)


@api_blueprint.route('/api/questions', methods=['GET'])
def get_all_question():
    # if not request.json or not 'title' in request.json:
    #     abort(400)
    result = dict()
    # questions = Question.query.all()
    # for question in questions:
    #     result[question.id] = {'id': question.id, 'question': question.question}
    result_json = json.dumps(result)
    ic(result_json)
    return jsonify(result_json)


# class QuestionsAPI(Resource):
#     def get(self) -> dict:
#         result = dict()
#         questions = Question.query.all()
#         for question in questions:
#             result[question.id] = {'id': question.id, 'question': question.question}
#         ic(result)
#         return result
#
#
# class QuestionAddAPI(Resource):
#     def post(self) -> dict:
#         parser = reqparse.RequestParser()
#         parser.add_argument('question')
#         ic(parser.parse_args())
#         result = dict()
#         # question_check = Question.query.filter_by(question=question)
#         # if question_check:
#         #     new_question = Question(question=question)
#         #     db.session.add(new_question)
#         #     db.session.commit()
#         #     questions = Question.query.all()
#         #     for question in questions:
#         #         result[question.id] = {'id': question.id, 'question': question.question}
#         # else:
#         #     result = {'message': "Такой вопрос уже есть"}
#         # ic(result)
#         return result
#
#
# class QuestionAPI(Resource):
#     def get(self, id: int) -> dict:
#         question = Question.query.get(id)
#         result = {'id': question.id, 'question': question.question}
#         return result
#
#     def delete(self, id: int) -> dict:
#         question = Question.query.get(id)
#         if question:
#             db.session.delete(question)
#             db.session.commit()
#         result = dict()
#         questions = Question.query.all()
#         for question in questions:
#             result[question.id] = {'id': question.id, 'question': question.question}
#         ic(result)
#         return result
