import os

def main():
    files = []
    er_file = open("error.txt", "r", encoding="utf8")
    for line in er_file:
        if line[0] == "#" or line == "":
            continue
        line = line.strip()
        parts = line.split(", ")
        for p in parts:
            files.append(p)
    er_file.close()
    for i in files:
        print(i)


main()