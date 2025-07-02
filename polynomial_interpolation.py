import numpy as np
import matplotlib.pyplot as plt

def polynomial_interpolation(table_points, x):
    """
    Perform polynomial interpolation using numpy.

    Args:
        table_points (list of tuples): List of (x, y) points.
        x (float): The x-coordinate to evaluate the polynomial.

    Returns:
        float: The interpolated y-value at x.
    """
    # Extract x and y values from the table points
    xs = np.array([pt[0] for pt in table_points])
    ys = np.array([pt[1] for pt in table_points])

    # Fit a polynomial of degree len(xs) - 1
    coeffs = np.polyfit(xs, ys, deg=len(xs) - 1)
    polynomial = np.poly1d(coeffs)

    # Evaluate the polynomial at the given x
    result = polynomial(x)

    # Print the polynomial and result
    print("\nThe polynomial:")
    print(polynomial)
    print(f"\nP({x}) = {result:.6f}")

    # Plot the polynomial and data points
    x_vals = np.linspace(xs.min() - 1, xs.max() + 1, 500)
    y_vals = polynomial(x_vals)

    plt.scatter(xs, ys, color='red', label='Data Points')
    plt.plot(x_vals, y_vals, label='Interpolated Polynomial', color='blue')
    plt.axvline(x=x, color='green', linestyle='--', label=f'X={x}')
    plt.title('Polynomial Interpolation')
    plt.xlabel('X')
    plt.ylabel('P(X)')
    plt.legend()
    plt.grid()
    plt.show()

    return result

if __name__ == '__main__':
    table_points = [(1, 0.8415), (2, 0.9093), (3, 0.1411)]
    x = 2.5
    print("Table Points:", table_points)
    print(f"Finding an approximation for x = {x}\n")
    polynomial_interpolation(table_points, x)