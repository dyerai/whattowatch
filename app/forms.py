from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class MovieForm(FlaskForm):
    movieTitle = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Search!')