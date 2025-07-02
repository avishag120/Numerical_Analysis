import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from typing import Callable

def simpsons_rule_with_colored_surface(f: Callable[[float], float], f_sym, a: float, b: float, n: int):
    if n <= 0:
        raise ValueError("Number of subintervals (n) must be greater than 0.")
    if n % 2 != 0:
        raise ValueError("Number of subintervals (n) must be even for Simpson's Rule.")

    h = (b - a) / n
    x_vals = np.linspace(a, b, 500)
    y_vals = f(x_vals)

    # Plot the function
    plt.plot(x_vals, y_vals, label="Function", color="blue")

    # Shade the area under the curve
    plt.fill_between(x_vals, y_vals, color="cyan", alpha=0.5, label="Integral Surface")

    # Plot the subinterval points
    x_points = np.linspace(a, b, n + 1)
    y_points = f(x_points)
    plt.scatter(x_points, y_points, color="red", label="Subinterval Points")

    integral = f(a) + f(b)
    for i in range(1, n):
        x_i = a + i * h
        weight = 4 if i % 2 != 0 else 2
        integral += weight * f(x_i)

    # Calculate the integral and error bound
    integral_value = integral * h / 3
    error_bound = error_bound_exact_sympy(f_sym, a, b, n)

    # Annotate the integral value and error bound on the graph
    plt.text((a + b) / 2, max(y_vals) * 0.8, f"Integral ≈ {integral_value:.6f}", fontsize=12, color="green", ha="center")
    plt.text((a + b) / 2, max(y_vals) * 0.7, f"Error Bound ≈ {error_bound:.6f}", fontsize=12, color="orange", ha="center")

    plt.title("Simpson's Rule Approximation with Colored Surface")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()
    plt.grid(True)
    plt.show()

    return integral_value, error_bound


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
        result, error = simpsons_rule_with_colored_surface(f, f_sym, a, b, n)
        print(f"Numerical Integration of definite integral in range [{a}, {b}] is {result:.6f}")
        print(f"Estimated error of the approximation: {error:.6f}")
    except Exception as e:
        print(f"Error: {e}")
