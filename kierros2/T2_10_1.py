def main():
    for i in range(1,8):
        days_no=1
        if i==2:
            days_no=28
        elif i%2==0:
            days_no=30
        else:
            days_no=31
        for j in range(1,days_no+1):
            print("{:d}.{:d}.".format(j,i))
    for i in range(8,13):
        days_no=1
        if i%2==0:
            days_no=31
        else:
            days_no=30
        for j in range(1,days_no+1):
            print("{:d}.{:d}.".format(j, i))


main()