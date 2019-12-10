# Introduction to Programming
# Geometry
import math

##################################||||||||####################################


def p_ala_s(m1):
    """Returns area of square"""
    return m1**2


def p_ala_r(m1,m2):
    """Returns area of rectangle"""
    return m1*m2


def p_ala_c(m1):
    """Returns area of circle"""
    return math.pi*m1**2


def perm_r(w,l):
    """Returns perimeter of rectangle"""
    return 2*w+2*l


def perm_s(m1):
    """Returns perimeter of square"""
    return m1*4


def perm_c(r):
    """Returns perimeter of circle"""
    return 2*math.pi*r
##################################||||||||####################################


def check_values(m1):
    # Function checks if values are less or equal to zero
    if m1 <= 0:
        return False
    else:
        return True


def square():
    # Function computes area and circumference of square
    side = 0
    while True:
        side = float(input("Enter the length of the square's side: "))
        if check_values(side):
            break
    return p_ala_s(side), perm_s(side)


def rectangle():
    # Function computes area and circumference of rectangle
    side1=-1
    side2=-1
    while True:
        side1 = float(input("Enter the length of the rectangle's side 1: "))
        if check_values(side1):
            break
    while True:
        side2 = float(input("Enter the length of the rectangle's side 2: "))
        if check_values(side2):
            break
    return p_ala_r(side1,side2), perm_r(side1,side2)


def circle():
    # Function computes area and circumference of circle
    r = -1
    while True:
        radius = float(input("Enter the circle's radius: "))
        if check_values(radius):
            break
    return p_ala_c(radius), perm_c(radius)


def ret_func(area, circumference):
    # Function prints out area and circumference
    print("The total circumference is {:2.2f}".format(circumference))
    print("The surface area is {:2.2f}".format(area))


def menu():
    while True:
        answer = input("Enter the pattern's first letter, q stops this (s/r/q): ")
        if answer == "s":
            a,c = square()
            ret_func(a,c)

        elif answer == "r":
            a,c = rectangle()
            ret_func(a,c)

        elif answer == "c":
            a,c = circle()
            ret_func(a,c)

        elif answer == "q":
            return

        else:
            print("Incorrect entry, try again!")

        print()  # Empty row for the sake of readability


def main():
    menu()
    print("Goodbye!")


main()