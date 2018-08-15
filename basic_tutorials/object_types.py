import graphene

class Person(graphene.ObjectType):
    first_name = graphene.String()
    last_name = graphene.String()
    full_name = graphene.String()

    def resolve_full_name(self, info):
        return "{} {}".format(self.first_name, self.last_name)
