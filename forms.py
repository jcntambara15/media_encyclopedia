from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    search_input = StringField('What genre of media would you like to see? (Music, Sports, Movies, TV Shows',
                           validators=[DataRequired(), Length(min=2, max=10)])
    submit = SubmitField('Enter')