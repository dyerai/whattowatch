# This is a sample Python script.
import tmdbsimple as tmdb
tmdb.API_KEY = '73972aa479b5ec8c31a15ff73eba8ef3'
# from flask import Flask

# app = Flask(__name__)


# @app.route('/')


discover = tmdb.Discover()
genreChoices = tmdb.Genres().movie_list()['genres']
formattedChoices = []
for g in genreChoices:
    formattedChoices.append((tuple((g['id'], g['name']))))
print(formattedChoices)