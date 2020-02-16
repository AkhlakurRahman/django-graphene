import graphene
from graphene_django import DjangoObjectType

from .models import Track


class TrackType(DjangoObjectType):
    class Meta:
        model = Track


class Query(graphene.ObjectType):
    tracks = graphene.List(TrackType)

    def resolve_tracks(self, info):
        return Track.objects.all()


class CreateTrack(graphene.Mutation):
    track = graphene.Field(TrackType)

    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String()
        url = graphene.String(required=True)

    def mutate(self, info, title, description, url):
        # Getting authenticated user
        user = info.context.user or None

        if user.is_anonymous:
            raise Exception('Please login to add a track')

        track = Track(title=title, description=description,
                      url=url, created_by=user)
        track.save()

        return CreateTrack(track=track)


class Mutation(graphene.ObjectType):
    create_track = CreateTrack.Field()
