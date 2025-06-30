from colors import bcolors

def calculate_machine_epsilon():
    """Calculate the machine epsilon, which is the smallest number that, when added to 1.0, results in a value greater than 1.0."""
    epsilon = 1.0
    while (1.0 + epsilon) > 1.0:
        epsilon /= 2.0
    return epsilon * 2.0

if __name__ == '__main__':
    machine_epsilon_value = calculate_machine_epsilon()
    print(f"{bcolors.OKBLUE}Machine Precision  : {machine_epsilon_value}{bcolors.ENDC}")

    expression_value = abs(0.1+0.1+0.1 - 0.3)
    print("\nResult of abs(0.1+0.1+0.1 - 0.3) :")
    print(f"{bcolors.FAIL}Before using machine epsilon: {expression_value}{bcolors.ENDC}")

    corrected_expression_value = expression_value - machine_epsilon_value
    print(f"{bcolors.OKGREEN}After correcting with machine epsilon: {corrected_expression_value}{bcolors.ENDC}")