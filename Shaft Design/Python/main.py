from math import pi, sqrt


def goodman_criteria_one():
    """
    Calculates the goodman criteria for questions 1-10
    """
    # Calculating sqrt(a)
    bendingRootA = 0.246 - (3.08 * 10 ** -3) * Sut + (1.51 * 10 ** -5) * Sut ** 2 - (2.67 * 10 ** -8) * Sut ** 3
    torsionalRootA = 0.190 - (2.51 * 10 ** -3) * Sut + (1.35 * 10 ** -5) * Sut ** 2 - (2.67 * 10 ** -8) * Sut ** 3

    # Calculating q values
    qBending = 1 / (1 + (bendingRootA / rootR))
    qTorsional = 1 / (1 + (torsionalRootA / rootR))

    # converting Kt and Kts
    Kf = 1 +  qBending * (Kt - 1)
    Kfs = 1 + qTorsional * (Kts - 1)

    # Calculating K (a-e) values
    a = 2
    b = -0.217
    Ka = a * Sut ** b
    Kb = 0.879 * diameter ** -0.107
    Kc = 1
    Kd = 1
    Ke = 1

    #calculating Se
    Se = Ka * Kb * Kc * Kd * Ke * sePrime

    # Calculating stress components
    A = sqrt(4 * (Kf * moment) ** 2)
    B = sqrt(3* (Kfs * torque) ** 2)

    # Calculating safety factor
    Nf = ((pi * diameter ** 3) / 16) * ((A / Se) + (B / Sut)) ** -1

    # Showing the answer to the user
    print('The factor of safety calculated from the Goodman criteria is : ' + str(Nf))


def vonmises_stress():
    """
    Calculates the safety factor against first cycle yielding, using Von Mises.
    Questions ___
    """
    #

    # Showing the answer to the user
    print('The factor of safety calculated from the von Mises stress is : ' + str(safetyFactor))


def goodman_criteria_two():
    """
    Calculates the goodman criteria for questions ____
    """
    Nf = 1
    print('The factor of safety calculated from the Goodman criteria is : ' + str(Nf))


if __name__ == "__main__":
    # Declaring material properties for 1030 HR steel (machined)
    Sut = 68  # ksi
    Sy = 37.5
    sePrime = 0.5 * Sut

    # Accepting user input, data collected from problem statement
    moment = int(input("Moment: ")) / 1000
    torque = int(input("Torque: ")) / 1000
    diameter = float(input("Diameter: "))
    print("For sharp radius enter '0' for sharp radius enter '1'")
    radiusType = eval(input("Radius: "))
    print("For the safety factor against fatigue using goodman, enter '1'")
    print("For the safety factor against first cycle yield using vonMises stresses, enter '2'")
    print("For the first cycle yield using conservative approximation and infinite life using the goodman criteria, enter '3'")
    problemType = eval(input("Problem type: "))

    # Allowing the user to select sharp or wide radius
    if radiusType == 0:
        # Sharp radius
        Kt = 2.7
        Kts = 2.2
        rootR = sqrt(diameter * 0.02)
    elif radiusType == 1:
        # Wide radius
        Kt = 1.7
        Kts = 1.5
        rootR = sqrt(diameter * 0.1)

    # Allowing the user to select a problem type
    if problemType == 1:
        goodman_criteria_one()
    elif problemType == 2:
        vonmises_stress()
    else:
        goodman_criteria_two()
