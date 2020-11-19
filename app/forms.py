from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField
from wtforms.validators import DataRequired
import tmdbsimple as tmdb
import datetime
tmdb.API_KEY = '73972aa479b5ec8c31a15ff73eba8ef3'


class MovieForm(FlaskForm):
    genreChoices = list(tmdb.Genres().movie_list()['genres'])
    formattedGenres = []

    # format the genre choices to a list of tuples in order to have RadioField accept it
    for g in genreChoices:
        formattedGenres.append((tuple((g['id'], g['name']))))

    genre = SelectField('Genres', choices=formattedGenres, coerce=int)
    year = SelectField('from', choices=[(0, "this year"), (5, "the past five years"), (10, "the past decade"),
                                        (20, "the past two decades")], coerce=int)
    submit = SubmitField('Search!')