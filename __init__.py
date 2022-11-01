from flask import Flask

app = Flask(__name__)

from .views import main_views, question_views, answer_views, auth_views

app.register_blueprint(main_views.bp)
# app.register_blueprint(question_views.bp)
# app.register_blueprint(answer_views.bp)
# app.register_blueprint(auth_views.bp)

app.run(debug=True)