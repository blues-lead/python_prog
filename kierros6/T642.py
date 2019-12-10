def create_an_acronym(_str):
    words = _str.split(" ")
    acro = ""
    for w in words:
        acro += w[0].upper()
    # print(acro)
    return acro