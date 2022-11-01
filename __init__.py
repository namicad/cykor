from flask import Flask, render_template

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
#        return render_template('home.html')
        return 'hello, pybo!'
    
    if __name__=='__main__':
        app.run(debug=True)

    return app