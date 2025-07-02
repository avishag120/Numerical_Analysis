import matplotlib.pyplot as plt
import numpy as np

def has_close_or_duplicate_x(x_data, tolerance=1e-9):
    """
    Checks if there are duplicate or very close x-values in the x_data array.

    Parameters:
    x_data (list): List of x-values to check.
    tolerance (float): The tolerance for considering two x-values as "close".

    Returns:
    bool: True if there are duplicate or close x-values, False otherwise.
    """


    n = len(x_data)
    for i in range(n):
        for j in range(i + 1, n):
            if abs(x_data[i] - x_data[j]) < tolerance:
                return True
    return False

def lagrange_interpolation(x_data, y_data, x):
    """
    Lagrange Interpolation

    Parameters:
    x_data (list): List of x-values for data points.
    y_data (list): List of y-values for data points.
    x (float): The x-value where you want to evaluate the interpolated polynomial.

    Returns:
    float: The interpolated y-value at the given x.
    """
    if len(x_data) != len(y_data):
        raise ValueError('the length of x-data have to be equal from the length of y-data')
    if has_close_or_duplicate_x(x_data):
        raise Exception("There are duplicate or very close x-values in the array.")
    n = len(x_data)
    result = 0.0

    for i in range(n):
        term = y_data[i]
        for j in range(n):
            if i != j:
                term *= (x - x_data[j]) / (x_data[i] - x_data[j])
        result += term

    return result



def plot_lagrange_interpolation(x_data, y_data, x_interpolate):
    # Generate x values for plotting the polynomial using numpy
    x_vals = np.linspace(min(x_data) - 1, max(x_data) + 1, 500)
    y_vals = [lagrange_interpolation(x_data, y_data, x) for x in x_vals]

    # Calculate the interpolated y value once
    y_interpolate = lagrange_interpolation(x_data, y_data, x_interpolate)

    # Plot the data points
    plt.scatter(x_data, y_data, color='red', label='Data Points')
    # Plot the Lagrange polynomial
    plt.plot(x_vals, y_vals, color='blue', label='Lagrange Polynomial')
    # Highlight the interpolated point
    plt.scatter([x_interpolate], [y_interpolate], color='green', label=f'Interpolated Point ({x_interpolate}, {y_interpolate:.4f})')

    plt.title('Lagrange Interpolation')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    try:
        x_data = [1, 2, 4]
        y_data = [1, 0, 1.5]
        x_interpolate = 3  # The x-value where you want to interpolate
        plot_lagrange_interpolation(x_data, y_data, x_interpolate)
    except ValueError as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")