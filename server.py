from flask import Flask, render_template
from datetime import datetime
import views
from database import Database
from movie import Movie


def create_app():
    app = Flask(__name__)
    app.config.from_object("settings")

    app.add_url_rule("/", view_func=views.home_page)
    app.add_url_rule("/movies", view_func=views.movies_page, methods=["GET", "POST"])
    app.add_url_rule("/movies/<int:movie_key>", view_func=views.movie_page)
    app.add_url_rule("/movies/<int:movie_key>/edit",view_func=views.movie_edit_page, methods=["GET", "POST"])
    app.add_url_rule("/new-movie", view_func=views.movie_add_page, methods=["GET", "POST"])

    db = Database()
    db.add_movie(Movie("Slaughterhouse-Five","George Roy Hill", 1972 ))
    db.add_movie(Movie("The Shining",  "Stanley Kubrick", 1980))
    db.add_movie(Movie("Star Wars: Episode IV - A New Hope",  "George Lucas", 1978))
    db.add_movie(Movie("The Fellowship of the Ring", "Peter Jackson", 2001 ))
    app.config["db"] = db

    return app



if __name__ == "__main__":
    app=create_app()
    port=app.config.get("PORT", 5000)
    app.run(host="localhost", port=port)
