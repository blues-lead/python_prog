class Polynomi:
    def __init__(self, poly): # polynom will be preserved as a list of lists of size nx2, because I supposed
        self.__polynom = []   # that unsimplified version of polynom is needed as well
                              # though a better way to preserve a polynom would be a dict

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
            base = str(value[0])
            exponent = str(value[1])
            substr.append("x^".join([base, exponent]))
        return " + ".join(substr)

    def simplify(self): # the polynome is converted into dict and then back to list, because I didnt know
                        # about necessity of preserving an unsimplified polynom. By default unsimplified version
                        # of a polynom is preserved in list of lists
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
        method for adding polynomials. Polynom being added is just appended to "self".
        After that it can be simplified by method simplify
        :param poly: Polynom being added
        :return: resulting Polynom
        """
        new_poly = [a for a in self.__polynom]
        for element in poly.__polynom:
            new_poly.append(element)
        return Polynomi(new_poly)

    def subtract(self,poly):
        """
        method for subtracting polynoms. Acting the same way as "add", but all members of the polynom
        being added are multiplied by (-1) and after that method "add" is called
        :param poly: Polynom being subtracted
        :return: resulting Polynom
        """
        for element in poly.__polynom:
            element[0] *= -1
        return self.add(poly)

    def multiply(self,poly):
        """
        Method for multiplying polynomes. Each member of the polynome being multiplied is multiplied by each member
        of "self"-polynom. The same way as we do it by hand.
        :param poly: Polynom being multiplied
        :return: resulting Polynom
        """
        new_p = []
        for value in poly.__polynom:
            for p in self.__polynom:
                base = value[0] * p[0]
                exponent = value[1] + p[1]
                new_p.append([base,exponent])
        return Polynomi(new_p)





