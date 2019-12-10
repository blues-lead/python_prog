# Fill in all TODOs in this file

from math import sqrt

# This is a text-based menu. You should ONLY touch TODOs inside the menu.
# TODOs in the menu call functions that you have implemented and take care
# of the return values of the function calls.


def menu():
    tank_size = read_number("How much does the vehicle's gas tank hold? ")
    gas = tank_size  # Tank is full when we start
    gas_consumption = read_number("How many liters of gas does the car " +
                                  "consume per hundred kilometers? ")
    x = 0.0  # Current X coordinate of the car
    y = 0.0  # Current Y coordinate of the car

    while True:
        print("Coordinates x={:.1f}, y={:.1f}, "
              "the tank contains {:.1f} liters of gas.".format(x, y, gas))

        choice = input("1) Fill 2) Drive 3) Quit\n-> ")

        if choice == "1":
            to_fill = read_number("How many liters of gas to fill up? ")
            gas = fill(tank_size,to_fill,gas)

        elif choice == "2":
            new_x = read_number("x: ")
            new_y = read_number("y: ")
            gas,x,y = drive(x,y,new_x,new_y,gas,gas_consumption)

        elif choice == "3":
            break

    print("Thank you and bye!")


# This function has three parameters which are all FLOATs:
#       (1) the size of the tank
#       (2) the amount of gas that is requested to be filled in
#       (3) the amount of gas in the tank currently
#
# The parameters have to be in this order.
# The function returns one FLOAT that is the amount of gas in the
# tank AFTER the filling up.
#
# The function does not print anything and does not ask for any
# input.
def fill(size,to_fill,filled):
    if to_fill > size:
        return size
    elif to_fill+filled > size:
        return size
    else:
        return to_fill+filled


# This function has six parameters. They are all floats.
#   (1) The current x coordinate
#   (2) The current y coordinate
#   (3) The destination x coordinate
#   (4) The destination y coordinate
#   (5) The amount of gas in the tank currently
#   (6) The consumption of gas per 100 km of the car
#
# The parameters have to be in this order.
# The function returns three floats:
#   (1) The amount of gas in the tank AFTER the driving
#   (2) The reached (new) x coordinate
#   (3) The reached (new) y coordinate
#
# The return values have to be in this order.
# The function does not print anything and does not ask for any
# input.
def drive(x,y,dx,dy,gas,cons):
    # It might be usefull to make one or two helper functions to help
    # the implementation of this function (drive)
    new_x = dx
    new_y = dy
    route = calc_length(x,y,dx,dy)
    kulutettu = route*(cons/100)
    if kulutettu > gas:
        n_route = gas*(100/cons)
        scale = n_route/route
        new_x = x + (n_route*(dx - x))/route
        new_y = y + (n_route*(dy - y))/route
        gas = 0
    else:
        gas = gas - kulutettu

    return gas, new_x, new_y



# TODO
def calc_length(x,y,dx=0,dy=0):
    length1 = dx - x
    length2 = dy - y
    return sqrt(length1**2+length2**2)



# Implement your own functions here. It is required to implement at least
# two functions that take at least one parameter and return at least one
# value.
# The functions have to be used somewhere in the program.


def read_number(prompt, error_message="Incorrect input!"):

    # This function reads input from the user.
    # Do not touch this function.
    try:
        return float(input(prompt))
    except ValueError:
        print(error_message)
        return read_number(prompt, error_message)


def main():
    menu()

main()
