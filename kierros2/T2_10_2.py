def main():
    pnt_d=3
    pnt_m=1
    days=0
    z=1
    for i in range(1,8):
        days_no=1
        if i==2:
            days_no=28
        elif i%2==0:
            days_no=30
        else:
            days_no=31
        for j in range(1,days_no+1):
            if j==3 and i==1:
                print("{:d}.{:d}.".format(j,i))
                z=0
            elif z==7:
                print("{:d}.{:d}.".format(j, i))
                z=0
            z+=1
    for i in range(8,13):
        days_no=1
        if i%2==0:
            days_no=31
        else:
            days_no=30
        for j in range(1,days_no+1):
            if z==7:
                print("{:d}.{:d}.".format(j, i))
                z=0
            z+=1


main()