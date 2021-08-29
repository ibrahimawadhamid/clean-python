import pprint
from collections import defaultdict, OrderedDict


pp = pprint.PrettyPrinter(indent=4)

def use_default_dict():
    """defaultdict doesn't raise KeyError like dict"""
    color = defaultdict(lambda: "#000000")
    color["White"] = "#FFFFFF"
    pp.pprint(color["White"])
    pp.pprint(color["Red"])

def use_ordered_dict():
    """In pthon 3.6+ dict also acts like ordereddict"""
    colors = OrderedDict()
    colors["red"] = "RED"
    colors["blue"] = "BLUE"
    colors["orange"] = "ORANGE"
    pp.pprint(colors.items())

def first(amount):
    return amount+1

def second(amount):
    return amount+2

def third(amount):
    return amount+3

def switch_using_dict():
    my_calculator = {
        "first": first,
        "second": second,
        "third": third
    }
    pp.pprint(my_calculator["first"](1))

def merge_dictionaries():
    salary_first = {"Albert": 3000, "Lisa": 4000}
    salary_second = {"Josh": 5000, "John": 2500}
    pp.pprint({**salary_first, **salary_second})

use_default_dict()
use_ordered_dict()
switch_using_dict()
merge_dictionaries()