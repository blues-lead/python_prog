# Johdatus ohjelmointiin
# Print a box with input checking
def read_input(string):
    szi = -1
    while szi <= 0:
        szi=input(string)
        szi = int(szi)
    return szi

def print_box(w,h,m):
    for i in range(1,h+1):
        string = m*w
        print(string)

def main():

    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")

    
    print_box(width, height, mark)

main()
