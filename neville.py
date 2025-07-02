def neville(x_data, y_data, x_interpolate):
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

    return tableau[0][n - 1]

if __name__ == '__main__':
    # Example usage:
    x_data = [2,4,6]
    y_data = [5,6,8]
    x_interpolate = 4.5
    try:
        interpolated_value = neville(x_data, y_data, x_interpolate)
        print(f"\nInterpolated value at x = {x_interpolate} is y = {interpolated_value}")
    except ValueError as e:
        print(f"Error: {e}")