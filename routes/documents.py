from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required
from hr_app.models import db, Document, Employee
from hr_app.forms import DocumentForm

bp = Blueprint("documents", __name__, url_prefix="/documents")

@bp.route("/")
@login_required
def list():
    return render_template("documents/list.html", documents=Document.query.all())

@bp.route("/create", methods=["GET","POST"])
@login_required
def create():
    form = DocumentForm()
    form.employee_id.choices = [(e.id, e.email) for e in Employee.query.all()]
    if form.validate_on_submit():
        filename = form.file.data.filename if form.file.data else "document.pdf"
        doc = Document(employee_id=form.employee_id.data, filename=filename)
        db.session.add(doc)
        db.session.commit()
        flash("Document ajouté.")
        return redirect(url_for("documents.list"))
    return render_template("documents/form.html", form=form, title="Ajouter un document")
