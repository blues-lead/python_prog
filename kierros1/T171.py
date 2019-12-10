def main():
    text="A suitable smiley would be ";
    feel=input("How do you feel? (1-10) ")
    if 2 <= int(feel) <= 7:
        if int(feel) < 4:
            print(text,":-(")
        else:
            print(text+":-|")
    elif 7 < int(feel) <= 9:
        print(text+":-)")
    elif int(feel)==1:
        print(text,":'(")
    elif int(feel)==10:
        print(text,":-D")
    else:
        print("Bad input!")

main()