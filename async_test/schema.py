import typing
import strawberry
from gqlauth.core.middlewares import JwtSchema
from .resolvers import *
from .permissions import *


@strawberry.type
class Book:
    title: str
    author: str


@strawberry.type
class Query:
    books: typing.List[Book] = strawberry.field(resolver=get_books, permission_classes=[TestPermission])


schema = JwtSchema(query=Query)
test_schema = strawberry.Schema(query=Query)