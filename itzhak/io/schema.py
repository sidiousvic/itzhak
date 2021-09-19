import json
import logging
import copy
from django.core.checks import messages
from django.db import models
from graphene.types import mutation, Scalar
from graphene.types.generic import GenericScalar
from graphene.types.scalars import String
from graphene_django import DjangoObjectType
import graphene
from graphene import ObjectType, InputObjectType, InputField, JSONString
from graphql.error.located_error import GraphQLLocatedError
from itzhak.data.models.user import User
from json import JSONEncoder


class UserType(DjangoObjectType):
    class Meta:
        model = User


#
class AddUserInputType(InputObjectType):
    email = String(required=True)
    first_name = String(required=True)
    last_name = String(required=True)


#         return {"email":self.email}
# return {k: v
# for k, v in vars(self).items() if not str(k).startswith('_')}

# class Meta:
# model=User

# email = graphene.Field(graphene.String(required=True))
# first_name = graphene.Field(graphene.String(required=True))
# last_name = graphene.Field(graphene.String(required=True))
# print(email)

class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    user = graphene.Field(UserType, id=graphene.ID())

    def resolve_users(root, info):
        return User.objects.all()

    def resolve_user(root, info, id):
        return User.objects.get(id=id)


class DeleteUserMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    user = graphene.Field(UserType)
    message = graphene.String()

    @classmethod
    def mutate(cls, root, info, id):
        user = User.objects.get(id=id)
        user_deleted = copy.deepcopy(user)

        user_deletion = user.delete()

        if user_deletion[1]:
            message = "USER SUCCESSFULLY DELETED"
            return DeleteUserMutation(user_deleted, message)
        else:
            message = "USER DELETION FAILED"
            return DeleteUserMutation(user, message)


class AddUserMutation(graphene.Mutation):
    class Arguments:
        input = graphene.Argument(AddUserInputType)

    user = graphene.Field(UserType)
    message = graphene.String()

    @classmethod
    def mutate(cls, root, info, input: AddUserInputType):
        user = graphene.Field(UserType, email=input.email, first_name=input.first_name, last_name=input.last_name)
        user.save()

        message = "user successfully added"

        return AddUserMutation(user, message)


class Mutation(graphene.ObjectType):
    delete_user = DeleteUserMutation.Field()
    add_user = AddUserMutation.Field()


schema = graphene.Schema(query=Query, types=[AddUserInputType], mutation=Mutation)
