import pytest
from django.test import TestCase
from django.utils import timezone
from async_test.models import *
from async_test.schema import schema, test_schema

# Create your tests here.

query = '''
query MainPage {
  books {
    title
    author
  }
}
'''


class BooksTestCase(TestCase):

    @pytest.mark.asyncio
    async def test_jwt_schema(self) -> None:  # test fail
        resp = await schema.execute(query, variable_values={}, context_value={})
        assert resp.data is not None

        return

    @pytest.mark.asyncio
    async def test_strawberry_schema(self) -> None:  # test success
        resp = await test_schema.execute(query, variable_values={}, context_value={})
        assert resp.data is not None

        return
