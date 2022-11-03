from flask import Blueprint, url_for, render_template, request, session, flash
from werkzeug.security import generate_password_hash
from werkzeug.utils import redirect

from . import mod_dbconn

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        id = request.form['id']
        pw = request.form['pw']

        if(mod_dbconn.check_id((id,pw)) == 2):
            session['userId'] = id
            flash("login success!")
            return redirect(url_for('main.index'))
    
        else:
            flash("login failed!")

    return render_template('auth/login.html')

@bp.route('/register', methods=('GET','POST'))
def register():
    if request.method == 'POST':
        id = request.form['id']
        pw = request.form['pw']

        if(mod_dbconn.check_id((id,pw))==0):
            if(mod_dbconn.reg((id,pw))):
                flash("register success!")
                return render_template('auth/login.html')

        else:
            flash("register failed!")
    return render_template('auth/register.html')

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('main.index'))