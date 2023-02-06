def catAndMouse(x, y, z):
    if abs(x-z) > abs(y-z):
        return "Cat B"
    elif abs(y-z) > abs(x-z):
        return "Cat A"
    else:
        return "Mouse C"