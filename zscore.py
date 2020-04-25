from scipy.integrate import quad
import numpy as np


def normalProbabilityDensity(x):
    constant = 1.0 / np.sqrt(2 * np.pi)
    return (constant * np.exp((-x ** 2) / 2.0))


print("*********************************************")
print(" Calculation of P(z<z0) for given z0 ")
print("*********************************************")
repeat = "y"
while repeat == "y":
    try:
        text = input("enter the value z0 to calculate the P(z<z0) ")
        number = float(text)
    except ValueError:
        print("Error! This is not a number. Try again.")
    else:
        result, _ = quad(normalProbabilityDensity, np.NINF, number)
        print(result)

    repeat = input(" press y to continue / any key to exit ")

repeatAlpha = "y"
print("****************************************************************")
print("Calculation of z0 for given alpha such that P(z<z0)=alpha")
print("****************************************************************")
while repeatAlpha == "y":
    try:
        text = input("enter the value alpha to calculate the  z0 such that P(z<z0)=alpha ")
        number = float(text)
    except ValueError:
        print("Error! This is not a number. Try again.")
    else:
        r = 0
        start = -349
        end = 350
        mid = round(float((start + end) / 2),6)
        count = 100
        while count > 0:
            z = round(mid / 100, 8)

            result, _ = quad(normalProbabilityDensity, np.NINF, z)
            p = round(float(result), 8)

            if p == round(number, 8):
                print("the calculated z value is")
                print(z)
                r = 1
                break
            else:
                if p > number:
                    end = mid
                else:
                    start = mid
            mid = round(float((start + end) / 2), 8)
            count = count - 1
        if r == 0:
            print("Sorry !!!! unable to find , try a different value")

    repeatAlpha = input(" press y to continue / any key to exit ")
