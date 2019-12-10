def factorial(num):
    """Recursive function. Returns factorial"""
    if num==0:
        return 1
    return num*factorial(num-1)


def probability(t,d):
    """
    Function counts all possible permutations.
    :param t: Total number of balls
    :param d: Number of balls drawn
    :return: Number of permutations
    """
    if t < 0 or d < 0:
        return -1
    elif t < d:
        return -2
    else:
        return factorial(t)/(factorial(t-d)*factorial(d))


def main():
    tot = int(input("Enter the total number of lottery balls: "))
    drawn = int(input("Enter the number of the drawn balls: "))
    res = probability(tot,drawn)
    if res == -1:
        print("The number of balls must be a positive number.")
        return
    elif res == -2:
        print("At most the total number of balls can be drawn.")
        return
    print("The probability of guessing all {:1d} balls correctly is 1/{:1.0f}".format(drawn,res))


main()

