from math import pi, sqrt

# Declaring given info from the problem statement
moment = 100
torque = 200
diameter = 0.75

# Declaring material properties for 1030 HR steel
# Declaring material properties (HR 1030 Steel)
Sut = 68  # ksi
Sy = 42000
sePrime = 0.5 * Sut

def goodman_criteria_one():
    """
    Calculates the goodman criteria for questions 1-10.
    The constants are assuming HR 1030 Steel material properties.
    """
    # Calculating K values
    a = 11
    b = -0.650
    ka = a*Sut**b
    kb = 0.879*diameter**-0.107
    kc = 1
    # Problem statement does not include a temp, so skipping Kd
    za = 2.326
    ke = 1- 0.08*za
    Se = ka * kb * kc * ke * sePrime
    kf = 1.5
    # Calculating alternating bending stress
    sigmaA = kf * (32 * moment)/ (pi * diameter**3)
    # Calculating alternating torsional stress
    tauA = kf * (16 * torque) / (pi*diameter**3)

    # Declaring mean torsional stress and bending stress
        # Due to the loading configuration, there are no mean stresses
    tauM = sigmaM = 0

    # Calculating Von mises alternating stress
    sigmaPrimeA = sqrt( sigmaA**2 + 3 * tauA**2)

    # Calculating Von mises mean stress
    sigmaPrimeM = sqrt( sigmaM**2 + 3 * tauM**2)

    # Calculating Goodman Criterion
    Nf = 1 / ( (sigmaPrimeA/Se) + (sigmaPrimeM/Sut) )

    # Showing the answer to the user
    print('The factor of safety calculated from the Goodman criteria is : ' + str(Nf))

def vonmises_stress():
    """
    Calculates the safety factor against first cycle yielding, using Von Mises.
    Questions 11-20
    """

    # Calculating bending stress
    sigma = kf * 32*moment / (pi*diameter**3)

    # Calculating shear stress
    tau = 16*torque / (pi*diameter**3)

    # Calculating von mises stress
    sigmaPrime = sqrt(sigma**2 + 3*tau**2)

    # Calculating the von mises safety factor
    safetyFactor = Sy / sigmaPrime

    # Showing the answer to the user
    print('The factor of safety calculated from the Goodman criteria is : ' + str(safetyFactor))

if __name__ == "__main__":
    #goodman_criteria_one()
    vonmises_stress()