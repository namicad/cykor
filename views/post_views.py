from datetime import datetime
from distutils.util import execute
from flask import Blueprint, render_template, request, url_for, session, flash
from werkzeug.utils import redirect

from . import mod_dbconn

bp = Blueprint('post', __name__, url_prefix='/post')

@bp.route('/list')
def list():

    data_list = mod_dbconn.board()
    return render_template('post/post_list.html', post_list=data_list)


@bp.route('/create/', methods=('GET', 'POST'))
def create():
    if 'userId' in session:
        if request.method == 'POST':
            # num = mod_dbconn.board_size()
            title = str(request.form['title'])
            writer = str(session['userId'])
            content = str(request.form['content'])

            mod_dbconn.board_post((title,writer,content))

            return redirect(url_for('main.index'))
            
        return render_template('post/post_form.html')#, form=form)
    
    flash("login first!")
    return render_template('auth/login.html')

@bp.route('/detail/<int:index>', methods=('GET','POST'))
def detail(index):

    edit_en = False
    data = mod_dbconn.board()[index-1]

    if request.method == 'POST':
        if 'userId' not in session:
            flash("login first!")
            return render_template('auth/login.html')
        
        if data[1] == session['userId']:
            edit_en = True

        else:
            flash("You do not have permission.")
            return redirect(url_for('post.list'))


    return render_template('post/post_detail.html', data=data, edit_en=edit_en, index=index)


@bp.route('/detail/<int:index>/<int:sw>', methods=('GET','POST'))
def change(index, sw):
    pre_data = mod_dbconn.board()[index-1]

    print(pre_data)
    if request.method == 'POST':
        #delete
        if 'userId' not in session:
            flash("login first!")
            return render_template('auth/login.html')

        if pre_data[1] == session['userId']:
            if sw==0:
                mod_dbconn.board_delete(pre_data)
                return redirect(url_for('post.list'))

            #edit
            elif sw==1:
                title = str(request.form['title'])
                content = str(request.form['content'])

                print((title, content) + pre_data)
                mod_dbconn.board_edit((title, content), pre_data)
                return redirect(url_for('post.list'))
        else :
            flash("You do not have permission.")
            return redirect(url_for('post.list'))

    else:
        return render_template('post/post_detail.html', data=pre_data, edit_en=False, index=index)