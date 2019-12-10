# TIE-02100 Johdatus ohjelmointiin

def print_keys(sanakirja):
    uusilause = ""
    uusilause = ", ".join(sorted(sanakirja))
    return uusilause

def print_dict(en_sanakirja):
    sp_sanakirja = {}
    for word in en_sanakirja:
        sp_sanakirja[en_sanakirja[word]] = word
    print()
    print("English-Spanish")
    for word in sorted(en_sanakirja):
        print(word,en_sanakirja[word])
    print()
    print("Spanish-English")
    for word in sorted(sp_sanakirja):
        print(word, sp_sanakirja[word])
    print()

def main():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}
    print("Dictionary contents:")
    print(print_keys(english_spanish))

    while True:
        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command == "W":

            word = input("Enter the word to be translated: ")
            if word not in english_spanish:
                print("The word", word, "could not be found from the dictionary.")
                continue
            print(word, "in Spanish is", english_spanish[word])

        elif command == "A":
            en_word = input("Give the word to be added in English: ")
            sp_word = input("Give the word to be added in Spanish: ")
            english_spanish[en_word] = sp_word
            print("Dictionary contents:")
            print(print_keys(english_spanish))

        elif command == "R":
            r_word = input("Give the word to be removed: ")
            if r_word not in english_spanish:
                print("The word", r_word, "could not be found from the dictionary.")
                continue
            del english_spanish[r_word]
        elif command == "P":
            print_dict(english_spanish)

        elif command == "T":
            translated = ""
            to_translate = input("Enter the text to be translated into Spanish: ")
            word_list = to_translate.split(" ")
            for word in word_list:
                tmp = ""
                if word in english_spanish:
                    tmp = english_spanish[word]
                else:
                    tmp = word
                translated += tmp + " "
            print("The text, translated by the dictionary:")
            print(translated)
        elif command == "Q":
            print("Adios!")
            return

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")


main()
