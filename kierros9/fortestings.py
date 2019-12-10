def main():
    hakemisto = {'auto': {'formula': [10], 'rekka': [[1, 5, 6]]}, 'juna': {'pendolino': [[7, 9]], 'tavarajuna': [[3, 7]]},
     'mopo': {'mopoauto': [9], 'viritetty': [37]}}
    """for type in sorted(hakemisto):
        print(type)
        for kv in sorted(hakemisto[type]):
            print(" ", kv, end=" ")
            for sivu in sorted(hakemisto[type][kv]):
                print(sivu, "")"""
    for hakusana in sorted(hakemisto):
        print(hakusana)
        for alakasite in sorted(hakemisto[hakusana]):
            print(" ", alakasite, end=" ")
            for sivu in sorted(hakemisto[hakusana][alakasite]):
                print(sivu, end=" ")
            print()


main()