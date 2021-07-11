from graphene_django import DjangoObjectType
import graphene

from itzhak.data.models.user import User


class UserType(DjangoObjectType):
    class Meta:
        model = User


class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    user = graphene.Field(UserType, id=graphene.ID())

    def resolve_users(self, info):
        return User.objects.all()

    def resolve_user(root, info, id):
        return User.objects.get(id=id)


schema = graphene.Schema(query=Query)
