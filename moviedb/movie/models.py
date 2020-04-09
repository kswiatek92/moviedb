from sqlalchemy.dialects.postgresql import JSON

from ..movie.database import db


class Movie(db.Model):
    __tablename__ = "movies"

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    year = db.Column(db.String(4), nullable=False)
    rated = db.Column(db.String(7), nullable=True)
    released = db.Column(db.String(15), nullable=True)
    runtime = db.Column(db.String(10), nullable=True)
    genre = db.Column(db.String(50), nullable=True)
    director = db.Column(db.String(50), nullable=True)
    writer = db.Column(db.String(200), nullable=True)
    actors = db.Column(db.String(200), nullable=True)
    plot = db.Column(db.String(200), nullable=True)
    language = db.Column(db.String(20), nullable=True)
    country = db.Column(db.String(50), nullable=True)
    awards = db.Column(db.String(200), nullable=True)
    poster = db.Column(db.String(200), nullable=True)
    ratings = db.Column(JSON, nullable=False)
    metascore = db.Column(db.String(50), nullable=True)
    imdbrating = db.Column(db.String(50), nullable=True)
    imdbvotes = db.Column(db.String(50), nullable=True)
    imdbid = db.Column(db.String(50), nullable=True)
    type = db.Column(db.String(50), nullable=True)
    dvd = db.Column(db.String(50), nullable=True)
    boxoffice = db.Column(db.String(50), nullable=True)
    production = db.Column(db.String(50), nullable=True)
    website = db.Column(db.String(200), nullable=True)


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
