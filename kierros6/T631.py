# a e i o u y
def main():
    vowels = "aeiouy"
    word = input("Enter a word: ")
    counter = 0
    for chr in word:
        if chr in vowels:
            counter += 1
    print("The word", word, "contains {:1d} vowels and {:1d} consonants".format(counter,len(word)-counter))

main()