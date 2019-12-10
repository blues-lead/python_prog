class Fraction:
    """ This class represents one single fraction that consists of
        numerator and denominator """

    def __init__(self, numerator, denominator):
        """
        Constructor. Checks that the numerator and denominator are of
        correct type and initializes them.

        :param numerator: fraction's numerator
        :param denominator: fraction's denominator
        """

        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError
        elif denominator == 0:
            raise ValueError

        self.__numerator = numerator
        self.__denominator = denominator

    def return_string(self):
        """ Returns a string-presentation of the fraction in the format
        numerator/denominator """

        if self.__numerator * self.__denominator < 0:
            sign = "-"
        else:
            sign = ""
        return "{:s}{:d}/{:d}".format(sign, abs(self.__numerator),
                                     abs(self.__denominator))

    def simplify(self):
        divisor = greatest_common_divisor(self.__numerator, self.__denominator)
        self.__denominator //= divisor
        self.__numerator //= divisor

    def reciprocal(self):
        n_numerator = self.__denominator
        n_denominator = self.__numerator
        return Fraction(n_numerator, n_denominator)

    def complement(self):
        n_numerator = self.__numerator
        n_denominator = self.__denominator
        return Fraction(n_numerator*(-1),n_denominator)

    def multiply(self,fraction):
        num1 = self.__numerator
        den1 = self.__denominator
        num2 = fraction.__numerator
        den2 = fraction.__denominator
        return Fraction(num1*num2,den1*den2)

    def divide(self,fraction):
        n_num = self.__numerator*fraction.__denominator
        n_den = self.__denominator*fraction.__numerator
        return Fraction(n_num,n_den)

    def add(self,fraction):
        n_den = self.__denominator*fraction.__denominator
        n1_num = self.__numerator*fraction.__denominator
        n2_num = fraction.__numerator*self.__denominator
        return Fraction(n1_num+n2_num,n_den)

    def deduct(self,fraction):
        n_den = self.__denominator*fraction.__denominator
        n1_num = self.__numerator*fraction.__denominator
        n2_num = fraction.__numerator*self.__denominator
        return Fraction(n1_num-n2_num,n_den)

    def __lt__(self,fraction):
        n = self.deduct(fraction)
        return n.__numerator < 0 or n.__denominator < 0

    def __gt__(self,fraction):
        n = self.deduct(fraction)
        return n.__numerator > 0 and n.__denominator > 0

    def __str__(self):
        if self.__numerator*self.__denominator < 0:
            sign = "-"
        else:
            sign = ""
        return "{:s}{:d}/{:d}".format(sign,abs(self.__numerator),abs(self.__denominator))


def greatest_common_divisor(a, b):
    """
    Euclidean algorithm.
    """

    while b != 0:
        a, b = b, a % b
    return a

def read_file(fname):
    laskin = {}
    try:
        file = open(fname,"r")
        source = file.readlines()
        file.close()
        for line in source:
            parts = line.split("=")
            if len(parts) != 2:
                raise
            ml = parts[1].split("/")
            if len(ml) != 2:
                raise
            murtoluku = Fraction(int(ml[0]), int(ml[1]))
            name = parts[0]
            laskin[name] = murtoluku
        return laskin
    except:
        print("Error: the file cannot be read.")
        return


def main():
    operations = {"+" : lambda f1,f2: f1.add(f2),
                  "-" : lambda f1,f2: f1.deduct(f2),
                  "*" : lambda f1,f2: f1.multiply(f2),
                  "/" : lambda f1,f2: f1.divide(f2)}
    laskin = {}
    while True:
        str = input("> ")
        if str == "add":
            s_murtoluku = input("Enter a fraction in the form integer/integer: ").split("/")
            name = input("Enter a name: ")
            laskin[name] = Fraction(int(s_murtoluku[0]),int(s_murtoluku[1]))
        elif str == "quit":
            print("Bye bye!")
            return
        elif str == "print":
            name = input("Enter a name: ")
            if name in laskin:
                print("{:s} = {:s}".format(name,laskin[name].return_string()))
            else:
                print("Name", name, "was not found")
        elif str == "list":
            if len(laskin) == 0:
                continue
            else:
                for name in sorted(laskin):
                    print("{:s} = {:s}".format(name, laskin[name].return_string()))
        # elif str == "*":
        elif str in operations:
            f1 = input("1st operand: ")
            if f1 not in laskin:
                print("Name", f1, "was not found")
                continue
            f2 = input("2nd operand: ")
            if f2 not in laskin:
                print("Name", f2, "was not found")
                continue
            new = operations[str](laskin[f1],laskin[f2])
            print(laskin[f1], str, laskin[f2], " = ", new)
            new.simplify()
            print("simplified", new)
        elif str == "file":
            f_name = input("Enter the name of the file: ")
            laskin = read_file(f_name)
            if not laskin:
                continue
        else:
            print("Unknown command!")

main()