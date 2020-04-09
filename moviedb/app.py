from ariadne.asgi import GraphQL
from starlette.applications import Starlette

from . import settings
from .movie.database import db
from .schema import schema
from .middleware import middleware

routes = []

app = Starlette(debug=settings.DEBUG, routes=routes, middleware=middleware)
app.mount("/graphql", GraphQL(schema, debug=True))

# Connect database to Starlette app
db.init_app(app)
