from flask import Blueprint, render_template, url_for, request, flash, redirect, session, jsonify, current_app
from flask_login import current_user, login_required
from ..qadoor_db import db
from .models import Questions, Answers
import json

PER_PAGE = 20
question = Blueprint('question', __name__, url_prefix='')

@question.route('/', methods=['GET'])
@question.route('/<int:page>', methods=['GET'])
def question_index(page=1):
    paginate = Questions.query.filter(Questions.id).paginate(page, PER_PAGE)
    print(paginate.items[0].title)
    return render_template('index.html', questions=paginate.items, pagination=paginate)
    # return render_template('index.html')
    # return render_template('question.html', duty_list=todo_list)

@question.route('/search/', methods=['GET', 'POST'])
@question.route('/search/<string:keyword>/', methods=['GET', 'POST'])
@question.route('/search/<string:keyword>/<int:page>', methods=['GET', 'POST'])
def question_search(keyword='', page=1):
    # keyword = request.form['key']
    # keyword = request.form['key']
    print(keyword)
    paginate = Questions.query.filter(Questions.title.like('%' + keyword + '%')).paginate(page, PER_PAGE)
    return render_template('index.html', questions=paginate.items, pagination=paginate)

@question.route('/tag/<string:tag>/', methods=['GET'])
@question.route('/tag/<string:tag>/<int:page>', methods=['GET'])
def question_tag(tag, page=1):
    paginate = Questions.query.filter(Questions.tags.like('%'+tag+'%')).paginate(page, PER_PAGE)
    return render_template('index.html', questions=paginate.items, pagination=paginate)

@question.route('/detail/<question_id>', methods=['GET'])
def question_detail(question_id):
    question = Questions.query.filter(Questions.question_id==question_id).one()
    print(question.content)
    answer = Answers.query.filter(Answers.question_id == question_id).one()
    print(answer.content)
    return render_template('question_detail.html',
                           question=question,
                           answer=answer)
