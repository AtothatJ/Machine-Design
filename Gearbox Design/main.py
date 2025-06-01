from numpy import pi


def user_inputs():
    """
    Accepts user input, then calls the corresponding method of calculation. Features a while loop to keep the user from
    re-running the script. Also features a try statement incase a user inputs the wrong type of value
    """

    while True:
        print("\nPlease input the number of the section you would like to calculate")
        print("\tPower requirements: 1")
        print("\tShaft Analysis (fatigue and static): 2")
        print("\tEnd script: 0")

        try:
            user_choice = int(input("\tSection: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if user_choice == 1:
            power_requirements()
        elif user_choice == 2:
            print("Something else is not implemented yet.")
        elif user_choice == 0:
            break
        else:
            print("Invalid option. Please select 1 or 2.")


def power_requirements():
    """
    Calculates the horsepower and torque required at the output of the shaft. Power in == power out
    """
    # Declaring given shaft input values
    H = 9.5
    Wi = 3000
    Wo = 400

    # Finding input torque
    Ti = H / Wi * (550 * 60 / (2 * pi))

    # Finding torque output
    To = H / Wo * (550 * 60 / (2 * pi))

    print("Input Torque: " + str(Ti))
    print("Output Torque: " + str(To))

def analysis():
    


if __name__ == '__main__':
    user_inputs()
