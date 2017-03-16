from ..qadoor_db import db

class Questions(db.Model):

    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    reprint_link = db.Column(db.String(256), nullable=False)
    question_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    status = db.Column(db.Integer, default=0)
    answer_count = db.Column(db.Integer)
    view_count = db.Column(db.Integer)
    vote_count = db.Column(db.Integer)
    tags = db.Column(db.String(256))
    created_date = db.Column(db.DateTime)
    updated_date = db.Column(db.DateTime)

class Answers(db.Model):

    __tablename__ = 'answers'

    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text(), nullable=False)
    votes = db.Column(db.Integer)
    # created_date = db.Column(db.DateTime)
    # updated_date = db.Column(db.DateTime)