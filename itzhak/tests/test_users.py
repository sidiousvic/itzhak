import json
from json.encoder import JSONEncoder
from django.db.models import query
import pytest
from django.test import TestCase, client
from graphql.error import GraphQLLocatedError
from mixer.backend.django import mixer
from graphene.test import Client
import graphene

from itzhak.data.models.user import User
from itzhak.io.schema import AddUserInputType, AddUserMutation, DeleteUserMutation, Query, UserType, schema

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


add_user_mutation = """
    mutation($input: AddUserInputType!) {
        addUser(input: $input) {
            user {
                id
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
        # print(test_user.id)
        response = self.client.execute(
            delete_user_mutation, variables={"id": test_user.id}
        )

        print(response)
        delete_user_mutation_response = response.get("data").get("deleteUser")
        assert delete_user_mutation_response["message"] == "USER SUCCESSFULLY DELETED"
        assert delete_user_mutation_response["user"]["id"] == str(test_user.id)

    # from graphql.error.located_error import GraphQLLocatedError
    def test_delete_user_mutation_fail(self):
        non_existing_user_id = 1

        response = self.client.execute(delete_user_mutation, variables={"id": non_existing_user_id})

        print(response)

        if response['errors']:
            for error in response['errors']:
                if error['message'] =='User matching query does not exist.':
                    print('Please enter a valid user ID')

            print(response['errors'])
        else:
            delete_user_mutation_response = response.get("data").get("deleteUser")
            assert delete_user_mutation_response["message"] == "USER DELETION FAILED"


    def test_add_user_mutation(self):
        # schema=graphene.Schema(types=[AddUserInputType])
        # print(schema)
        # test_user = mixer.blend(User)
        # schema=graphene.Schema(query=Query, mutation=DeleteUserMutation)
        # response=schema.execute(delete_user_mutation,variables={"id":test_user.id})

        # sch
        # my_schema=graphene.Schema(types=[AddUserInputType],mutation=AddUserMutation)

        # self.client=Client(my_schema)
        # print(response)
        inputs=AddUserInputType()

        inputs.email="papa@gmail.com"
        inputs.first_name="Papa"
        inputs.last_name="Jones"

        response=self.client.execute(
            add_user_mutation,
            variables={"input":inputs}
        )
        assert response['message']== "user successfully added"
        # print(response)
