import math
from typing import Callable

def simpsons_rule(f: Callable[[float], float], a: float, b: float, n: int) -> float:
    """
    Simpson's Rule for Numerical Integration.

    Parameters:
    f (Callable[[float], float]): The function to be integrated.
    a (float): The lower limit of integration.
    b (float): The upper limit of integration.
    n (int): The number of subintervals (must be even and greater than 0).

    Returns:
    float: The approximate definite integral of the function over [a, b].
    """
    if n <= 0:
        raise ValueError("Number of subintervals (n) must be greater than 0.")
    if n % 2 != 0:
        raise ValueError("Number of subintervals (n) must be even for Simpson's Rule.")

    h = (b - a) / n  # Step size
    integral = f(a) + f(b)  # Initialize with endpoints

    # Apply Simpson's Rule
    for i in range(1, n):
        x_i = a + i * h
        weight = 4 if i % 2 != 0 else 2  # Alternate weights: 4 for odd, 2 for even
        integral += weight * f(x_i)

    integral *= h / 3  # Final scaling factor
    return integral

def error_calculation_exact(a: float, b: float, n: int) -> float:
    """
    Calculate the error of Simpson's Rule approximation using the exact fourth derivative.

    Parameters:
    a (float): The lower limit of integration.
    b (float): The upper limit of integration.
    n (int): The number of subintervals.

    Returns:
    float: The estimated error of the approximation.
    """
    max_fourth_derivative = 1  # Maximum value of |sin(x)| in [0, pi]
    error_bound = ((b - a) ** 5 / (180 * n ** 4)) * max_fourth_derivative
    return error_bound


if __name__ == '__main__':
    # Example usage
    f = lambda x: math.sin(x)  # Function to integrate
    a, b = 0, math.pi  # Integration limits
    n = 4  # Number of subintervals (must be even)

    print(f"Division into n={n} sections")
    try:
        result = simpsons_rule(f, a, b, n)
        print(f"Numerical Integration of definite integral in range [{a}, {b}] is {result:.6f}")
        print(f"Estimated error of the approximation: {error_calculation_exact(a, b, n):.6f}")
    except ValueError as e:
        print(f"Error: {e}")



