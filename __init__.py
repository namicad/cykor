from flask import Flask
import pymysql

app = Flask(__name__)

from views import main_views, question_views, answer_views, auth_views

app.register_blueprint(main_views.bp)
# app.register_blueprint(question_views.bp)
# app.register_blueprint(answer_views.bp)
# app.register_blueprint(auth_views.bp)

conn = pymysql.connect(host='localhost', user='root', password='password', charset='utf8')
cursor = conn.cursor() 

sql = "CREATE DATABASE developer" 

cursor.execute(sql) 

conn.commit() 
conn.close() 

app.run(debug=True)