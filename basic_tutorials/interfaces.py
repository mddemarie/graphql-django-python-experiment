import graphene

class Character(graphene.Interface):
    id = graphene.ID(required=True)
    name = graphene.String(required=True)
    friends = graphene.List(lambda: Character)

class Human(graphene.ObjectType):
    class Meta:
        interface = (Character, )

    starships = graphene.List('Starship') # temporary solution with Starship - class Starship is missing for reference
    home_planet = graphene.String()

class Droid(graphene.ObjectType):
    class Meta:
        interface = (Character, )

    primary_function = graphene.String()
