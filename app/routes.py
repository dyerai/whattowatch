from flask import render_template, redirect
from app import app
from app.forms import MovieForm
import tmdbsimple as tmdb
import datetime

firstYear: int
lastYear: int
genre: int
genreName: str
includePG: bool


@app.route('/', methods=['GET', 'POST'])
def index():
    form = MovieForm()
    if form.validate_on_submit():
        global genre
        global firstYear
        global lastYear
        global genrename
        global includePG
        genre = form.genre.data
        genrename = dict(form.genre.choices).get(form.genre.data)
        firstYear = form.firstYear.data
        lastYear = form.lastYear.data
        includePG = form.includePG.data

        return redirect('/list')
    return render_template('index.html', form=form)


@app.route('/list')
def list():
    form = MovieForm()
    discover = tmdb.Discover()
    global genre
    global genreName
    global firstYear
    global lastYear
    global includePG
    # search arguments
    formattedfirstyear = str(firstYear) + "-01-01"
    formattedlastyear = str(lastYear) + "-12-31"
    if includePG:
        movies = discover.movie(with_genres=genre, primary_release_date_gte=formattedfirstyear,
                                primary_release_date_lte=formattedlastyear, sort_by='vote_average.desc',
                                vote_count_gte=500, with_original_language='en')['results']
    else:
        movies = discover.movie(with_genres=genre, primary_release_date_gte=formattedfirstyear,
                                primary_release_date_lte=formattedlastyear, sort_by='vote_average.desc',
                                vote_count_gte=500, with_original_language='en', certification_country='US',
                                certification_gte='PG-13')['results']
    imgURL = tmdb.Configuration().info()['images']['base_url'] + "w154"
    return render_template('list.html', movies=movies, genre=genre, firstYear=firstYear, lastYear=lastYear,
                           imgURL=imgURL, genrename=genrename)