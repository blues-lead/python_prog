def main():
    name = input("Enter the name of the file: ")
    try:
        file_desc = open(name,"r")
        i = 1
        for row in file_desc:
            row = row.strip()
            print("{:<1d} {:1s}".format(i,row))
            i += 1
        file_desc.close()
    except OSError:
        print("There was an error in reading the file.")


main()