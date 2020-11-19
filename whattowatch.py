# This is a sample Python script.
import tmdbsimple as tmdb
tmdb.API_KEY = '73972aa479b5ec8c31a15ff73eba8ef3'
# from flask import Flask

# app = Flask(__name__)



discover = tmdb.Discover()
genre = tmdb.Genres()
movies = discover.movie(sort_by='vote_average', vote_count_gte=1000)['results']
config = tmdb.Configuration()
print(discover.movie()['results'])

