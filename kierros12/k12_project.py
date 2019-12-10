# TIE-02100 Johdatus ohjelmointiin
# Anton Kondratev, anton.kondratev@tuni.fi, opiskelijanumero: 282650
# Ohjelma lukee tiedostosta polynomit muodossa: base1 exponent1; base2 exponent2;... muistiin
# Sen jälkeen ohjelma suorittaa laskutoimitukset polynomien kanssa
# Osa kommenteistä ovat englanniksi, koska Olio oli toteutettu toisena tiedostona
# ja itse ohjelmaa tehdessä muistin, että kurssi on suomenkielinen

class Polynomi:
    def __init__(self, poly): # polynomial will be preserved as a list of lists of size nx2, because I supposed
        self.__polynom = []   # that unsimplified version of polynomial is needed as well
                              # though a better way to preserve a polynomial would be a dict

        if len(poly) == 0 :   # check if empty list was related
            raise ValueError
        err = False
        if len([a for a in poly if len(a) != 2]) != 0: #check if length of each part of polynom less than 2
            err=True
        if len([b for a in poly for b in a if not isinstance(b,int)]) != 0: # check if there are not integers
            err = True
        if err == True: # rise exception if some of upper conditions is true
            raise ValueError
        self.__polynom = poly

    def __str__(self):
        """
        method is used for print-operaattorin kuormittamiseen. Polynomi tulostuu järjestettynä
        exponentin arvon mukaan.
        :return: Polynomi str-muodossa
        """
        substr = []
        if self.__polynom == []:
            return str(0)
        for value in sorted(self.__polynom, reverse = True, key = lambda x : x[1]):
            if value[0] == 0:
                continue
            base = str(value[0])
            exponent = str(value[1])
            substr.append("x^".join([base, exponent]))
        if len(substr) == 0:
            return "0"
        return " + ".join(substr)

    def simplify(self):
        """
        Funktio sieventää polynomin. Aluksi polynomi on muodossa "lista, jossa on listoja"
        Alkuperäinen muoto vaihdetaan dictiksi, jossa avaimina ovat polinomin eksponentit, jolloin
        termien yhdistäminen on paljon mukavampaa. Termit, joiden arvo on 0*x^y jätetään pois.
        :return: polinomi sievennettynä
        """
        dict = {}
        for element in self.__polynom:
            if element[1] not in dict:
                dict[element[1]] = element[0]
            else:
                dict[element[1]] += element[0]
        self.__polynom.clear()
        for element in dict:
            if dict[element] == 0:
                continue
            self.__polynom.append([dict[element],element])

    def add(self,poly):
        """
        method for adding polynomials. Polynomial being added is just appended to "self".
        After that it can be simplified by method simplify
        :param poly: Polynomial being added
        :return: resulting Polynomial
        """
        new_poly = [a for a in self.__polynom]
        for element in poly.__polynom:
            new_poly.append(element)
        return Polynomi(new_poly)

    def subtract(self,poly):
        """
        method for subtracting polynoms. Acting the same way as "add", but all members of the polynomial
        being added are multiplied by (-1) and after that method "add" is called
        :param poly: Polynomial being subtracted
        :return: resulting Polynomial
        """
        new_poly = []
        for element in poly.__polynom:
            new_element = [element[0] * -1, element[1]]
            new_poly.append(new_element)
        return self.add(Polynomi(new_poly))

    def multiply(self,poly):
        """
        Method for multiplying polynomials. Each member of the polynome being multiplied is multiplied by each member
        of "self"-polynomial. The same way as we do it by hand.
        :param poly: Polynom being multiplied
        :return: resulting Polynomial
        """
        new_p = []
        for value in poly.__polynom:
            for p in self.__polynom:
                base = value[0] * p[0]
                exponent = value[1] + p[1]
                new_p.append([base,exponent])
        return Polynomi(new_p)

def read_file(f_name):
    """
    Funktio lukee käyttäjän antaman tiedoston, jossa polynomit ovat muotoa: base1 exponent1;base2 exponent2;...
    Tiedoston luettua, funkito muodostaa dictin, jossa on Polynomi-oliot
    :param f_name: tiedoston nimi
    :return: kokoelma Polynomeja
    """
    to_ret = {}
    try:
        with open(f_name, "r") as polynoms:
            expressions = polynoms.readlines()
        i = 0
        for row in expressions:
            row = row.rstrip()
            pols = row.split(";")
            polynom = []
            for p in pols:
                np = p.split(" ")
                base = int(np[0])
                exponent = int(np[1])
                polynom.append([base,exponent])
            to_ret[i] = Polynomi(polynom)
            i += 1
    except OSError: # jos tiedosto ei ole luettavissa
        print("Error in reading the file.")
        return
    except ValueError: # oliossa nostetut virheet
        print("Error in reading the file.")
        return
    except IndexError: # jos tiedoston rakenteessa on virhe
        print("Error in reading the file.")
        return
    return to_ret


def main():
    functions = {"+" : lambda p1,p2 : p1.add(p2),
                 "-" : lambda p1,p2 : p1.subtract(p2),
                 "*" : lambda p1,p2 : p1.multiply(p2)}
    f_name = input("Enter file name: ")
    polynomials = read_file(f_name)
    if not polynomials: # jos read_file ei palauttanut mitään = hälytti virheestä
        return
    while True:
        command = input("> ")
        if command in ["Quit","quit"]:
            print("Bye bye!")
            break
        else:
            parts = command.split(" ")
            if len(parts) != 3: # jos komento ei koostu kolmesta osasta
                print("Error: entry format is memory_location operation memory_location.")
                continue
            if not parts[0].isdigit() or not parts[2].isdigit(): # jos komennon osat eivät ole lukuja
                print("Error: entry format is memory_location operation memory_location.")
                continue
            op1 = int(parts[0])
            op2 = int(parts[2])
            operation = parts[1]
            if operation not in functions:
                print("Error: unknown operator.")
                continue
            if op1 not in polynomials or op2 not in polynomials:
                print("Error: the given memory location does not exist.")
                continue
            result = functions[operation](polynomials[op1],polynomials[op2])
            result.simplify()
            print("Memory location {:d}: {:s}".format(op1,str(polynomials[op1])))
            print("Memory location {:d}: {:s}".format(op2, str(polynomials[op2])))
            print("The simplified result:")
            print(result)



main()