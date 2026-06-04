from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date

db = SQLAlchemy()

class Department(db.Model):
    __tablename__ = "department"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)

    employees = db.relationship("Employee", backref="department", lazy=True)


class Employee(db.Model):
    __tablename__ = "employee"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(50), nullable=False, default="EMPLOYEE")

    department_id = db.Column(db.Integer, db.ForeignKey("department.id"))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    leaves = db.relationship("Leave", backref="employee", lazy=True)
    absences = db.relationship("Absence", backref="employee", lazy=True)
    reviews = db.relationship("PerformanceReview", backref="employee", lazy=True)
    documents = db.relationship("Document", backref="employee", lazy=True)


class Leave(db.Model):
    __tablename__ = "leave"

    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey("employee.id"))
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(50), default="PENDING")
    reason = db.Column(db.Text)


class Absence(db.Model):
    __tablename__ = "absence"

    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey("employee.id"))
    date = db.Column(db.Date, nullable=False)
    reason = db.Column(db.Text)


class PerformanceReview(db.Model):
    __tablename__ = "performance_review"

    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey("employee.id"))
    score = db.Column(db.Integer, nullable=False)
    comments = db.Column(db.Text)
    date = db.Column(db.Date, default=date.today)


class Document(db.Model):
    __tablename__ = "document"

    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey("employee.id"))
    filename = db.Column(db.String(255), nullable=False)
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)

