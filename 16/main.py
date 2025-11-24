#!/usr/bin/env python3

import json
from json import JSONEncoder 

class Animal(JSONEncoder):
    def __name__(self, name):
        self.name = name

    def default(self, obj):
        if isinstance(obj, Animal):
            return {"name": obj.name}
        return super().default(self, obj)

def main():
    
    data = '''
    {
    "username": "alex123",
    "email": "alex.new@mail.com",
    "is_premium": true,
    "favorite_colors": ["blue", "purple"],
    "settings": {"theme": "light", "notifications": false}
    }
    '''

    user_profile_pydict = json.loads(data)
    print(user_profile_pydict)
    print(type(user_profile_pydict))

    print("---")

    user_profile_json_string = json.dumps(user_profile_pydict)
    print(user_profile_json_string)
    print(type(user_profile_json_string))

    c = dict(name="cat")
    d = dict(name="dog")
    m = dict(name="mouse")
    animals = [c, d, m]

    animals_json = json.dumps(animals, cls = Animal)
    print(animals_json)

if __name__ == "__main__":
    main()