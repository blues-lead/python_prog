import json

def main():
    ifile = input("Enter the name of the input file: ")
    ofile = input("Enter the name of the output file: ")
    try:
        with open(ifile,"r") as fname:
            data = json.load(fname)
        with open(ofile,"w") as fname:
            for element in data:
                id = element['stationId']
                name = element['name']
                print("{:s};{:s}".format(id,name), file=fname)
    except OSError:
        print("There was an error in handling the file.")
        return
    print()
    print("Conversion succeeded.")

main()