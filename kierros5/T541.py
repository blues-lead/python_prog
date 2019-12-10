def input_to_list(count):
    i = 0
    list = [0]*(count)
    print("Enter {:1d} numbers:".format(count))
    while i < count:
        list[i] = int(input(""))
        i+=1
    return list


def main():
    counter = 0
    cnt = int(input("How many numbers do you want to process: "))
    nums = input_to_list(cnt)
    tbs = int(input("Enter the number to be searched: "))
    for element in nums:
        if element == tbs:
            counter += 1
    if counter != 0:
        print("{:1d} shows up {:1d} times among the numbers you have entered.".format(tbs,counter))
    else:
        print("{:1d} is not among the numbers you have entered.".format(tbs))


main()