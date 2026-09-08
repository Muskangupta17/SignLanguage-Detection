from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


db = SQLAlchemy()

bcrypt = Bcrypt()

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):

    from models.user_model import User

    return User.query.get(int(user_id))