def are_all_members_same(lst):
    ln = len(lst)
    if ln == 0:
        return True
    fst = lst[0]
    to_ret = False
    for element in lst:
        if fst != element:
            return False
    return True