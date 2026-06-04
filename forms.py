from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, DateField, IntegerField, FileField, SubmitField
from wtforms.validators import DataRequired, Email, Length, Optional, NumberRange

class DepartmentForm(FlaskForm):
    name = StringField("Nom du département", validators=[DataRequired()])
    submit = SubmitField("Enregistrer")

class EmployeeForm(FlaskForm):
    first_name = StringField("Prénom", validators=[DataRequired()])
    last_name = StringField("Nom", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    role = SelectField("Rôle", choices=[("EMPLOYEE","Employé"),("MANAGER","Manager"),("ADMIN","Admin")])
    department_id = SelectField("Département", coerce=int)
    submit = SubmitField("Enregistrer")

class LeaveForm(FlaskForm):
    employee_id = SelectField("Employé", coerce=int)
    start_date = DateField("Début", validators=[DataRequired()])
    end_date = DateField("Fin", validators=[DataRequired()])
    status = SelectField("Statut", choices=[("PENDING","En attente"),("APPROVED","Approuvé"),("REJECTED","Rejeté")])
    reason = TextAreaField("Raison")
    submit = SubmitField("Enregistrer")

class AbsenceForm(FlaskForm):
    employee_id = SelectField("Employé", coerce=int)
    date = DateField("Date", validators=[DataRequired()])
    reason = TextAreaField("Raison")
    submit = SubmitField("Enregistrer")

class ReviewForm(FlaskForm):
    employee_id = SelectField("Employé", coerce=int)
    score = IntegerField("Score", validators=[DataRequired(), NumberRange(min=1,max=10)])
    comments = TextAreaField("Commentaires")
    submit = SubmitField("Enregistrer")

class DocumentForm(FlaskForm):
    employee_id = SelectField("Employé", coerce=int)
    file = FileField("Fichier")
    submit = SubmitField("Uploader")
