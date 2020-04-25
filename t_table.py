from scipy.integrate import quad
import numpy as np


print("****************************************************************")
print("Calculation of t value from given p  and DOF")
print("****************************************************************")

repeat = "y"
while repeat == "y":
    try:
        text = input("enter the P value   ")
        value = float(text)
    except ValueError:
        print("Error! This is not a number. Try again.")
    else:
        try:
            text = input("enter the degrees of freedom ")
            dof = int(text)
        except ValueError:
            print("Error! This is not a number. Try again.")
        else:
            gammaUp = np.math.gamma((dof + 1) / 2)
            gammaL = np.math.gamma(dof / 2)
            constant = gammaUp / (np.sqrt(dof * np.pi) * gammaL)
            r = 0
            start = 0
            end = 63799999
            mid = round(float((start + end) / 2), 4)
            count = 100
            while count > 0:
                t= round( mid/100000, 8)

                ProbabilityDensity = lambda x: constant * 1 / (pow((x * x / dof) + 1, (dof + 1) / 2))
                result, _ = quad(ProbabilityDensity, np.NINF, t )

                p = round(1 - float(result), 8)

                if p == value:
                    r = 1
                    print("the t value is ", t)
                    break
                else:
                    if p == 1.0 :
                        end = mid
                    else:
                        if p < value:
                            end = mid
                        else:
                            start = mid
                mid = round(float((start + end) / 2), 4)
                count = count - 1
            if r == 0:
                print("unable to find !!!! plz try again !!!!")

    repeat = input(" press y to continue / any key to exit ")
repeat = "y"


print("***************************************************************")
print("Calculation of P from given t and DOF")
print("***************************************************************")
while repeat == "y":
    try:
        text = input("enter the t value   ")
        value = float(text)
    except ValueError:
        print("Error! This is not a number. Try again.")
    else:
        try:
            text = input("enter the degrees of freedom ")
            dof = int(text)
        except ValueError:
            print("Error! This is not a number. Try again.")
        else:
            gammaUp = np.math.gamma((dof + 1) / 2)
            gammaL = np.math.gamma(dof / 2)

        constant = gammaUp / (np.sqrt(dof * np.pi) * gammaL)

        ProbabilityDensity = lambda x: constant * 1 / (pow((x * x / dof) + 1, (dof + 1) / 2))
        result, _ = quad(ProbabilityDensity, np.NINF, value)
        print("the P value is ", round(1 - float(result), 3))

    repeat = input(" press y to continue / any key to exit ")




