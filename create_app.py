from os import getenv
from dotenv import load_dotenv
from icecream import ic

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


load_dotenv()

app = Flask(__name__)


def get_uri() -> str:
    driver = ""
    db_params = f"{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    match DB_DBMS:
        case 'MYSQL':
            driver = f"mysql+mysqlconnector://"
        case 'PGSQL':
            driver = f"postgresql+psycopg://"
        case 'SQLite':
            driver = f"sqlite+pysqlite://"
            db_params = f"/{DB_SQLite}"
    uri = f"{driver}{db_params}"
    ic(uri)
    return uri


def str_bool(text: str) -> bool:
    result: bool = False
    if text.lower() == "true":
        result = True
    return result


DB_HOST: str = getenv('DB_HOST')
DB_PORT: str = getenv('DB_PORT')
DB_USER: str = getenv('DB_USER')
DB_PASS: str = getenv('DB_PASS')
DB_NAME: str = getenv('DB_NAME')
DB_SQLite: str = getenv('DB_SQLite')
DB_DBMS: str = getenv('DB_DBMS')

DB_OWERWRITE = str_bool(getenv('DB_OWERWRITE'))

app.config['SQLALCHEMY_DATABASE_URI'] = get_uri()
app.config['SECRET_KEY'] = 'p?ikvBmp6@'

db = SQLAlchemy(app)
