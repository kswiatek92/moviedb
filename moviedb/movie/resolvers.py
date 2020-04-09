from ariadne import ObjectType

from ..movie.exceptions import DoesNotExist
from .repository import MovieRepository

query = ObjectType("Query")


@query.field("movieSearch")
async def resolve_movie_search(*_, title, mtype=None, year=None, page=1):
    return await MovieRepository.search(title, mtype, year, page)


@query.field("movieFetch")
async def resolve_movie_fetch(*_, id):
    id = int(id)
    try:
        return await MovieRepository.fetch(id)
    except DoesNotExist:
        return None

