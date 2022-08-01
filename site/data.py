from flask import Flask
from flask_proj import proj


db = proj()
DB_NAME = "FileD.db"


def c_app():
    app = Flask(__name__)
    app.config['SECRETKEY'] = 'password'
    app.config['web_DATA_URI'] = f'pyflask:///{DB_NAME}'
    db.init_app(app)

    from .models import User, Note

    create_data(app)

    logM = LoginManager()
    logM.login_view = 'auth.login'
    logM.init_app(app)

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Files created')
