import logging
import copy

from django.core.checks import messages
from graphene.types import mutation
from graphene.types.scalars import String
from graphene_django import DjangoObjectType
import graphene
from graphql.error.located_error import GraphQLLocatedError
from itzhak.data.models.user import User


class UserType(DjangoObjectType):
    class Meta:
        model = User


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
        # try:
        user = User.objects.get(id=id)
        # except GraphQLLocatedError as err:
        #     print(err)
        #     message = "USER DELETION FAILED AS NO SUCH USER EXISTS"
        #     return DeleteUserMutation(graphene.Field(UserType,id=1), message)

        user_deleted = copy.deepcopy(user)

        # delete user here
        user_deletion = user.delete()
        print(user_deletion)
        # verify that the user was deleted
        if user_deletion[1]:
            message = "USER SUCCESSFULLY DELETED"
            return DeleteUserMutation(user_deleted, message)
        # try to test deletion for a non-existing user
        else:
            message = "USER DELETION FAILED"
            return DeleteUserMutation(user, message)


class Mutation(graphene.ObjectType):
    delete_user = DeleteUserMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
