import requests
from icecream import ic

res = requests.post("http://127.0.0.1:3000/api/question_add/", {'question': "How are You?"})
ic(res)
