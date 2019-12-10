# TIE-02100 Johdatus ohjelmointiin
# TIE-02100 Introduction to programming
# Template song b, Old MacDonald
def print_verse(animal, voice):
    print("Old MACDONALD had a farm")
    print("E-I-E-I-O")
    print("And on his farm he had a", animal)
    print("E-I-E-I-O")
    print("With a {:s} {:s} here".format(voice,voice))
    print("And a {:s} {:s} there".format(voice,voice))
    print("Here a {:s}, there a {:s}".format(voice,voice))
    print("Everywhere a {:s} {:s}".format(voice,voice))
    print("Old MacDonald had a farm")
    print("E-I-E-I-O")
    print()

def main():

    print_verse("cow", "moo")
    print_verse("pig", "oink")
    print_verse("duck", "quack")
    print_verse("horse", "neigh")
    print_verse("lamb", "baa")

main()
