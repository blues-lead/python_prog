# TIE-02100 Johdatus ohjelmointiin
# Anton Kondratev, anton.kondratev@tuni.fi, opiskelijanumero: 282650
# Tehtävän 6.2. ratkaisu:
# Ohjelma tulostaa pylväsdiagrammin käyttäjän syöttämien tietojen
# perusteella. Ensin syötetään pistevälit, sitten jokaisen opiskelijan
# tenttipisteet. Näiden tietojen mukaan tulostetaan pylväsdiagrammi

def get_ranges():
    """
    Function asks user for pel spacings of marks.
    Value of a pel spacing can`t be less than zero or less than
    previously fed value
    :return: pel spacings as a list
    """
    ranges = [0]*6
    prev = -1 # previously fed value
    print("Please input the grade ranges.")
    for i in range(0,6):
        rng = int(input("Maximum score qualifying for grade {:1d}: ".format(i)))
        if rng < 0 or rng <= prev:
            print("Entered value {:1d} is not valid. Program terminating.".format(rng))
            return -1 # return -1 to flag error
        else:
            ranges[i]=rng
            prev = rng
    print("Finished reading the grade ranges.")
    print()
    return ranges

def get_students_marks(max_points):
    """
    Function asks user for exam points of each student while
    blank symbol is not fed. Value fed can`t be less than zero
    and greater than "max_points"
    :param max_points: highest value of points (from ranges)
    :return: list with students points
    """
    mark = -1
    mark_list = []
    i = 1
    print("Please input the scores for individual students.\nFinish by entering an empty line.")
    while True:
        mark = input("Input the exam score for student {:1d}: ".format(i))
        if mark == "" and len(mark_list) == 0:
            print("Finished reading the scores.\n\nNo students to process. Program terminating.")
            return -1
        elif mark == "":
            print("Finished reading the scores.")
            print()
            return mark_list
        elif int(mark) < 0 or int(mark) > max_points:
            print("Entered value {:1d} is not valid. Program terminating.".format(int(mark)))
            return -1
        mark_list.append(int(mark))
        i += 1

def form_data(ranges,marks):
    """
    Function produces list in form [index, count of marks].
    for instance [0,4] meaning that there are 4 zero-marks,
    [1,2] two marks 1
    :param ranges: list of pel spacings (result of function get_ranges)
    :param marks: list of each students points
    :return: list of marks and counts of the marks
    """
    data = [0]*len(ranges)
    z = 0 # counter for ranges list
    j = 0 # counter for marks in each range
    for rng in ranges:
        for m in marks:
            if m >= z and m <= rng:
                data[j] += 1
        z = rng + 1 # go to next range value
        j += 1
    return data

def print_diagram(data):
    """
    Function prints a bar diagram based on list of counts of marks
    :param data: count of marks of each student
    :return: nothing
    """
    for i in range(0,len(data)):
        print("{:1d}{:3d}".format(i,data[i]),"#"*data[i])

def main():
    ranges = get_ranges()
    if ranges == -1:
        return
    marks = get_students_marks(ranges[-1])
    if marks == -1:
        return
    data = form_data(ranges,marks)
    print_diagram(data)

main()