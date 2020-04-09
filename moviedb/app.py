from ariadne.asgi import GraphQL
from starlette.applications import Starlette

from . import settings
from .movie.database import db
from .schema import schema

routes = []

app = Starlette(debug=settings.DEBUG, routes=routes)
app.mount("/graphql", GraphQL(schema, debug=True))

# Connect database to Starlette app
db.init_app(app)
