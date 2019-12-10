def main():
    perfs = []
    for i in range(1,6):
        sec_i = float(input("Enter the time for performance {:1d}: ".format(i)))
        perfs.append(sec_i)
    perfs.sort() # järjestetään lista poistaakseni paras ja huonoin tulos
    del perfs[0] # poistetaan paras
    del perfs[3] # poistetaan huonoin
    sum = 0
    for element in perfs:
        sum += element
    print("The official competition score is {:1.2f} seconds.".format(sum/len(perfs)))


main()