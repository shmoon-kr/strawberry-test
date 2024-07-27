import typing
import strawberry
from asgiref.sync import sync_to_async
from strawberry.permission import BasePermission


class TestPermission(BasePermission):
    message = "User is not authenticated"

    # This method can also be async!
    def has_permission(
        self, source: typing.Any, info: strawberry.Info, **kwargs
    ) -> bool:
        return True
