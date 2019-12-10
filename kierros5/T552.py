def is_the_list_in_order(lst):
    lst_s = sorted(lst)
    if lst_s == lst:
        return True
    else:
        return False