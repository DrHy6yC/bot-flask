import requests
from icecream import ic

res1 = requests.get("http://127.0.0.1:3000/api/questions")
ic(res1.json())
