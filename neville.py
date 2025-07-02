import matplotlib.pyplot as plt

def neville_with_plot(x_data, y_data, x_interpolate):
    """
    Neville's Interpolation Method with visualization.
    Args:
        x_data: List of x-coordinates (must be unique).
        y_data: List of y-coordinates corresponding to x_data.
        x_interpolate: The x-coordinate at which to evaluate the interpolation.

    Returns: the interpolated y-value at the given x_interpolate.
    """
    n = len(x_data)
    if n != len(y_data):
        raise ValueError("x_data and y_data must have the same length.")

    if n == 0:
        raise ValueError("Empty x_data or y_data is not allowed.")

    if len(set(x_data)) != n:
        raise ValueError("x_data must contain unique values.")

    # Initialize the tableau
    tableau = [[0.0] * n for _ in range(n)]

    for i in range(n):
        tableau[i][0] = y_data[i]

    for j in range(1, n):
        for i in range(n - j):
            tableau[i][j] = ((x_interpolate - x_data[i + j]) * tableau[i][j - 1] -
                             (x_interpolate - x_data[i]) * tableau[i + 1][j - 1]) / (x_data[i] - x_data[i + j])

    interpolated_value = tableau[0][n - 1]

    # Plot the data points
    plt.scatter(x_data, y_data, color="red", label="Data Points")
    plt.plot(x_data, y_data, color="blue", linestyle="--", label="Interpolation Line")

    # Highlight the interpolated point
    plt.scatter([x_interpolate], [interpolated_value], color="green", label=f"Interpolated Point ({x_interpolate}, {interpolated_value:.2f})")

    plt.title("Neville's Interpolation")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()
    plt.grid(True)
    plt.show()

    return interpolated_value

if __name__ == '__main__':
    # Example usage:
    x_data = [2, 4, 6]
    y_data = [5, 6, 8]
    x_interpolate = 4.5
    try:
        interpolated_value = neville_with_plot(x_data, y_data, x_interpolate)
        print(f"\nInterpolated value at x = {x_interpolate} is y = {interpolated_value}")
    except ValueError as e:
        print(f"Error: {e}")