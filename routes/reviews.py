from flask import Blueprint, render_template, request, redirect, url_for, flash
from hr_app.models import db, PerformanceReview, Employee

bp = Blueprint("reviews", __name__, url_prefix="/reviews")

@bp.route("/")
def list_reviews():
    reviews = PerformanceReview.query.all()
    return render_template("reviews/list.html", reviews=reviews)

@bp.route("/add", methods=["GET", "POST"])
def add_review():
    employees = Employee.query.all()

    if request.method == "POST":
        employee_id = request.form.get("employee_id")
        score = request.form.get("score")
        comments = request.form.get("comments")

        review = PerformanceReview(
            employee_id=employee_id,
            score=score,
            comments=comments
        )

        db.session.add(review)
        db.session.commit()
        flash("Évaluation ajoutée avec succès.", "success")
        return redirect(url_for("reviews.list_reviews"))

    return render_template("reviews/add.html", employees=employees)

@bp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_review(id):
    review = PerformanceReview.query.get_or_404(id)
    employees = Employee.query.all()

    if request.method == "POST":
        review.employee_id = request.form.get("employee_id")
        review.score = request.form.get("score")
        review.comments = request.form.get("comments")

        db.session.commit()
        flash("Évaluation mise à jour.", "success")
        return redirect(url_for("reviews.list_reviews"))

    return render_template("reviews/edit.html", review=review, employees=employees)

@bp.route("/delete/<int:id>", methods=["POST"])
def delete_review(id):
    review = PerformanceReview.query.get_or_404(id)
    db.session.delete(review)
    db.session.commit()
    flash("Évaluation supprimée.", "success")
    return redirect(url_for("reviews.list_reviews"))

