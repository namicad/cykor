from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def index():
    from . import mod_dbconn

    data_list = mod_dbconn.board()
    return render_template('post/post_list.html', post_list=data_list)