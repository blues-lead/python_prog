def print_in_accordance_of_values(dct):
    for z in sorted(dct, key = lambda x: dct[x]):
        print(dct[z],z)