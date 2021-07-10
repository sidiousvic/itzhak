import pytest
from django.test import TestCase
from mixer.backend.django import mixer
from graphene.test import Client

from itzhak.data.models.user import User
from itzhak.io.schema import schema

users_query = """
    query {
        users {
            id
            email
            firstName
            lastName
            balance
            currency
        }
    }
"""


@pytest.mark.django_db
class TestUserSchema(TestCase):
    def setUp(self):
        self.client = Client(schema)
        self.user = mixer.blend(User)

    def test_users_query(self):
        response = self.client.execute(users_query, variables={"id": self.user.id})
        response_users = response.get("data").get("users")
        assert len(response_users) == 1
