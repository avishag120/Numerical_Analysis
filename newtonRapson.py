import numpy as np
from colors import bcolors


def newton_raphson(f, df, p0, tol, max_iter=50):
    """
    Newton-Raphson method for finding roots of a function.

    :param f: Function for which the root is to be found
    :param df: Derivative of the function
    :param p0: Initial guess
    :param tol: Tolerance for stopping criterion
    :param max_iter: Maximum number of iterations
    :return: Approximate root or None if not found
    """

    print("{:<10} {:<15} {:<15}".format("Iteration", "p0", "p1"))
    for i in range(max_iter):
        df_p0 = df(p0)
        if (abs(df_p0 - 0) <= tol):
            print("Derivative is zero at p0, method cannot continue.")
            return None

        p1 = p0 - f(p0) / df_p0

        print("{:<10} {:<15.9f} {:<15.9f}".format(i, p0, p1))

        if abs(p1 - p0) < tol:
            print(bcolors.OKGREEN, f"\nConverged to root: x = {p1:.9f}", bcolors.ENDC)
            return p1

        p0 = p1

    print(bcolors.FAIL, "\nMethod did not converge within the maximum number of iterations.", bcolors.ENDC)
    return None

if __name__ == '__main__':
    f = lambda x: x**2
    df = lambda x: 2*x
    p0 = 0
    tol = 1e-6
    max_iter = 100

    root = newton_raphson(f, df, p0, tol, max_iter)
    if root is not None:
        print(bcolors.OKBLUE, f"\nThe equation f(x) has an approximate root at x = {root:.9f}", bcolors.ENDC)