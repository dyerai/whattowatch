from flask import render_template, flash, redirect
from app import app
from app.forms import MovieForm

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = MovieForm()
    if form.validate_on_submit():
        genre = MovieForm.genre
    return render_template('index.html', form=form)