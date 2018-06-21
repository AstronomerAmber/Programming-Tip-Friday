#Using Python's enumerate and zip to iterate over two lists and their indices.

#enumerate- Iterate over indices and items of a list

Amber_list = ['stars','galaxies', 'quasars']

for i, a in enumerate(Amber_list):
    print i, a

#zip- Iterates over two lists in parallel
Rank = ['cool','cooler','coolest']

for a, b in zip(Amber_list, Rank):
    print a, str('='), b

for i, (a,b) in enumerate(zip(Amber_list, Rank)):
    print i, a, str('='), b
