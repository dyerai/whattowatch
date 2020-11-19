from flask import render_template, flash, redirect
from app import app
from app.forms import MovieForm
import tmdbsimple as tmdb
import datetime

year: int
yearname: str
genre: int
genrename: str


@app.route('/', methods=['GET', 'POST'])
def index():
    form = MovieForm()
    if form.validate_on_submit():
        global genre
        global year
        global genrename
        global yearname
        genre = form.genre.data
        genrename = dict(form.genre.choices).get(form.genre.data)
        year = form.year.data
        yearname = dict(form.year.choices).get(form.year.data)

        print(genre)
        print(year)
        return redirect('/list')
    return render_template('index.html', form=form)


@app.route('/list')
def list():
    form = MovieForm()
    discover = tmdb.Discover()
    global genre
    global genrename
    global year
    global yearname
    # search arguments
    formattedyear = str(datetime.datetime.now().year - year) + "-01-01"
    movies = discover.movie(with_genres=genre, primary_release_date_gte=formattedyear, sort_by='vote_average.desc',
                            vote_count_gte=500, with_original_language='en')['results']
    imgURL = tmdb.Configuration().info()['images']['base_url'] + "w154"
    return render_template('list.html', movies=movies, genre=genre, years=form.year.description,
                           imgURL=imgURL, genrename=genrename, yearname=yearname)