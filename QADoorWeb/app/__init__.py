from .qadoor_app import app
from .qadoor_db import db
# from .user import User
# from .user import user
from .question import Questions
from .question import question
# from .extensions import login_manager



app.register_blueprint(question)
# app.register_blueprint(user)
# configure_login(app)