import graphene

from graphene_django.types import DjangoObjectType

from .models import Family, Location, Product, Transaction

class FamilyType(DjangoObjectType):
    class Meta:
        model = Family

class LocationType(DjangoObjectType):
    class Meta:
        model = Location

class ProductType(DjangoObjectType):
    class Meta:
        model = Product

class TransactionType(DjangoObjectType):
    class Meta:
        model = Transaction

class Query(graphene.AbstractType):
    all_families = graphene.List(FamilyType)
    all_locations = graphene.List(LocationType)
    all_products = graphene.List(ProductType)
    all_transactions = graphene.List(TransactionType)

    family = graphene.Field(FamilyType, id=graphene.Int())
    location = graphene.Field(LocationType, id=graphene.Int())
    product = graphene.Field(ProductType, id=graphene.Int())
    transaction = graphene.Field(TransactionType, id=graphene.Int())

    def resolve_all_families(self, args):
        return Family.objects.all()
    
    def resolve_all_locations(self, args):
        return Location.objects.all()

    def resolve_all_products(self, args):
        return Product.objects.all()

    def resolve_all_transactions(self, args):
        return Transaction.objects.all()

    def resolve_family(self, args, id):
        return Family.objects.get(pk=id)

    def resolve_location(self, args, id):
        return Location.objects.get(pk=id)

    def resolve_product(self, args, id):
        return Product.objects.get(pk=id)

    def resolve_transaction(self, args, id):
        return Transaction.objects.get(pk=id)
