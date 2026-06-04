from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required
from hr_app.models import db, Employee, Department
from hr_app.forms import EmployeeForm

bp = Blueprint("employees", __name__, url_prefix="/employees")

@bp.route("/")
@login_required
def list():
    return render_template("employees/list.html", employees=Employee.query.all())

@bp.route("/create", methods=["GET","POST"])
@login_required
def create():
    form = EmployeeForm()
    form.department_id.choices = [(0,"---")] + [(d.id, d.name) for d in Department.query.all()]
    if form.validate_on_submit():
        dept = form.department_id.data or None
        emp = Employee(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            role=form.role.data,
            department_id=dept if dept != 0 else None
        )
        db.session.add(emp)
        db.session.commit()
        flash("Employé créé.")
        return redirect(url_for("employees.list"))
    return render_template("employees/form.html", form=form, title="Créer un employé")
