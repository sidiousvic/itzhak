from django.core.checks import messages
from graphene.types import mutation
from graphene.types.scalars import String
from graphene_django import DjangoObjectType
import graphene

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

    def mutate(root, info, id):
        user = User.objects.get(id=id)
        # delete user here
        # verify that the user was deleted
        message = "USER SUCCESSFULLY DELETED"
        return DeleteUserMutation(user, message)


class Mutation(graphene.ObjectType):
    delete_user = DeleteUserMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
