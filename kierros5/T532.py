def main():
    print("Give 5 numbers:")
    nums = []
    i = 1
    while i <= 5:
        number = int(input("Next number: "))
        nums.append(number)
        i += 1
    print("The numbers you entered, in reverse order:")
    for i in range (4,-1,-1):
        print(nums[i])

main()