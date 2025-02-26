from math import pi, sqrt

def goodman_criteria_one():
    """
    Calculates the goodman criteria for questions 1-10
    """
    Kf = kf()
    Kfs = kfs()

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
    B = sqrt(3 * (Kfs * torque) ** 2)

    # Calculating safety factor
    Nf = ((pi * diameter ** 3) / 16) * ((A / Se) + (B / Sut)) ** -1

    # Showing the answer to the user
    print('The factor of safety calculated from the Goodman criteria is : ' + str(Nf))

def vonmises_stress():
    """
    Calculates the safety factor against first cycle yielding, using Von Mises.
    Questions ___
    """
    Kf = kf()
    Kfs = kfs()

    # Calculating sigma and Tau
    sigma = (32 * Kf * moment) / (pi * diameter ** 3)
    tau = (16 * Kfs * torque) / (pi * diameter ** 3)

    # Calculating sigma ' max
    sigmaPrimeMax = sqrt((sigma ** 2) + (3*tau**2))

    # Calculating safety factor for von mises
    Ny = Sy / sigmaPrimeMax
    # Showing the answer to the user
    print('The factor of safety calculated from the von mises stress is : ' + str(Ny))

def goodman_criteria_two():
    """
    Calculates the goodman criteria for questions ____
    """

    sigmaPrimeA = (16 / (pi * diameter ** 3)) * sqrt(4 * (kf() * moment)**2)
    sigmaPrimeM = (16 / (pi * diameter ** 3)) * sqrt(3 * (kfs() * torque)**2)
    Ny = Sy / (sigmaPrimeA + sigmaPrimeM)
    print('The factor of safety calculated from the Goodman criteria is : ' + str(Ny))

def kf():
    """
    Calculates the bending fatigue stress-concentration
    """
    # Calculating sqrt(a)
    bendingRootA = 0.246 - (3.08 * 10 ** -3) * Sut + (1.51 * 10 ** -5) * Sut ** 2 - (2.67 * 10 ** -8) * Sut ** 3

    # Calculating q values
    qBending = 1 / (1 + (bendingRootA / rootR))

    # converting Kt to Kf
    Kf = 1 + qBending * (Kt - 1)
    return Kf

def kfs():
    """
    Calculates the torsional fatigue stress-concentration
    """
    # Calculating sqrt(a)
    torsionalRootA = 0.190 - (2.51 * 10 ** -3) * Sut + (1.35 * 10 ** -5) * Sut ** 2 - (2.67 * 10 ** -8) * Sut ** 3

    # Calculating q values
    qTorsional = 1 / (1 + (torsionalRootA / rootR))

    # Converting Kts to Kfs
    Kfs = 1 + qTorsional * (Kts - 1)
    return Kfs

if __name__ == "__main__":
    # Declaring material properties for 1030 HR steel (machined)
    Sut = 68  # ksi
    Sy = 37.5
    sePrime = 0.5 * Sut

    # Accepting user input, data collected from problem statement
    moment = int(input("Moment: ")) / 1000
    torque = int(input("Torque: ")) / 1000
    diameter = float(input("Diameter: "))
    print("For... \n\t Sharp Radius: 0  \n\t Wide Radius: 1 \n\t Keyway: 2")
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
    elif radiusType == 2:
        Kt = 2.14
        Kts = 3.0
        rootR = sqrt(diameter * 0.02)

    # Allowing the user to select a problem type
    if problemType == 1:
        goodman_criteria_one()
    elif problemType == 2:
        vonmises_stress()
    elif problemType == 3:
        goodman_criteria_two()