from flask import Flask

def func():
  app = Flask(__name__)
  app.secret_key = "secret"

  from views import main_views, post_views, auth_views

  app.register_blueprint(main_views.bp)
  app.register_blueprint(post_views.bp)
  app.register_blueprint(auth_views.bp)
  
  return app
