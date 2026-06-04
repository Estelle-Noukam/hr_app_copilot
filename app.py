from flask import Flask, render_template
from flask_login import current_user

from hr_app.models import (
    db,
    Department,
    Employee,
    Leave,
    Absence,
    PerformanceReview,
    Document
)

from hr_app.models_user import User
from hr_app.routes.departments import bp as departments_bp
from hr_app.routes.employees import bp as employees_bp
from hr_app.routes.leaves import bp as leaves_bp
from hr_app.routes.absences import bp as absences_bp
from hr_app.routes.reviews import bp as reviews_bp
from hr_app.routes.documents import bp as documents_bp
from flask_login import LoginManager
from hr_app.routes.auth import bp as auth_bp

import os

# Force l’import des modèles pour SQLAlchemy
models = [Department, Employee, Leave, Absence, PerformanceReview, Document, User]

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev_key")
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg://hr_user:test1234@localhost:5433/hr_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# 🔥 Les blueprints DOIVENT être enregistrés ici
app.register_blueprint(auth_bp)
app.register_blueprint(departments_bp)
app.register_blueprint(employees_bp)
app.register_blueprint(leaves_bp)
app.register_blueprint(absences_bp)
app.register_blueprint(reviews_bp)
app.register_blueprint(documents_bp)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    total_employees = Employee.query.count()
    total_departments = Department.query.count()
    pending_leaves = Leave.query.filter_by(status="PENDING").count()
    return render_template(
        "dashboard.html",
        total_employees=total_employees,
        total_departments=total_departments,
        pending_leaves=pending_leaves,
    )

if __name__ == "__main__":
    app.run(debug=True)
