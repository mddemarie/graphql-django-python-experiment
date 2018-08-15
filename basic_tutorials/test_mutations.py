from graphene.test import Client

from mutations import schema as my_schema

def test_hey():
    client = Client(my_schema)
    executed = client.execute('''{ hey }''')
    assert executed == {
        'data': {
            'hey': 'hello world!'
        }
    }
