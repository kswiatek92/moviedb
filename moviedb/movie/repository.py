import aiohttp
from .. import settings
from ..movie.base_repository import BaseRepository
from . import (
    MovieDataclass,
    MovieType,
    PlotType,
    MovieFetchDataclass,
    MovieSearchDataclass,
)

ERRORS_MAPPER = {
    "Something went wrong.": {"field": "unknown", "message": "Something went wrong."},
    "Incorrect IMDb ID.": {"field": "imbdid", "message": "Incorrect IMDb ID."},
}


def convert_result_keys(received_dict):
    return {k.lower(): v for k, v in received_dict.items()}


class MovieRepository(BaseRepository):
    @staticmethod
    async def search(
        title: str, mtype: MovieType = None, year: str = None, page: int = 1
    ) -> MovieSearchDataclass:
        params = {
            "apikey": settings.OMDBAPI_KEY,
            "s": title,
        }
        if mtype:
            params["type"] = mtype
        if year:
            params["year"] = year
        if page:
            params["page"] = page

        async with aiohttp.ClientSession() as session:
            response = await session.get(url=settings.OMDBAPI_URL, params=params)
            response.raise_for_status()
            content = await response.json()

            if content["Response"] == "False":
                movies = []
                errors = [ERRORS_MAPPER[content["Error"]]]
            else:
                result = [convert_result_keys(record) for record in content["Search"]]
                movies = [MovieDataclass(**record) for record in result]
                errors = []

        return MovieSearchDataclass(movies=movies, errors=errors)

    @staticmethod
    async def fetch(
        imdbid: int = None,
        title: str = None,
        mtype: MovieType = None,
        year: str = None,
        plot: PlotType = None,
    ) -> MovieFetchDataclass:
        params = {
            "apikey": settings.OMDBAPI_KEY,
        }
        if imdbid:
            params["imdbid"] = imdbid
        if title:
            params["title"] = title
        if mtype:
            params["mtype"] = mtype
        if year:
            params["year"] = year
        if plot:
            params["plot"] = plot

        async with aiohttp.ClientSession() as session:
            response = await session.get(url=settings.OMDBAPI_URL, params=params)
            response.raise_for_status()
            content = await response.json()
            print(content)
            print(content)

            if content["Response"] == "False":
                movie = None
                errors = [ERRORS_MAPPER[content["Error"]]]
            else:
                content = convert_result_keys(content)
                movie = MovieDataclass(**content)
                errors = []

        return MovieFetchDataclass(movie=movie, errors=errors)
