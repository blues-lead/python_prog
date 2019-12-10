def read_file():
    f_list = []
    d_points = {}
    fname = input("Enter the name of the score file: ")
    try:
        fdesc = open(fname,"r")
        f_list = fdesc.readlines()
        for line in f_list:
            line = line.rstrip()
            row = line.split(" ")
            if len(row) != 2:
                print("There was an erroneous line in the file:\n", line.strip(),sep="")
                return 0
            if row[0] in d_points:
                d_points[row[0]] += int(row[1])
            else:
                d_points[row[0]] = int(row[1])
        return d_points
    except OSError:
        print("There was an error in reading the file.")
        return 0
    except ValueError:
        print("There was an erroneous score in the file:")
        print(row[1])
        return 0



def main():
    gamepoints = read_file()
    if gamepoints == 0:
        return
    print("Contestant score:")
    for s in sorted(gamepoints):
        print(s,gamepoints[s])


main()