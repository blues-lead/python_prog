# TIE-02100 Johdatus ohjelmointiin
# TIE-02106 Introduction to Programming
# Template for task: ruutu
def print_box(leveys, korkeus, merkki):
    leveys=int(leveys)
    korkeus=int(korkeus)
    for i in range(1,korkeus+1):
        print(str(merkki)*leveys)

def main():
    width = input("Enter the width of a frame: ")
    height = input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")

    print_box(width, height, mark)


main()
