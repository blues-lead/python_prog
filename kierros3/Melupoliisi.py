def main():
    #Ask user for # of measuremenets
    num=input("Enter the number of measurements: ")
    num=int(num)
    #tarkistetaan onko syötetty arvo sopiva
    if num <= 0:
        print("The number of measurements must be a positive number.")
        return
    prev=0 # edellinen mittaustulos
    yli_k=0 # tähän muuttujan lasketaan montako 80 dB ylitsevää tulosta
    for i in range(1,num+1):
        to_print = "Enter the measurement result " + str(i) + ": "
        n_mea = input(to_print)
        n_mea = int(n_mea)
        if i==1: # jos mittaustulos on ensimmäinen
            prev = n_mea # otetaan talteen "edelliseksi" tulokseksi
            if n_mea > 80: # ja jos tämä ensimmäinen ylitsee 80 dB
                yli_k += 1 # kasvatetaan laskuri
            continue # aloitetaan kierros alusta
        if prev > 80 and n_mea > 80: # jos nykyinen ja edellinen tulokset ovat yli 80dB
            print("High noise level. Ear protection needed!")
            return # lopetetaan ohjelma
        if n_mea > 80:
            yli_k+=1
        if yli_k > num*0.1: # jos laskurin arvo on isompi kuin 10% mitt.tul. määrää
            print("High noise level. Ear protection needed!")
            return
        prev=n_mea # tallennetaan nykyinen tulos "edelliseksi" tulokseksi
    print("Noise level is acceptable.")


main()