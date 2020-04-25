
from scipy.integrate import quad
import numpy as np

print("****************************************************************")
print("Calculation of chi square value from given p value and DOF")
print("****************************************************************")

repeat = "y"
while repeat == "y":
    try:
        text = input("enter the P value   ")
        value = float(text)
        length=int(len(text))-2
    except ValueError:
        print("Error! This is not a number. Try again.")
    else:
        try:
            text = input("enter the degrees of freedom ")
            dof = int(text) / 2
        except ValueError:
            print("Error! This is not a number. Try again.")
        else:
            gamma = np.math.gamma(dof)
            constant = 1 / (pow(2, dof) * gamma)
            r = 0
            start = 0
            end = 90000
            mid = round(float((start + end) / 2), 8)
            count = 150
            while count > 0:

                chi = round(mid / 1000, 8)
                if chi== 0:
                    r=1
                    print("the chi square value is ", chi)
                    break
                ProbabilityDensity = lambda x: constant * np.exp(-x / 2) * pow(x, dof - 1)
                result, _ = quad(ProbabilityDensity, 0, chi)
                p = round(1 - float(result), length)
                if p == value:
                    r = 1
                    print("the chi square value is ", chi)
                    break
                else:
                    if p == 1.0:
                        end = mid
                    else:
                        if p < value:
                            end = mid
                        else:
                            start = mid
                mid = round(float((start + end) / 2), 8)
                count = count - 1
            if r == 0:
                print("unable to find !!!! plz try again !!!!")

    repeat = input(" press y to continue / any key to exit ")

print("****************************************************************")
print("Calculation of P from given chi square value and DOF")
print("****************************************************************")
repeat = "y"
while repeat == "y":
    try:
        text = input("enter the chi square value   ")
        value = float(text)
    except ValueError:
        print("Error! This is not a number. Try again.")
    else:
        try:
            text = input("enter the degrees of freedom ")
            number = int(text) / 2
        except ValueError:
            print("Error! This is not a number. Try again.")
        else:
            gamma = np.math.gamma(number)

        constant = 1 / (pow(2, number) * gamma)

        ProbabilityDensity = lambda x: constant * np.exp(-x / 2) * pow(x, number - 1)
        result, _ = quad(ProbabilityDensity, 0, value)
        print("the P value is ", round(1 - float(result), 2))

    repeat = input(" press y to continue / any key to exit ")
