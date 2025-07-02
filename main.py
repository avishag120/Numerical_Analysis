from condition_of_linear_equations import condition_number, solve_gaussian
from GaussAndJacobi import gauss_seidel, jacobi_iterative
from bisection_method import bisection_method
from secant_method import secant_method
from newtonRapson import find_roots_in_section
from Simpson_method import simpsons_rule
from romberg_method import romberg_integration
from trapezoidal_refactored import trapezoidal_rule
from lagrange import lagrange_interpolation
from neville import neville
from linear_interpolation import linearInterpolation
from polynomial_interpolation import polynomialInterpolation
from cubic_spline import cubicSplineInterpolation
from machine_precision import calculate_machine_epsilon
from displaying_graphs import plot_points

from math import pi, exp, cos

# ==== Matrix Problems ====
gauss_A = [[2, 1.7, -2.5], [1.24, -2, -0.5], [3, 0.2, 1]]
gauss_b = [3.5, -1.2, 4.8]

# ==== Iterative Methods ====
iter_A = [[4, 2, 0], [2, 10, 4], [0, 4, 5]]
iter_b = [2, 6, 5]
x0 = [0.0, 0.0, 0.0]

# ==== Integration ====
f_simpson = lambda x: exp(x ** 2)
f_romberg = lambda x: 1 / (2 + x ** 4)
f_trap = lambda x: x ** 2

a_int, b_int, n_int = 0, 1, 4

# ==== Interpolation ====
x_data = [1, 2, 3]
y_data = [0.8415, 0.9093, 0.1411]
x_val = 2.5

x_spline = [0, pi/6, pi/4, pi/3, pi/2]
y_spline = [0, 0.5, 0.7071, 0.8660, 1.0]
x_interp = pi/3

# ==== Root Finding ====
f_bisect = lambda x: x ** 3 - x - 1
f_newton = lambda x: 4 * x ** 3 - 48 * x + 5
f_secant = lambda x: x ** 3 - cos(x)

def generate_linspace(start, end, num_points):
    step = (end - start) / (num_points - 1)
    return [start + i * step for i in range(num_points)]

def run():
    while True:
        print("\n=== Numerical Analysis Main Menu ===")
        print("1. Solve Ax = b using Gaussian Elimination")
        print("2. Calculate Condition Number")
        print("3. Gauss-Seidel / Jacobi Method")
        print("4. Integration (Simpson, Romberg, Trapezoidal)")
        print("5. Interpolation (Lagrange, Neville, Linear, Polynomial, Spline)")
        print("6. Root Finding (Bisection, Newton-Raphson, Secant)")
        print("7. Machine Epsilon")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if not choice.isdigit() or int(choice) not in range(0, 8):
            print("Invalid choice. Please enter a number between 0 and 7.")
            continue

        choice = int(choice)

        if choice == 1:
            print("\nSolution x:", solve_gaussian(gauss_A, gauss_b))

        elif choice == 2:
            condition_number(gauss_A)

        elif choice == 3:
            method = input("Enter 1 for Gauss-Seidel, 2 for Jacobi: ")
            if method == '1':
                gauss_seidel(iter_A, iter_b, x0)
            elif method == '2':
                jacobi_iterative(iter_A, iter_b, x0)
            else:
                print("Invalid method choice.")

        elif choice == 4:
            print("Simpson:", simpsons_rule(f_simpson, a_int, b_int, n_int))
            print("Romberg:", romberg_integration(f_romberg, 0, 1, 5))
            print("Trapezoidal:", trapezoidal_rule(f_trap, 0, 1, 100))

            show_plot = input("Would you like to display the plot for the integration methods? (y/n): ").lower() == 'y'
            if show_plot:
                x_vals = generate_linspace(a_int, b_int, 100)
                plt_vals = [f_trap(x) for x in x_vals]
                plot_points(x_vals, plt_vals, "Function for Integration")

        elif choice == 5:
            print("Lagrange:", lagrange_interpolation(x_data, y_data, x_val))
            print("Neville:", neville(x_data, y_data, x_val))
            print("Linear:", linearInterpolation(list(zip(x_data, y_data)), x_val))
            print("Spline:", cubicSplineInterpolation(x_spline, y_spline, x_interp))
            print("Polynomial: \u2B07", )
            polynomialInterpolation(list(zip(x_data, y_data)), x_val)
        elif choice == 6:
            print("Bisection:")
            try:
                b_root = bisection_method(f_bisect, 1, 2, 1e-6)
                print(f"Bisection Root: x = {b_root}")
            except Exception as e:
                print("Bisection Error:", e)

            print("Newton-Raphson:")
            try:
                find_roots_in_section(f_newton, 2, 9)
            except Exception as e:
                print("Newton-Raphson Error:", e)

            print("Secant:")
            try:
                secant_method(f_secant, 1.0, 0.0)
            except Exception as e:
                print("Secant Error:", e)

            show_plot = input("Would you like to display the plot of the function for root finding? (y/n): ").lower() == 'y'
            if show_plot:
                x_vals = generate_linspace(0, 5, 200)
                y_vals = [f_bisect(x) for x in x_vals]
                plot_points(x_vals, y_vals, "Function for Root Finding")

        elif choice == 7:
            eps = calculate_machine_epsilon()
            print("Machine Epsilon:", eps)

        elif choice == 0:
            print("Exiting.")
            break

if __name__ == '__main__':
    run()
