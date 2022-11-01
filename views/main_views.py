# from flask import Blueprint, url_for
# from werkzeug.utils import redirect


# bp = Blueprint('main', __name__, url_prefix='/')


# @bp.route('/hello')
# def hello_pybo():
#     return 'Hello, Pybo!'


# @bp.route('/')
# def index():
#     #return redirect(url_for('question._list'))
#     return redirect(url_for('home'))

from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'


@bp.route('/')
def index():
    from .mod_dbconn import data_list
    
    print(data_list[0])
    print(data_list[1])
    print(data_list[2])
    return render_template('home.html', post_list=data_list)