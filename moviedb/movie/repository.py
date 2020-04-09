import aiohttp
from starlette.authentication import requires
from starlette.requests import Request
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
    @requires("authenticated")
    async def search(
        request: Request,
        title: str,
        mtype: MovieType = None,
        year: str = None,
        page: int = 1,
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
    @requires("authenticated")
    async def fetch(
        request: Request,
        imdbid: int = None,
        title: str = None,
        mtype: MovieType = None,
        year: str = None,
        plot: PlotType = None,
    ) -> MovieFetchDataclass:
        if not imdbid and not title:
            return MovieFetchDataclass(
                errors=[
                    {
                        "field": "imbdid",
                        "message": "One of (imbdid, title) arguments is required",
                    },
                ],
            )
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

            if content["Response"] == "False":
                movie = None
                errors = [ERRORS_MAPPER[content["Error"]]]
            else:
                content = convert_result_keys(content)
                movie = MovieDataclass(**content)
                errors = []

        return MovieFetchDataclass(movie=movie, errors=errors)
