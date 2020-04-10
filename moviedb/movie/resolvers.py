from ariadne import MutationType, ObjectType
from starlette.exceptions import HTTPException

from .repository import MovieRepository

query = ObjectType("Query")
mutation = MutationType()


@query.field("movieSearch")
async def resolve_movie_search(_, info, title, mtype=None, year=None, page=1):
    request = info.context["request"]
    try:
        return await MovieRepository.search(request, title, mtype, year, page)
    except HTTPException:
        return {
            "movies": [],
            "errors": [{"field": "unknown", "message": "Login required",},],
        }


@query.field("movieFetch")
async def resolve_movie_fetch(
    _, info, imdbid=None, title=None, mtype=None, year=None, plot=None
):
    request = info.context["request"]
    try:
        return await MovieRepository.fetch(request, imdbid, title, mtype, year, plot)
    except HTTPException:
        return {
            "movie": None,
            "errors": [{"field": "unknown", "message": "Login required",},],
        }


@mutation.field("movieSave")
def resolve_movie_save(_, info, imdbid, input):
    request = info.context["request"]
    try:
        return await MovieRepository.save(request, imdbid, input)
    except HTTPException:
        return {
            "movie": None,
            "errors": [{"field": "unknown", "message": "Login required",},],
        }
