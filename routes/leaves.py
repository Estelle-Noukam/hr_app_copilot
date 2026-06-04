from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required
from hr_app.models import db, Leave, Employee
from hr_app.forms import LeaveForm

bp = Blueprint("leaves", __name__, url_prefix="/leaves")

@bp.route("/")
@login_required
def list():
    return render_template("leaves/list.html", leaves=Leave.query.all())

@bp.route("/create", methods=["GET","POST"])
@login_required
def create():
    form = LeaveForm()
    form.employee_id.choices = [(e.id, e.email) for e in Employee.query.all()]
    if form.validate_on_submit():
        leave = Leave(
            employee_id=form.employee_id.data,
            start_date=form.start_date.data,
            end_date=form.end_date.data,
            status=form.status.data,
            reason=form.reason.data
        )
        db.session.add(leave)
        db.session.commit()
        flash("Congé créé.")
        return redirect(url_for("leaves.list"))
    return render_template("leaves/form.html", form=form, title="Créer un congé")
