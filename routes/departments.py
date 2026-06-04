from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required
from hr_app.models import db, Department
from hr_app.forms import DepartmentForm

bp = Blueprint("departments", __name__, url_prefix="/departments")

@bp.route("/")
@login_required
def list():
    return render_template("departments/list.html", departments=Department.query.all())

@bp.route("/create", methods=["GET","POST"])
@login_required
def create():
    form = DepartmentForm()
    if form.validate_on_submit():
        db.session.add(Department(name=form.name.data))
        db.session.commit()
        flash("Département créé.")
        return redirect(url_for("departments.list"))
    return render_template("departments/form.html", form=form, title="Créer un département")
