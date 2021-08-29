from collections import namedtuple


def log_point_data():
    """Prefer to use NamedTuple to have variables names
     and for data that won't change."""
    Point = namedtuple("Point", ["x", "y", "z"])
    point = Point(x=1, y=2, z=3)
    print(point.x)
    print(point.y)
    print(point.z)

def get_user_info():
    """Use NamedTuple for returning data."""
    UserInfo = namedtuple("UserInfo", ["first_name", "last_name", "age"])
    user_info = UserInfo(first_name="John", last_name="Smith", age=30)
    return user_info

log_point_data()
print(get_user_info())