from promise import Promise
from promise.dataloader import DataLoader

import graphene

class UserLoader(DataLoader):
    def batch_load_fn1(self, keys):
        # Here I return a promise that will result on the
        # corresponding user for each key in keys
        return Promise.resolve(['get_user(id=key)' for key in keys]) # temporary solution with string, necessary to solve

user_loader = UserLoader()
user_loader.load(1).then(lambda user: user_loader.load(user.best_friend_id))
user_loader.load(2).then(lambda user: user_loader.load(user.best_friend_id))

class User(graphene.ObjectType):
    name = graphene.String()
    best_friend = graphene.Field(lambda: User)
    friends = graphene.List(lambda: User)

    def resolve_best_friend(self, info):
        return user_loader.load('self.best_friend_id') # temporary solution with string, necessary to solve

    def resolve_friends(self, info):
        return user_loader.load_many('self.friend_ids') # temporary solution with string, necessary to solve
