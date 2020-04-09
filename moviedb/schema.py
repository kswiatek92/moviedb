import os
from typing import List

from ariadne import (
    SchemaBindable,
    load_schema_from_path,
    make_executable_schema,
    snake_case_fallback_resolvers,
)

from .movie.resolvers import query

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCHEMA_DIR = os.path.join(BASE_DIR, "schema")


type_defs = load_schema_from_path(SCHEMA_DIR)


schema_types: List[SchemaBindable] = []
schema_types += [query, snake_case_fallback_resolvers]

schema = make_executable_schema(type_defs, schema_types)
