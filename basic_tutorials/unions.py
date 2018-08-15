import graphene

class Human(graphene.ObjectType):
    name = graphene.String()
    born_in = graphene.String()

class Droid(graphene.ObjectType):
    name = graphene.String()
    primary_function = graphene.String()

class Starship(graphene.ObjectType):
    name = graphene.String()
    length = graphene.Int()

class SearchResult(graphene.Union):
    class Meta:
        types = (Human, Droid, Starship)

'''
Representation in Schema:

type Droid {
  name: String
  primaryFunction: String
}

type Human {
  name: String
  bornIn: String
}

type Ship {
  name: String
  length: Int
}

union SearchResult = Human | Droid | Starship
'''
