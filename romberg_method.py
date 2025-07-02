import numpy as np
from colors import bcolors
import matplotlib.pyplot as plt
import math


def romberg_integration_with_plot(func, a, b, n, epsilon=1e-8):
    """
    Romberg Integration with visualization of the integral surface.

    Parameters:
    func (function): Function to integrate.
    a (float): Lower integration limit.
    b (float): Upper integration limit.
    n (int): Maximum number of iterations.
    epsilon (float): Convergence threshold.

    Returns:
    float: Approximated definite integral of func over [a, b].
    """

    if n < 1:
        raise ValueError("Number of iterations n must be >= 1.")
    if a == b:
        return 0.0

    h = b - a
    R = np.zeros((n, n), dtype=float)

    # First trapezoidal approximation
    fa, fb = func(a), func(b)
    if not (np.isfinite(fa) and np.isfinite(fb)):
        raise ValueError("Function returned non-finite value at interval endpoints.")

    R[0, 0] = 0.5 * h * (fa + fb)

    for i in range(1, n):
        h /= 2
        sum_term = 0.0

        for k in range(1, 2**i, 2):
            x = a + k * h
            fx = func(x)
            if not np.isfinite(fx):
                raise ValueError(f"Function returned invalid value at x = {x}")
            sum_term += fx

        R[i, 0] = 0.5 * R[i - 1, 0] + h * sum_term

        for j in range(1, i + 1):
            R[i, j] = R[i, j - 1] + (R[i, j - 1] - R[i - 1, j - 1]) / ((4**j) - 1)

        if i > 0 and abs(R[i, i] - R[i - 1, i - 1]) < epsilon:
            integral_value = R[i, i]
            break
    else:
        integral_value = R[n - 1, n - 1]

    # Plot the function and integral surface
    x_vals = np.linspace(a, b, 500)
    y_vals = func(x_vals)

    plt.plot(x_vals, y_vals, label="Function", color="blue")
    plt.fill_between(x_vals, y_vals, color="cyan", alpha=0.5, label="Integral Surface")
    plt.title("Romberg Integration with Integral Surface")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()
    plt.grid(True)

    # Annotate the integral value
    plt.text((a + b) / 2, max(y_vals) * 0.8, f"Integral ≈ {integral_value:.6f}", fontsize=12, color="green", ha="center")
    plt.show()

    return integral_value

def f(x):
    return 1/(2+x ** 4)


if __name__ == '__main__':

    a = 0
    b = 1
    n = 5
    integral = romberg_integration_with_plot(f, a, b, n)

    print( f" Division into n={n} sections ")
    print(bcolors.OKBLUE, f"Approximate integral in range [{a},{b}] is {integral}", bcolors.ENDC)