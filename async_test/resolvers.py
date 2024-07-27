from .models import *
from asgiref.sync import sync_to_async


async def get_books():
    return [
        Book(
            title="The Great Gatsby",
            author="F. Scott Fitzgerald",
        ),
    ]
