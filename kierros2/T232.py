def main():
    nr=input("Choose a number: ")
    res=0
    i=1
    while res < 100:
        res=i*int(nr)
        print(i,"*",nr,"=",res)
        i+=1



main()