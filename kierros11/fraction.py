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

