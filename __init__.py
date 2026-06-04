from flask import Flask
from flask_login import LoginManager
from .models import db
import os

login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev_key")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    login_manager.init_app(app)

    from .routes.departments import bp as departments_bp
    from .routes.employees import bp as employees_bp
    from .routes.leaves import bp as leaves_bp
    from .routes.absences import bp as absences_bp
    from .routes.reviews import bp as reviews_bp
    from .routes.documents import bp as documents_bp

    app.register_blueprint(departments_bp)
    app.register_blueprint(employees_bp)
    app.register_blueprint(leaves_bp)
    app.register_blueprint(absences_bp)
    app.register_blueprint(reviews_bp)
    app.register_blueprint(documents_bp)

    return app
