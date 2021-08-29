from collections import OrderedDict

def compare_types():
    """Use isinstance() method instead of type() method for comparison.

    Use isinstance() method instead of type() method for comparison, 
    because isinstance() is true for all subclasses.
    """
    user_ages = {"Larry": 35, "John": 89, "Omar": 12}
    if isinstance(user_ages, dict):
        print("user_ages is of type dict")
    
    user_ages_updated = OrderedDict()
    user_ages_updated["Larry"] = 35
    user_ages_updated["John"] = 89
    user_ages_updated["Omar"] = 12

    if isinstance(user_ages_updated, dict):
        print("user_ages_updated is of type dict")

    if type(user_ages_updated) == dict:
        print("THIS WILL FAIL")


compare_types()