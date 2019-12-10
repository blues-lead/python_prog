# TIE-02100 Johdatus ohjelmointiin
# TIE-02106 Introduction to Programming
# BMI

from tkinter import *

NAN = float('NaN')

class Userinterface:

    def __init__(self):
        self.__mainwindow = Tk()
        self.__float_tulos = NAN
        # TODO: Change the title of the main window to be "BMI calculator"
        self.__mainwindow.title("BMI calculator")

        # TODO: Add GUI components to make the GUI understandable for the
        # user, for example labels to indicate what the user should write
        # in the Entry-components.
        self.__we_desc = Label(self.__mainwindow,text = "Enter your weight(kg)")
        self.__he_desc = Label(self.__mainwindow, text="Enter your height(cm)")

        # TODO: Create an Entry-component for the weight.
        self.__weight_value = Entry(self.__mainwindow)
        # TODO: Create an Entry-component for the height.
        self.__height_value = Entry(self.__mainwindow)

        # TODO: Create a Button that will call the calculate_BMI-method.
        # TODO: Change the colour of the Button to something else than
        # the default colour.
        self.__calculate_button = Button(self.__mainwindow, text="calculate BMI", bg="green", fg="black", command=self.calculate_BMI)
        # TODO: Create a Label that will show the decimal value of the BMI 
        # after it has been calculated.
        self.__result_text = Label(self.__mainwindow)
        # TODO: Create a Label that will show a verbal description of the BMI
        # after the BMI has been calculated.
        self.__explanation_text = Label(self.__mainwindow)
        # TODO: Create a button that will call the stop-method.
        self.__stop_button = Button(self.__mainwindow, text = "Quit", command=self.stop)

        # TODO: Place the components in the GUI as you wish.
        # If you read the Gaddis book, you can use pack here instead of grid!
        self.__we_desc.pack()
        self.__weight_value.pack()
        self.__he_desc.pack()
        self.__height_value.pack()
        self.__calculate_button.pack(side = LEFT)
        self.__stop_button.pack(side = RIGHT)
        self.__result_text.pack()
        self.__explanation_text.pack()


    # TODO: Implement this method.
    def calculate_BMI(self):
        ###
        try:
            w = float(self.__weight_value.get())
            h = float(self.__height_value.get())
            if w <= 0 or h <= 0:
                self.__explanation_text.configure(text="Error: height and weight must be positive.")
                self.reset_fields()
                return
        except ValueError:
            self.__explanation_text.configure(text="Error: height and weight must be numbers.")
            self.reset_fields()
            return

        ###
        h *= 0.01
        self.__float_tulos = w / ((h**2))
        if self.__float_tulos >= 18.5 and self.__float_tulos <=25:
            expl = "Your weight is normal."
        elif self.__float_tulos < 18.5:
            expl = "You are underweight."
        else:
            expl = "You are overweight."
        res = "{:.2f}".format(self.__float_tulos)
        self.__result_text.configure(text=res)
        self.__explanation_text.configure(text=expl)
        """ Section b) This method calculates the BMI of the user and
            displays it. First the method will get the values of
            height and weight from the GUI components
            self.__height_value and self.__weight_value.  Then the
            method will calculate the value of the BMI and show it in
            the element self.__result_text. 
            
            Section e) Last, the method will display a verbal
            description of the BMI in the element
            self.__explanation_text. 
        """ 
        pass

    # TODO: Implement this method.
    def reset_fields(self):
        """ In error situations this method will zeroize the elements
            self.__result_text, self.__height_value, and self.__weight_value.
        """
        self.__weight_value.delete(0,END)
        self.__height_value.delete(0,END)
        self.__result_text.configure(text="")

    def stop(self):
        """ Ends the execution of the program.
        """
        self.__mainwindow.destroy()

    def start(self):
        """ Starts the mainloop. 
        """
        self.__mainwindow.mainloop()

    def get_values(self):
        """try:
            weight = float(self.__weight_value.get())
            if weight <= 0:
                self.__explanation_text.configure(text="Error: height and weight must be positive.")
                self.reset_fields()
                return NAN
        except ValueError:
            self.__explanation_text.configure(text="Error: height and weight must be numbers.")
            self.reset_fields()
            return NAN
        try:
            height = float(self.__height_value.get())
            if height <= 0:
                self.__explanation_text.configure(text="Error: height and weight must be positive.")
                self.reset_fields()
                return NAN
        except ValueError:
            self.__explanation_text.configure(text="Error: height and weight must be numbers.")
            self.reset_fields()
            return NAN"""
        try:
            weight = float(self.__weight_value.get())
            height = float(self.__height_value.get())
            if weight <= 0 or height <= 0:
                self.__explanation_text.configure(text="Error: height and weight must be positive.")
                return -1, -1
        except ValueError:
            self.__explanation_text.configure(text="Error: height and weight must be numbers.")
            return -1, -1
        return weight,height


def main():
    ui = Userinterface()
    ui.start()


main()
