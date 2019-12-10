def longest_substring_in_order(rivi):
    i = 0
    test = 0
    lst = []
    left_lst = []
    prev = ""
    word = ""
    # while i < len(rivi):
    while True:
        if i == len(rivi):
            lst.append(word)
            break
        if rivi[i] > prev:
            word += rivi[i]
            if len(word) == len(rivi):
                return word
            prev = rivi[i]
        else:
            # print(word)
            lst.append(word)
            prev = rivi[i]
            word = prev
        i += 1
    pisin = ""
    for e in lst:
        if len(e) > len(pisin):
            pisin = e
    return pisin




print(longest_substring_in_order("abcdefghijk"))
# print("="*30)
print(longest_substring_in_order("abcabcdefgabab"))
# print("="*30)
print(longest_substring_in_order("acdkbarstyefgioprtyrtyx"))
# print("="*30)
print(longest_substring_in_order("fedcba"))
# print("="*30)
print(longest_substring_in_order("efghijklmnopopqefgabcdeabcdefghijklm"))