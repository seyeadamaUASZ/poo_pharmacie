from datetime import datetime

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, IntegerField, DateTimeField
from wtforms.validators import InputRequired, Email, DataRequired, Length, EqualTo
from wtforms.fields.html5 import DateTimeLocalField, DateField


class LoginForm(FlaskForm):
    """User Login Form."""
    email = StringField(
        u'Email',
        validators=[
            DataRequired('Please enter a valid email address'),
            Email('Please enter a valid email address')
        ])
    password = PasswordField(u'Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


class RegisterForm(FlaskForm):
    """User Signup Form."""
    lastname = StringField(
        u'Lastname',
        validators=[DataRequired(message='Please enter Your lastname')])

    firstname = StringField(
        u'Firstname',
        validators=[DataRequired(message='please enter your firstname')])

    password = PasswordField(
        u'Password',
        validators=[DataRequired(message='Please enter a password.'),
                    Length(min=8, message='Please select a strong password'),
                    EqualTo('confirm', message='Passwords must match')])

    confirm = PasswordField('Confirm Your Password')

    email = StringField(
        u'Email',
        validators=[
            Length(min=6, message='please enter a valid email address.'),
            DataRequired(message='Please enter a valid email address'),
            Email(message='Please enter a valid email address')
        ])


class CategoryForm(FlaskForm):
    "Category form"
    name = StringField(
        u'Nom categorie',
        validators=[DataRequired(message="Entrer le nom de la catégorie")
                    ])
    description = StringField(
        u'Description'
    )


class MedicamentForm(FlaskForm):
    "Medicament form"
    name = StringField(
        u'Nom médicament',
        validators=[DataRequired(message="Entrer le nom du médicament")]

    )
    prixu = IntegerField(
        u'prix unitaire',
        validators=[DataRequired(message="Entrer le prix unitaire")]
    )
    quantite = IntegerField(
        u'Quantité médicament',
        validators=[DataRequired(message="Entrer la quantité")]
    )
    designation = StringField(
        u'La désignation'
    )
    category_id = StringField(
		u'category_id',
		validators=[DataRequired(message='Entrer la catégorie')])
