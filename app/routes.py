from flask import render_template, flash, redirect
from app import app
from app.forms import MovieForm

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = MovieForm()
    if form.validate_on_submit():
        flash('Information requested for movie {}'.format(
            form.movieTitle.data))
    return render_template('index.html', form=form)