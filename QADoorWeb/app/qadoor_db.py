from flask_sqlalchemy import SQLAlchemy
from .qadoor_app import app

db = SQLAlchemy(app)