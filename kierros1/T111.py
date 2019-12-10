def main():
    price = input("Purchase price: ")
    paid = input("Paid amount of money: ")
    ret = int(paid) - int(price)
    if ret > 0:
        print("Offer change:")
        ten_euro=ret//10;
        if ten_euro != 0:
            print(ten_euro,"ten-euro notes")
        ret=ret-ten_euro*10;
        five_euro=ret//5
        if five_euro != 0:
            print(five_euro,"five-euro notes")
        ret=ret-five_euro*5;
        two_euro=ret//2;
        if two_euro != 0:
            print(two_euro,"two-euro coins")
        ret=ret-two_euro*2
        if ret != 0:
            print(ret,"one-euro coins")
    else:
        print("No change")
main()