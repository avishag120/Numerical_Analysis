import sympy as sp
import math
from typing import Callable

def simpsons_rule(f: Callable[[float], float], a: float, b: float, n: int) -> float:
    if n <= 0:
        raise ValueError("Number of subintervals (n) must be greater than 0.")
    if n % 2 != 0:
        raise ValueError("Number of subintervals (n) must be even for Simpson's Rule.")

    h = (b - a) / n
    integral = f(a) + f(b)
    for i in range(1, n):
        x_i = a + i * h
        weight = 4 if i % 2 != 0 else 2
        integral += weight * f(x_i)
    return integral * h / 3

def error_bound_exact_sympy(f_sym, a: float, b: float, n: int) -> float:
    x = sp.Symbol('x', real=True)  # Important for avoiding re(x)/im(x)
    f4_sym = sp.diff(f_sym, x, 4)
    f4_abs = sp.lambdify(x, sp.Abs(f4_sym), modules=["numpy"])  # More robust

    sample_points = [a + i * (b - a) / 100 for i in range(101)]
    max_f4 = max(f4_abs(xi) for xi in sample_points)

    h = (b - a) / n
    return ((b - a) * h ** 4 * max_f4) / 180

if __name__ == '__main__':
    x = sp.Symbol('x', real=True)
    # Try replacing with sp.exp(x**2), sp.ln(x + 1), etc.
    f_sym = sp.exp(x ** 2)  # Example function: e^(x^2)
    f = sp.lambdify(x, f_sym, modules=["numpy"])
    a, b = 0, 1
    n = 4

    print(f"Division into n={n} sections")
    try:
        result = simpsons_rule(f, a, b, n)
        print(f"Numerical Integration of definite integral in range [{a}, {b}] is {result:.6f}")
        print(f"Estimated error of the approximation: {error_bound_exact_sympy(f_sym, a, b, n):.6f}")
    except Exception as e:
        print(f"Error: {e}")
