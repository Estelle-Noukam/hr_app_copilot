from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required
from hr_app.models import db, Absence, Employee
from hr_app.forms import AbsenceForm

bp = Blueprint("absences", __name__, url_prefix="/absences")

@bp.route("/")
@login_required
def list():
    return render_template("absences/list.html", absences=Absence.query.all())

@bp.route("/create", methods=["GET","POST"])
@login_required
def create():
    form = AbsenceForm()
    form.employee_id.choices = [(e.id, e.email) for e in Employee.query.all()]
    if form.validate_on_submit():
        abs_ = Absence(
            employee_id=form.employee_id.data,
            date=form.date.data,
            reason=form.reason.data
        )
        db.session.add(abs_)
        db.session.commit()
        flash("Absence créée.")
        return redirect(url_for("absences.list"))
    return render_template("absences/form.html", form=form, title="Créer une absence")
