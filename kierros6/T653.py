def read_message():
    conv = []
    while True:
        stri = input()
        if stri != "":
            conv.append(stri)
        else:
            return conv


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
    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()
    encrypted = []
    for row in msg:
        encrypted.append(row_encryption(row))
    print("ROT13:")
    for row in encrypted:
        print(row)

main()