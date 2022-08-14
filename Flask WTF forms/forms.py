from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class Forms(FlaskForm):
    email = EmailField(label='Email:',
                       validators=[DataRequired('Please enter a legit email address!'),
                                   Email(message='Invalid email address')])
    password = PasswordField(label='Password',
                             validators=[DataRequired('Please enter a strong password'), Length(min=8, max=20)])
    submit = SubmitField(label='Log In')
