import graphene

import cookbook.ingredients.schema
import cookbook.inventory.schema

class Query(cookbook.ingredients.schema.Query, cookbook.inventory.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
