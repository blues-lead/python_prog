def read_text():
    user_text = []
    print("Enter rows of text for word counting. Empty row to quit.")
    while True:
        row = input().lower()
        if row == "":
            break
        user_text.append(row)
    return user_text


def count_words(text):
    tilasto = {}
    for row in text:
        tmp = row.split(" ")
        for sign in tmp:
            if sign in tilasto:
                tilasto[sign] += 1
            else:
                tilasto[sign] = 1
    return tilasto

def main():
    user_text = read_text()
    tls = count_words(user_text)
    for word in sorted(tls):
        print("{:1s} : {:1d} times".format(word,tls[word]))


main()