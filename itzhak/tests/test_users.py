import pytest
from django.test import TestCase
from mixer.backend.django import mixer
from graphene.test import Client

from itzhak.data.models.user import User
from itzhak.io.schema import schema

users_query = """
    query {
        users { 
            # user query returns a User type
            id
            email
            firstName
            lastName
            balance
            currency
        }
    }
"""

user_query = """
    query($id: ID) {
        user(id: $id) {
            # user query returns a User type
            id
            email
            firstName
            lastName
            balance
          	currency
        }
    }
"""

delete_user_mutation = """
    mutation($id: ID) {
        deleteUser(id: $id) {
            user {
                id
                lastName
                firstName
            }
            message
        }        
    }
"""


@pytest.mark.django_db
class TestUserSchema(TestCase):
    def setUp(self):
        self.client = Client(schema)

    # get all users
    def test_users_query(self):
        for idx in range(3):
            mixer.blend(User)

        response = self.client.execute(users_query)
        response_users = response.get("data").get("users")
        ok = response.get("data").get("ok")
        assert len(response_users) == 3

    # get one user
    def test_user_query(self):
        test_user = mixer.blend(User)
        response = self.client.execute(user_query, variables={"id": test_user.id})
        response_user = response.get("data").get("user")
        ok = response.get("data").get("ok")
        assert response_user["id"] == str(test_user.id)

    # delete one user
    def test_delete_user_mutation(self):
        test_user = mixer.blend(User)
        response = self.client.execute(
            delete_user_mutation, variables={"id": test_user.id}
        )
        delete_user_mutation_response = response.get("data").get("deleteUser")
        assert delete_user_mutation_response["message"] == "USER SUCCESSFULLY DELETED"
        assert delete_user_mutation_response["user"]["id"] == str(test_user.id)
