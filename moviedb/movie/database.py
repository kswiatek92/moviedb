from gino.ext.starlette import Gino

from ..settings import DB_URL

db = Gino(dsn=DB_URL)
