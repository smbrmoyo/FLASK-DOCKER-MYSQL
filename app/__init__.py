from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_login import LoginManager
import pymysql

from config import config

pymysql.install_as_MySQLdb()

db = SQLAlchemy()
cors = CORS()

def create_app(target_env: str) -> Flask:
    app = Flask(__name__)
    
    app.config.from_object(config[target_env])
    config[target_env].init_app(app)

    login_manager = LoginManager(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'info'

    db.init_app(app)
    cors.init_app(app)

    def page_not_found(e):
        return jsonify({"msg": "The requested resouce is not found."})

    from app.models import User

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    from app.api import api as api_blueprint
    from app.auth import auth as auth_blueprint
    from app.ui import ui as ui_blueprint

    app.register_blueprint(api_blueprint, url_prefix="/api")
    app.register_blueprint(auth_blueprint, url_prefix="/auth")
    app.register_blueprint(ui_blueprint, url_prefix="/ui")
    app.register_error_handler(404, page_not_found)

    return app