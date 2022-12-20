from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from celery import Celery
from dotenv import load_dotenv
import os
from .config import SQLALCHEMY_DATABASE_URI

load_dotenv()



SECRET_KEY = os.getenv('SECRET_KEY')


app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SQLALCHEMY_POOL_SIZE'] = 370
app.config['SQLALCHEMY_MAX_OVERFLOW'] = 0


db = SQLAlchemy(app)
#migrate = Migrate(app, db)
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

with app.app_context():
    from app.views.views import view_bp
    from app.admin import admin
    app.register_blueprint(view_bp)