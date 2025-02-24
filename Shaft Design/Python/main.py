from math import pi, sqrt

# Declaring given info from the problem statement
moment = 400
torque = 100
diameter = 0.75
reliability = 0.5

# KT KTS values for sharp radius
#Kt = 2.7
#Kts = 2.2

# KT KTS values for wide radius
Kt = 1.7
Kts = 1.5

# Declaring material properties for 1030 machined steel
Sut = 68  # ksi
Sy = 42000
sePrime = 0.5 * Sut


def goodman_criteria_one():
    """
    Calculates the goodman criteria for questions 1-10. Assuming machined steel
    """
    bendingRootA = 0.246 - (3.08 * 10 ** -3) * Sut + (1.51 * 10 ** -5) * Sut ** 2 - (2.67 * 10 ** -8) * Sut ** 3
    torsionalRootA = 0.190 - (135 * 10 ** -3) * Sut + (1.35 * 10 ** -6) * Sut ** 2 - (2.67 * 10 ** -8) * Sut ** 3
    rootR = sqrt(diameter/2)
    qBending = 1 / (1 + (bendingRootA / rootR))
    qTorsional = 1 / (1 + (torsionalRootA / rootR))
    Kf = 1 + (Kt * qBending)
    Kfs = 1 + (Kts * qTorsional)
    SePrime = 0.5*Sut
    a = 2
    b = -0.217
    Ka = a*Sut**b
    kb = 0.879 * diameter ** -0.107
    kc = 1
    # Problem statement does not include a temp, so skipping Kd
    za = 2.326
    Ke = 1 - 0.08 * za
    Se = ka * kb * kc * ke * sePrime
    Se = Ka * Kb * Kc * Kd * Ke * SePrime
    SigmaPrimeA = sqrt( (32*) )
    SigmaPrimeM = sqrt(  )
    # Calculating Goodman Criterion
    Nf = 1 / ((SigmaPrimeA / Se) + (SigmaPrimeM / Sut))
    # Showing the answer to the user
    print('The factor of safety calculated from the Goodman criteria is : ' + str(Nf))


def vonmises_stress():
    """
    Calculates the safety factor against first cycle yielding, using Von Mises.
    Questions 11-20
    """
    kf = 1

    # Calculating bending stress
    sigma = kf * 32 * moment / (pi * diameter ** 3)

    # Calculating shear stress
    tau = 16 * torque / (pi * diameter ** 3)

    # Calculating von mises stress
    sigmaPrime = sqrt(sigma ** 2 + 3 * tau ** 2)

    # Calculating the von mises safety factor
    safetyFactor = Sy / sigmaPrime

    # Showing the answer to the user
    print('The factor of safety calculated from the von Mises stress is : ' + str(safetyFactor))


def goodman_criteria_two():
    """
    Calculates the goodman criteria for questions 21-30.
    """
    Nf = 1
    print('The factor of safety calculated from the Goodman criteria is : ' + str(Nf))


if __name__ == "__main__":
    goodman_criteria_one()
    vonmises_stress()
    goodman_criteria_two()
