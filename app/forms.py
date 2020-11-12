from flask_wtf import FlaskForm
from wtforms import SubmitField, RadioField, SelectField
from wtforms.validators import DataRequired
import tmdbsimple as tmdb
import datetime
tmdb.API_KEY = '73972aa479b5ec8c31a15ff73eba8ef3'


class MovieForm(FlaskForm):
    genreChoices = list(tmdb.Genres().movie_list()['genres'])
    formattedGenres = []
    formattedYears = []

    # format the genre choices to a list of tuples in order to have RadioField accept it
    for g in genreChoices:
        formattedGenres.append((tuple((g['id'], g['name']))))

    now = datetime.datetime.now()
    for i in reversed(range(1985, now.year + 1)):
        formattedYears.append((tuple((i, str(i)))))

    genre = RadioField('Genres', choices=formattedGenres)
    startYear = SelectField('From', choices=formattedYears)
    endYear = SelectField('to', choices=formattedYears)
    submit = SubmitField('Search!')