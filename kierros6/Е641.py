def reverse_name(s_name):
    new_name = ""
    if "," in s_name:
        lst_name = s_name.split(",")
        if len(lst_name[0]) > 0 and len(lst_name[1]) > 0:
            new_name = lst_name[1].strip() + " " + lst_name[0].strip()
        elif len(lst_name[0]) == 0 or len(lst_name[1]) == 0:
            if len(lst_name[0]) == 0:
                new_name = lst_name[1].strip()
            else:
                new_name = lst_name[0].strip()
    else:
        new_name = s_name.strip()
    # print(new_name)
    return new_name