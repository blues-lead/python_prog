# TIE-02100 Johdatus ohjelmointiin
# Koodipohja laulu c, Yogi Bear


def repeat_name(name,count):
    for i in range(1,count+1):
        print("{:s}, {:s} Bear".format(name,name))

def verse(vrs,name):
    print(vrs)
    print("{:s}, {:s}".format(name,name))
    print(vrs)
    repeat_name(name,3)
    print(vrs)
    repeat_name(name,1)
    print()


def main():
    verse("I know someone you don't know", "Yogi")
    verse("Yogi has a best friend too", "Boo Boo")
    verse("Yogi has a sweet girlfriend", "Cindy")

main()
