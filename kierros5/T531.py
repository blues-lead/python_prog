def main():
    print("Give 5 numbers:")
    nums = []
    i = 1
    while i <= 5:
        number = int(input("Next number: "))
        nums.append(number)
        i += 1
    print("The numbers you entered that were greater than zero were:")
    for n in nums:
        if n > 0:
            print(n)

main()