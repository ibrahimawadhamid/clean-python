def perform_string_concatination():
    """Prefer join instead of in-place string concatination"""
    first_name = "John"
    last_name = "Smith"
    print(" ".join([first_name, last_name]))

def use_starts_ends_with():
    """Prefer using startswith and endswith"""
    greeting = "Hello, How are you doing?"
    if greeting.startswith("Hello"):
        print("It starts with Hello")
    if greeting.endswith("?"):
        print("It ends with a '?'")

perform_string_concatination()
use_starts_ends_with()