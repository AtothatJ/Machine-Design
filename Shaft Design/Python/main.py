from math import pi, sqrt

# Declaring given info from the problem statement
moment = 400
torque = 100
diameter = 0.75


# Declaring material properties for 1030 machined steel
Sut = 68  # ksi
Sy = 42000
sePrime = 0.5 * Sut

def goodman_criteria_one():
    """
    Calculates the goodman criteria for questions 1-10.
    """
    sharp = 0
    if sharp == 1:
        rBending = 2.7
        rTorsion = 2.2
    elif sharp == 0
        rBending = 1.7
        rTorsion = 1.5
    Kf =
    Kfs =
    SePrime = 0.5*Sut
    Ka =
    Kb =
    Kc =
    Kd =
    Ke =
    Se = Ka * Kb * Kc * Kd * Ke * SePrime
    SigmaPrimeA = sqrt( (32*) )
    SigmaPrimeM = sqrt(  )
    # Calculating Goodman Criterion
    Nf = 1 / ((sigmaPrimeA / Se) + (sigmaPrimeM / Sut))

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
