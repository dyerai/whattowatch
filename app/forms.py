from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, BooleanField
from wtforms.validators import DataRequired
import tmdbsimple as tmdb
import datetime
tmdb.API_KEY = '73972aa479b5ec8c31a15ff73eba8ef3'


class MovieForm(FlaskForm):
    genreChoices = list(tmdb.Genres().movie_list()['genres'])
    formattedGenres = []
    formattedYears = []
    # format the genre choices to a list of tuples in order to have SelectField accept it
    for g in genreChoices:
        formattedGenres.append((tuple((g['id'], g['name']))))
    # format the year choices to a list of tuples in order to have SelectField accept it
    for i in reversed(range(1970, 2021)):
        formattedYears.append((tuple((i, str(i)))))

    genre = SelectField('Genres', choices=formattedGenres, coerce=int)
    firstYear = SelectField('from', choices=formattedYears, coerce=int)
    lastYear = SelectField('to', choices= formattedYears, coerce=int)
    includePG = BooleanField('include movies PG and under?', default='checked')
    submit = SubmitField('Search!')