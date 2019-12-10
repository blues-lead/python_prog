def main():
    num=input("How many Fibonacci numbers do you want? ")
    num=int(num)
    prev=1
    pprev=0
    i=2
    print("{:d}. {:<2d}".format(1, pprev + prev))
    while i <= num:
        print("{:d}. {:<2d}".format(i,pprev+prev))
        now=pprev+prev
        pprev=prev
        prev=now
        i+=1

main()