from ariadne import ObjectType

from ..movie.exceptions import DoesNotExist
from .repository import MovieRepository

query = ObjectType("Query")


@query.field("movieSearch")
async def resolve_movie_search(*_, title, mtype=None, year=None, page=1):
    return await MovieRepository.search(title, mtype, year, page)


@query.field("movieFetch")
async def resolve_movie_fetch(
    *_, imdbid=None, title=None, mtype=None, year=None, plot=None
):
    if not imdbid and not title:
        return {
            "movie": None,
            "errors": [
                {
                    "field": "imbdid",
                    "message": "One of (imbdid, title) arguments is required",
                },
            ],
        }

    try:
        return await MovieRepository.fetch(imdbid, title, mtype, year, plot)
    except DoesNotExist:
        return None
