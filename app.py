from src.cron.cron import *
from src.routes.track_history import *
from src.routes.forecast_track import *
from src.routes.tropical_cyclone import *
from src.routes.main import *
from flask import Flask, request, make_response
from flask_sqlalchemy import SQLAlchemy
import os
from waitress import serve

from dotenv import load_dotenv
load_dotenv()

flask_env = os.environ.get('FLASK_ENV')

DB_CONFIG = {}
if flask_env == 'development':
    DB_CONFIG = {
        'user': 'donaldwu',
        'pw': '',
        'db': 'donaldwu',
        'host': 'localhost',
        'port': '5432',
    }
else:
    DB_CONFIG = {
        'user': 'donaldwu',
        'pw': 'donaldwu',
        'db': 'donaldwu',
        'host': 'db',
        'port': '5432',
    }

app = Flask(__name__)
app.config["DEBUG"] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{}:{}@{}:{}/{}'.format(
    DB_CONFIG['user'], DB_CONFIG['pw'], DB_CONFIG['host'], DB_CONFIG['port'], DB_CONFIG['db'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# routes

# celery cron job

if __name__ == '__main__':
    if flask_env == 'development':
        app.run()
    else:
        serve(app, host="0.0.0.0", port=5000)
