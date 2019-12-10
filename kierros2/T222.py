def main():
    ans=input("Answer Y or N: ")
    while (ans!="Y" and ans!="y") and (ans!="N" and ans!="n"):
        print("Incorrect entry.")
        ans=input("Please retry: ")
    print("You answered ", ans)


main()