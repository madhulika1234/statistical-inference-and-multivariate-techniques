
from scipy.integrate import quad
import numpy as np


print("***************************************************************")
print("Calculation of F value from given P and DOF")
print("***************************************************************")

repeat = "y"
while repeat == "y":
    try:
        text = input("enter Alpha value  to calculate F value   ")
        value = float(text)
    except ValueError:
        print("Error! This is not a number. Try again.")
    else:
        try:
            text = input("enter the numerator degrees of freedom ")
            ndof = int(text)
            text = input("enter the denominator degrees of freedom ")
            ddof = int(text)
        except ValueError:
            print("Error! This is not a number. Try again.")
        else:
            gammaUp = np.math.gamma((ndof + ddof) / 2)
            gammaL1 = np.math.gamma(ndof / 2)
            gammaL2 = np.math.gamma(ddof / 2)
            constant = gammaUp * pow(ndof / ddof, ndof / 2) / (gammaL1 * gammaL2)
            r = 0
            start = 0
            end = 62009999
            mid = round(float((start + end) / 2), 4)
            count=100
            while count > 0  :
                f = round(mid / 10000, 8)
                ProbabilityDensity = lambda x: constant * pow(x, (ndof / 2) - 1) / pow(((ndof / ddof) * x) + 1,
                                                                                       (ndof + ddof) / 2)
                result, _ = quad(ProbabilityDensity, 0, f)
                p = round(1 - float(result), 6)
                if p == value:
                    r = 1
                    print("the F value is ", f)
                    break
                else :
                    if p < value :
                        end= mid
                    else :
                        start=mid
                mid = round(float((start + end) / 2), 4)
                count= count -1
            if r == 0:
                print("unable to find !!!! plz try again !!!!")


    repeat = input(" press y to continue / any key to exit ")

print("***************************************************************")
print("Calculation of P from given F value and DOF")
print("***************************************************************")
repeat = "y"
while repeat == "y":
    try:
        text = input("enter the F value  to calculate  P   ")
        value = float(text)
    except ValueError:
        print("Error! This is not a number. Try again.")
    else:
        try:
            text = input("enter the numerator degrees of freedom ")
            ndof = int(text)
            text = input("enter the denominator degrees of freedom ")
            ddof = int(text)
        except ValueError:
            print("Error! This is not a number. Try again.")
        else:
            gammaUp = np.math.gamma((ndof + ddof) / 2)
            gammaL1 = np.math.gamma(ndof / 2)
            gammaL2 = np.math.gamma(ddof / 2)
            constant = gammaUp * pow(ndof/ddof, ndof/2) / (gammaL1*gammaL2)

            ProbabilityDensity = lambda x: constant * pow(x, (ndof/2)-1)/ pow(  ((ndof/ddof)*x)+1  , (ndof+ddof)/2)
            result, _ = quad(ProbabilityDensity, 0, value)
            print("the P value is ", round(1 - float(result), 5))

    repeat = input(" press y to continue / any key to exit ")

