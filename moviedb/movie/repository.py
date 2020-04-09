import aiohttp
from .. import settings
from ..movie.base_repository import BaseRepository
from . import (
    MovieDataclass, MovieType
)


def convert_result_keys(received_dict):
    return {k.lower(): v for k, v in received_dict.items()}


class MovieRepository(BaseRepository):
    @staticmethod
    async def search(title: str, mtype: MovieType = None, year: str = None, page: int = 1) -> MovieDataclass:
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
            result = [convert_result_keys(record) for record in content["Search"]]

        return [MovieDataclass(**record) for record in result]

