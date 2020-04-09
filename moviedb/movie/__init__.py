from enum import Enum
from dataclasses import dataclass
from typing import Optional


class MovieType(Enum):
    MOVIE="movie"
    SERIES="series"
    EPISODE="episode"


@dataclass
class MovieDataclass:
    title: str
    year: str
    imdbid: str
    id: Optional[int] = None
    rated: Optional[str] = None
    released: Optional[str] = None
    runtime: Optional[str] = None
    genre: Optional[str] = None
    director: Optional[str] = None
    writer: Optional[str] = None
    actors: Optional[str] = None
    plot: Optional[str] = None
    language: Optional[str] = None
    country: Optional[str] = None
    awards: Optional[str] = None
    poster: Optional[str] = None
    ratings: Optional[str] = None
    metascore: Optional[str] = None
    imdbrating: Optional[str] = None
    imdbvotes: Optional[str] = None
    type: Optional[str] = None
    dvd: Optional[str] = None
    boxoffice: Optional[str] = None
    production: Optional[str] = None
    website: Optional[str] = None
