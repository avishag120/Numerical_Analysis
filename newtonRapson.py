from colors import bcolors
import math

def isclose(a, b, rel_tol=1e-05, abs_tol=1e-08):
    """
    Check if two values are close to each other.
    """
    return abs(a - b) <= (abs_tol + rel_tol * abs(b))

def numerical_derivative(f, x, h=1e-5):
    """
    Calculate the numerical derivative of a function using the central difference method.
    """
    return (f(x + h) - f(x - h)) / (2 * h)

def newton_raphson(f, df, p0, tol=1e-6, max_iter=50):
    """
    Newton-Raphson method for finding roots of a function.
    """
    print(f"{bcolors.HEADER}Starting Newton-Raphson method with initial guess: {p0}{bcolors.ENDC}")
    print(f"{bcolors.BOLD}{'Iteration':<10}{'p0':<15}{'p1':<15}{'f(p0)':<15}{'df(p0)':<15}{bcolors.ENDC}")
    print("-" * 70)

    for i in range(max_iter):
        df_p0 = df(p0)
        if isclose(df_p0, 0):
            print(f"{bcolors.FAIL}Iteration {i}: Derivative is zero at p0 = {p0}, method cannot continue.{bcolors.ENDC}")
            return None  # Derivative is zero, cannot proceed
        p1 = p0 - f(p0) / df_p0
        print(f"{i:<10}{p0:<15.6f}{p1:<15.6f}{f(p0):<15.6f}{df_p0:<15.6f}")
        if abs(p1 - p0) < tol:
            print(f"{bcolors.OKGREEN}Converged to root after {i + 1} iterations: x = {p1:.6f}{bcolors.ENDC}")
            return p1  # Converged to a root
        p0 = p1

    print(f"{bcolors.FAIL}Method did not converge within the maximum number of iterations.{bcolors.ENDC}")
    return None  # Did not converge

def find_roots_in_section(f, section_start, section_end, tol=1e-6, max_iter=50):
    """
    Find roots of a function in a given section by dividing it into sub-sections of size 0.1.
    """
    step = 0.1
    current_start = section_start
    roots = []  # List to store all found roots

    print(f"{bcolors.HEADER}Searching for roots in the section [{section_start}, {section_end}]...{bcolors.ENDC}")
    while current_start < section_end:
        current_end = min(current_start + step, section_end)
        f_start = f(current_start)
        f_end = f(current_end)

        print(f"\n{bcolors.BOLD}Checking sub-section: [{current_start:.1f}, {current_end:.1f}]{bcolors.ENDC}")

        # Check for sign change
        if f_start * f_end > 0:
            print(f"{bcolors.WARNING}No sign change in sub-section [{current_start:.1f}, {current_end:.1f}].{bcolors.ENDC}")
        else:
            print(f"{bcolors.OKBLUE}Sign change detected. Searching for roots...{bcolors.ENDC}")
            root = newton_raphson(f, lambda x: numerical_derivative(f, x), (current_start + current_end) / 2, tol, max_iter)

            if root is not None and current_start <= root <= current_end:
                print(f"{bcolors.OKGREEN}Root found in sub-section [{current_start:.1f}, {current_end:.1f}]: x = {root:.6f}{bcolors.ENDC}")
                roots.append(root)  # Add the root to the list
            else:
                print(f"{bcolors.WARNING}No root found in sub-section [{current_start:.1f}, {current_end:.1f}].{bcolors.ENDC}")

        current_start += step

    # Final display of all found roots
    print(f"\n{bcolors.HEADER}Summary of Found Roots:{bcolors.ENDC}")
    if roots:
        for i, root in enumerate(roots, 1):
            print(f"{bcolors.OKBLUE}Root {i}: x = {root:.6f}{bcolors.ENDC}")
    else:
        print(f"{bcolors.FAIL}No roots were found in the given section.{bcolors.ENDC}")



if __name__ == '__main__':
    f = lambda x:  4 * x**3 -48 * x + 5  # Example function
    section_start = 2
    section_end = 9

    find_roots_in_section(f, section_start, section_end)