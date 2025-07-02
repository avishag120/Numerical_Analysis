import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from typing import Callable

def simpsons_rule_with_colored_surface(func, a, b, n):
    """
    Compute the integral of a function using Simpson's rule and visualize the integral surface.

    Parameters:
        func: The function to integrate.
        a: The start of the interval.
        b: The end of the interval.
        n: Number of subintervals (must be even).

    Returns:
        Approximate integral of `func` from `a` to `b`.
    """
    if n % 2 != 0:
        raise ValueError("Number of subintervals (n) must be even.")

    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = func(x)

    # Simpson's rule formula
    integral = h / 3 * (y[0] + 4 * sum(y[1:n:2]) + 2 * sum(y[2:n-1:2]) + y[-1])

    # Plot the function and shaded area
    x_vals = np.linspace(a, b, 500)
    y_vals = func(x_vals)
    plt.plot(x_vals, y_vals, label="Function", color="blue")
    plt.fill_between(x_vals, y_vals, color="cyan", alpha=0.5, label="Integral Surface")
    plt.title("Simpson's Rule Approximation")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()
    plt.grid(True)
    plt.show()

    return integral

def error_bound_exact_sympy(f_sym, a: float, b: float, n: int) -> float:
    """
    Calculate the error bound for the Simpson's Rule approximation using SymPy.
    This function computes the fourth derivative of the given function symbolically,
    evaluates its absolute value at sample points within the interval [a, b],
    and uses the maximum value to estimate the error bound.

    Args:
        f_sym: sympy expression: The symbolic representation of the function to integrate.
        a: float: The start point of the interval.
        b: float: The end point of the interval.
        n: int: Number of subintervals (must be a positive even integer).

    Returns:
        float: Estimated error bound of the Simpson's Rule approximation.

    """
    x = sp.Symbol('x', real=True)  # Important for avoiding re(x)/im(x)
    f4_sym = sp.diff(f_sym, x, 4)
    f4_abs = sp.lambdify(x, sp.Abs(f4_sym), modules=["numpy"])  # More robust

    sample_points = [a + i * (b - a) / 100 for i in range(101)]
    max_f4 = max(f4_abs(xi) for xi in sample_points)

    h = (b - a) / n
    return ((b - a) * h ** 4 * max_f4) / 180

if __name__ == '__main__':
    x = sp.Symbol('x', real=True)
    f_sym = sp.exp(x ** 2)  # Example function: e^(x^2)
    f = sp.lambdify(x, f_sym, modules=["numpy"])
    a, b = 0, 1
    n = 4

    print(f"Division into n={n} sections")
    try:
        result, error = simpsons_rule_with_colored_surface(f, a, b, n), error_bound_exact_sympy(f_sym, a, b, n)
        print(f"Numerical Integration of definite integral in range [{a}, {b}] is {result:.6f}")
        print(f"Estimated error of the approximation: {error:.6f}")
    except Exception as e:
        print(f"Error: {e}")
