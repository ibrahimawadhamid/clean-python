def compare_with_none():
    """Consider using is and is not whenever you need to cpmare with None"""
    value = {};
    if value is not None:
        print("value is not none")
    else:
        print("value is none")

compare_with_none()