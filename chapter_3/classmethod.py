"""Create a factory pattern using classmethods."""


class User:
    def __init__(self, first_name: str, last_name: str):
        self._first_name = first_name
        self._last_name = last_name
    
    def __str__(self) -> str:
        return " ".join([self._first_name, self._last_name])
    
    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name
    
    @classmethod
    def create_using_string(cls, name_str):
        first_name, last_name = name_str.split(" ")
        user = User(first_name=first_name, last_name=last_name)
        return user
    
    @classmethod
    def create_using_json(cls, name_json):
        """Parse JSON, create user object, then return it."""
        pass

    @classmethod
    def create_using_obj(cls, user_obj):
        if isinstance(user_obj, User):
            first_name = user_obj.first_name
            last_name = user_obj.last_name
            user = User(first_name=first_name, last_name=last_name)
            return user
        else:
            raise ValueError("user_obj is not of type User")


user_1 = User.create_using_string("John Smith")
print(user_1)