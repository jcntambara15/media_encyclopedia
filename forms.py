from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
<<<<<<< HEAD
    search_input = StringField('What genre of media would you like to see? (Music, Sports, Movies, TV Shows',
                           validators=[DataRequired(), Length(min=2, max=10)])
    submit = SubmitField('Enter')
=======
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class SignInForm(FlaskForm):
    pass
>>>>>>> e28889e8d33f21c71c421397d7723eeb9d3ca4c5
