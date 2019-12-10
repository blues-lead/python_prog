def main():
    num=input("How many Fibonacci numbers do you want? ")
    num=int(num)
    print("1. 1\n2. 1")
    prev=1
    pprev=1
    for i in range(3,num+1):
        print("{:d}. {:<2d}".format(i,prev+pprev))
        now=prev+pprev
        pprev=prev
        prev=now


main()