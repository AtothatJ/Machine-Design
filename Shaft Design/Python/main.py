from math import pi, sqrt


def get_user_input(problemType):
    """
    Handles user input and stores the radius type, problem type, and related values.
    """
    moment = float(input("Moment (lb-in): ")) / 1000
    torque = float(input("Torque (lb-in): ")) / 1000

    if problemType == 4:
        diameter = 0.3
    else:
        diameter = float(input("Diameter (in): "))

    print("For... \n\t Sharp Radius: 0  \n\t Wide Radius: 1 \n\t Keyway: 2"
          " \n\t Retaining groove: 3")
    radiusType = int(input("Radius: "))

    if radiusType == 0:
        Kt = 2.7
        Kts = 2.2
        rootR = sqrt(diameter * 0.02)
    elif radiusType == 1:
        Kt = 1.7
        Kts = 1.5
        rootR = sqrt(diameter * 0.1)
    elif radiusType == 2:
        Kt = 2.14
        Kts = 3.0
        rootR = sqrt(diameter * 0.02)
    elif radiusType == 3:
        Kt = 5
        Kts = 3
        rootR = 5
    else:
        Kt = Kts = rootR = 0

    return moment, torque, diameter, Kt, Kts, rootR


def goodman_criteria(moment, torque, diameter, Kt, Kts, rootR):
    """
    Calculates the Goodman criteria for questions 1-10.
    """
    Kf = kf(rootR, Kt)
    Kfs = kfs(rootR, Kts)

    a, b = 2, -0.217
    Ka = a * Sut ** b
    Kb = 0.879 * diameter ** -0.107
    Kc = Kd = Ke = 1
    Se = Ka * Kb * Kc * Kd * Ke * sePrime

    A = sqrt(4 * (Kf * moment) ** 2)
    B = sqrt(3 * (Kfs * torque) ** 2)

    return ((pi * diameter ** 3) / 16) * ((A / Se) + (B / Sut)) ** -1


def vonmises_stress(moment, torque, diameter, Kt, Kts, rootR):
    """
    Calculates the safety factor against first cycle yielding, using Von Mises.
    """
    Kf = kf(rootR, Kt)
    Kfs = kfs(rootR, Kts)

    sigma = (32 * Kf * moment) / (pi * diameter ** 3)
    tau = (16 * Kfs * torque) / (pi * diameter ** 3)

    sigmaPrimeMax = sqrt((sigma ** 2) + (3 * tau ** 2))

    return Sy / sigmaPrimeMax


def goodman_criteria_two(moment, torque, diameter, Kt, Kts, rootR):
    """
    Calculates the Goodman criteria for questions 16-20.
    """
    sigmaPrimeA = (16 / (pi * diameter ** 3)) * sqrt(4 * (kf(rootR, Kt) * moment) ** 2)
    sigmaPrimeM = (16 / (pi * diameter ** 3)) * sqrt(3 * (kfs(rootR, Kts) * torque) ** 2)

    return Sy / (sigmaPrimeA + sigmaPrimeM)


def kf(rootR, Kt):
    """
    Calculates the bending fatigue stress-concentration.
    """
    bendingRootA = 0.246 - (3.08 * 10 ** -3) * Sut + (1.51 * 10 ** -5) * Sut ** 2 - (2.67 * 10 ** -8) * Sut ** 3
    qBending = 1 / (1 + (bendingRootA / rootR))
    return 1 + qBending * (Kt - 1)


def kfs(rootR, Kts):
    """
    Calculates the torsional fatigue stress-concentration.
    """
    torsionalRootA = 0.190 - (2.51 * 10 ** -3) * Sut + (1.35 * 10 ** -5) * Sut ** 2 - (2.67 * 10 ** -8) * Sut ** 3
    qTorsional = 1 / (1 + (torsionalRootA / rootR))
    return 1 + qTorsional * (Kts - 1)


def main():
    """
    Main execution function.
    """
    while True:
        print("For the safety factor against fatigue using Goodman, enter '1'")
        print("For the safety factor against first cycle yield using Von Mises stresses, enter '2'")
        print("For the first cycle yield using conservative approximation and first cycle yield using the Goodman criteria, enter '3'")
        print("To exit the program, enter '0'")
        problemType = int(input("Problem type: "))

        if problemType == 1:
            moment, torque, diameter, Kt, Kts, rootR = get_user_input(problemType)
            result = goodman_criteria(moment, torque, diameter, Kt, Kts, rootR)
            print('The factor of safety calculated from the Goodman criteria is:', result)
        elif problemType == 2:
            moment, torque, diameter, Kt, Kts, rootR = get_user_input(problemType)
            result = vonmises_stress(moment, torque, diameter, Kt, Kts, rootR)
            print('The factor of safety calculated from the Von Mises stress is:', result)
        elif problemType == 3:
            moment, torque, diameter, Kt, Kts, rootR = get_user_input(problemType)
            result = goodman_criteria_two(moment, torque, diameter, Kt, Kts, rootR)
            print('The factor of safety calculated from the Goodman criteria is:', result)
        elif problemType == 0:
            break


if __name__ == "__main__":
    Sut = 68  # ksi
    Sy = 37.5
    sePrime = 0.5 * Sut
    main()
