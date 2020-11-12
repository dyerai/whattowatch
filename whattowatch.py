# This is a sample Python script.
import omdb
from flask import Flask

app = Flask(__name__)


@app.route('/')
def main():
    API_KEY = "db933240"
    omdb.set_default('apikey', API_KEY)
    omdb.set_default('tomatoes', True)

    movie = omdb.search("The hangover")

    return movie[0]['title']
