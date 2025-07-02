import numpy as np
import matplotlib.pyplot as plt
from typing import Callable

def trapezoidal_rule_with_plot(func: Callable[[float], float], a: float, b: float, n: int) -> float:
    """
    Compute the integral of a function using the trapezoidal rule and visualize the integral surface.

    Parameters:
        func: The function to integrate.
        a: The start point of the interval.
        b: The end point of the interval.
        n: Number of sub-intervals (must be positive integer).

    Returns:
        Approximate integral of `func` from `a` to `b`.
    """
    if not callable(func):
        raise TypeError("func must be a callable function")
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    if a >= b:
        raise ValueError("a must be less than b")

    h = (b - a) / n
    x_points = np.linspace(a, b, n + 1)
    y_points = func(x_points)

    # Compute the integral
    total = 0.5 * (y_points[0] + y_points[-1])
    for i in range(1, n):
        total += y_points[i]
    integral = total * h

    # Plot the function
    x_vals = np.linspace(a, b, 500)
    y_vals = func(x_vals)
    plt.plot(x_vals, y_vals, label="Function", color="blue")

    # Shade the area under the curve
    plt.fill_between(x_vals, y_vals, color="cyan", alpha=0.5, label="Integral Surface")

    # Draw the trapezoids
    for i in range(n):
        plt.plot([x_points[i], x_points[i + 1]], [y_points[i], y_points[i + 1]], color="red")
        plt.fill_between([x_points[i], x_points[i + 1]], [y_points[i], y_points[i + 1]], color="orange", alpha=0.3)

    # Annotate the integral value
    plt.text((a + b) / 2, max(y_vals) * 0.8, f"Integral ≈ {integral:.6f}", fontsize=12, color="green", ha="center")

    plt.title("Trapezoidal Rule Approximation with Integral Surface")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()
    plt.grid(True)
    plt.show()

    return integral

# Example usage
if __name__ == "__main__":
    def example_function(x):
        return x ** 2

    result = trapezoidal_rule_with_plot(example_function, 0, 1, 10)
    print(f"Approximate integral: {result}")