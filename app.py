from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_compress import Compress
from flask_talisman import Talisman
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
CORS(app)
Compress(app)
Talisman(app)
db = SQLAlchemy(app)

# routes
from src.routes.main import *
from src.routes.tropicalCyclone import *
from src.routes.trackHistory import *
from src.routes.forecastTrack import *

# celery cron job
from src.cron.cron import *

if __name__ == '__main__':
    if flask_env == 'development':
        app.run()
    else:
        print('server is running on production mode')
        serve(app, host="0.0.0.0", port=5000)
