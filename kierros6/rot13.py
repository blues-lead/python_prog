# TIE-02100 Johdatus ohjelmointiin
# TIE-02106 Introduction to Programming
# Task: ROT13, program code template


def encrypt(alphabet):
    regular_chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                     "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                     "w", "x", "y", "z"]

    encrypted_chars = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                       "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                       "j", "k", "l", "m"]

    # Implement encryption here
    if alphabet.lower() in regular_chars:
        inds = regular_chars.index(alphabet.lower())
        enc = encrypted_chars[inds]
        if alphabet.islower():
            alphabet = enc
        else:
            alphabet = enc.upper()

    return alphabet


def row_encryption(rivi):
    to_ret = ""
    for char in rivi:
        to_ret += encrypt(char)
    return to_ret


def main():
    str = input("Phrase to encrypt: ")
    print(row_encryption(str))

main()