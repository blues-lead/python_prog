def main():
    fname = input("Enter the name of the file: ")
    try:
        file = open(fname, "w")
        print("Enter rows of text. Quit by entering an empty row.")
        i = 1
        while True:
            row = input()
            if row == "":
                file.close()
                print("File", fname, "has been written.")
                break
            row = str(i) + " " + row
            file.write(row + "\n")
            i += 1
    except OSError:
        print("Writing the file",fname,"was not successful.")



main()