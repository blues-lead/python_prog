# TIE-02100 Johdatus ohjelmointiin
# TIE-02106 Introduction to Programming
# Task: viesti, program code template

def read_message():
    conv = []
    while True:
        stri = input()
        if stri != "":
            conv.append(stri)
        else:
            return conv


def main():
    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()
    print("The same, shouting:")
    for row in msg:
        print(row.upper())


main()
