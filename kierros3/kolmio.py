# Johdatus ohjelmointiin
# Introduction to programming
# Area


from math import sqrt


def area(s1, s2, s3):
    s=(float(s1)+float(s2)+float(s3))/2
    return sqrt(s*(s-float(s1))*(s-float(s2))*(s-float(s3)))

def main():
    line1 = input("Enter the length of the first side: ")
    line2 = input("Enter the length of the second side: ")
    line3 = input("Enter the length of the third side: ")

    print("The triangle's area is {:.1f} ".format( area(line1,line2,line3)))
    

main()
