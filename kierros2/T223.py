def main():
    ans="z"
    while ans!="y":
        ans=input("Bored? (y/n) ")
        while ans!="n" and ans!="N" and ans!="y" and ans!="Y":
            ans=input("Incorrect entry.\nPlease retry: ")
    print("Well, let's stop this, then.")




main()