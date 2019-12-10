# Johdatus ohjelmointiin
# Parasetamol

def calculate_dose(w, h, l):
    to_ret = 0
    does_pweight = w*15
    if h < 6:
        to_ret = does_pweight - l
    else:
        to_ret = does_pweight
    if to_ret + l > 4000:
        to_ret = 4000 - l
    if to_ret < 0:
        to_ret = 0
    if h < 6:
        to_ret = 0
    return to_ret

def main():

    "Patient's weight (kg): "
    "How much time has passed from the previous dose (full hours): "
    "The total dose for the last 24 hours (mg): "
    "The amount of Parasetamol to give to the patient: "

    # calculate_dose assumes parameters to be of type int
    # and they should be passed in the order: weight, time, total_doze_24
    # (or more like the automated tests assume this)

    weight = input("Patient's weight (kg): ")
    hours = input("How much time has passed from the previous dose (full hours): ")
    last = input("The total dose for the last 24 hours (mg): ")
    next_dose = calculate_dose(int(weight), int(hours), int(last))
    print("The amount of Parasetamol to give to the patient: {:s}".format(str(next_dose)))

main()
