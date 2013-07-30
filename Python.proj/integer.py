def distance_from_zero(b):
    if type(b) == int or type(b) == float:
     return abs(b)
    else:
     return "Not a integer or float!"
print distance_from_zero(676)