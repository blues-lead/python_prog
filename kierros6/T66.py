def count_abbas(rivi):
    ind = 4
    i = 0
    counter = 0
    while ind <= len(rivi):
        if rivi[i:ind] == "abba":
            counter += 1
        ind += 1
        i += 1
    return counter