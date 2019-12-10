# Introduction to Programming
# Named parameters


def print_box(width, height, border_mark="#", inner_mark=" "):
    for i in range(1,height+1):
        if i==1 or i==height:
            string = border_mark*width
            print(string)
        else:
            string = border_mark + inner_mark*(width-2) + border_mark
            print(string)


def main():
    print_box(5, 4)
    print_box(3, 8, "*")
    print_box(5, 4, "O", "o")
    print_box(inner_mark=".", border_mark="O", height=4, width=6)

main()
