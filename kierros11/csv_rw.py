import csv

def main():
    file_to_read = input("Enter the name of the input file: ")
    dia_to_read = input("and its dialect: ")
    file_to_write = input("Enter the name of the output file: ")
    dia_to_write = input("and its dialect: ")
    r_info = []
    try:
        # file_to_read = "lecturepoints.csv"
        r_csv = open(file_to_read,'r', newline='')
        try:
            dia = csv.get_dialect(dia_to_read)
            rows = csv.reader(r_csv, dia)
            for r in rows:
                r_info.append(r)
        except csv.Error:
            print("The given dialect is wrong.")
            return
        r_csv.close()
    except OSError:
        print("There was an error in handling the file.")
        return
    try:
        # file_to_write = "text.csv"
        w_csv = open(file_to_write,'w',newline='')
        try:
            dia = csv.get_dialect(dia_to_write)
            writer = csv.writer(w_csv,dia)
            writer.writerows(r_info)
        except csv.Error:
            print("The given dialect is wrong.")
            return
        w_csv.close()
    except OSError:
        print("There was an error in handling the file.")
        return
    print()
    print("File {:s} has been converted into {:s}.".format(file_to_read, dia_to_write))




main()
