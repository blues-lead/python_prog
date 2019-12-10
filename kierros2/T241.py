def main():
    am=input("How many numbers would you like to have? ")
    am=int(am)
    i=1
    while i <= am:
        if i%3 ==0 and i%7 == 0:
            to_print="zip boing"
        elif i%7 == 0:
            to_print="boing"
        elif i%3 == 0:
            to_print="zip"
        else:
            to_print=i
        print(to_print)
        i+=1



main()