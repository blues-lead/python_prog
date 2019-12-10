b=input("Enter the amount of the study benefits: ")
korko = float(b)*1.0117
print("If the index raise is 1.17 percent, the study benefit,")
print("after a raise, would be " + str(korko) + " euros")
korko=float(b)*1.0117**2
print("and if there was another index raise, the study")
print("benefits would be as much as "+str(korko)+" euros")