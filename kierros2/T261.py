def main():
    num=input("How many numbers would you like to have? ")
    to_print=""
    for i in range(1,int(num)+1):
        if i%3==0 and i%7==0:
            to_print="zip boing"
        elif i%3==0:
            to_print="zip"
        elif i%7==0:
            to_print="boing"
        else:
            to_print=i
        print(to_print)


main()