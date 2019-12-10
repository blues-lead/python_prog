def main():
    choise1 = input("Player 1, enter your choice (R/P/S): ")
    choise2 = input("Player 2, enter your choice (R/P/S): ")
    if choise1 == "R":
        if choise2 == "P":
            print("Player 2 won!")
        elif choise2 == "S":
            print("Player 1 won!")
        else:
            print("It's a tie!")
    elif choise1 == "S":
        if choise2=="R":
            print("Player 2 won!")
        elif choise2=="P":
            print("Player 1 won!")
        else:
            print("It's a tie!")
    elif choise1 == "P":
        if choise2 == "S":
            print("Player 2 won!")
        elif choise2=="R":
            print("Player 1 won!")
        else:
            print("It's a tie!")

print("Minä haluaisin mennä yliopistoon")