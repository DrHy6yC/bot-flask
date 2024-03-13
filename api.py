from icecream import ic
import json

from flask import Blueprint, jsonify
from flask_restful import Api

from models import Question

api = Api()

api_blueprint = Blueprint('api', __name__)


@api_blueprint.route('/api/questions', methods=['GET'])
def get_all_question():
    result = dict()
    questions = Question.query.all()
    for question in questions:
        result[question.id] = {'id': question.id, 'question': question.question}
    result_json = json.dumps(result)
    ic(result_json)
    return jsonify(result_json)

