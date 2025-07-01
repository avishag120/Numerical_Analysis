from typing import Callable

def trapezoidal_rule(func: Callable[[float], float], a: float, b: float, n: int) -> float:
    """
    Compute the integral of a function using the trapezoidal rule.

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
    total = 0.5 * (func(a) + func(b))
    for i in range(1, n):
        total += func(a + i * h)
    return total * h

# Example usage
if __name__ == "__main__":
    def example_function(x):
        return x ** 2

    result = trapezoidal_rule(example_function, 0, 1, 100)
    print(f"Approximate integral: {result}")
