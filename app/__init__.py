from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def creat_app():

    app = Flask(__name__)

    app.config["SECRET_KEY"] = "my_secret_key" #creating secret key for session
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db" #telling sqlalchemy where to store database
    app.config["DATABASE_TRACK_MODIFICATION"] = False #telling sqlalchemy don't track all the modifications
    app.config["UPLOAD_FOLDER"] = "app/static/images" # where to store image

    db.__init__(app) #connecting db with app

    from models import UserInfo, Posts

    with app.app_context(): #telling flask which app is activate currently
        db.create_all() #create all the model tables in database


    from app.routes.auths import auth_bp
    from app.routes.tasks import task_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(task_bp)

    return app


