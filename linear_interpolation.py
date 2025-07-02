import matplotlib.pyplot as plt
from colors import bcolors

def linearInterpolation(table_points, point):
    """
Linear Interpolation/Extrapolation
    Args:
        table_points: List of tuples (x, y) representing the table points.
        point: The x-coordinate at which to evaluate the interpolation/extrapolation.

    Returns: the interpolated or extrapolated y-value at the given point.

    """
    if not table_points or len(table_points) < 2:
        raise ValueError("At least two table points are required for interpolation/extrapolation.")

    # Ensure table_points is sorted by x-values
    if any(table_points[i][0] > table_points[i + 1][0] for i in range(len(table_points) - 1)):
        raise ValueError("x-values must be sorted in ascending order.")

    result = None
    for i in range(len(table_points) - 1):
        x1, y1 = table_points[i]
        x2, y2 = table_points[i + 1]
        # Handle interpolation, including the boundary case for the last point
        if x1 <= point <= x2 or (i == len(table_points) - 2 and point == x2):
            result = y1 + ((y2 - y1) / (x2 - x1)) * (point - x1)
            break

    # Extrapolation
    if result is None:
        if point < table_points[0][0]:  # Before the first point
            x1, y1 = table_points[0]
            x2, y2 = table_points[1]
        elif point > table_points[-1][0]:  # After the last point
            x1, y1 = table_points[-2]
            x2, y2 = table_points[-1]
        else:
            raise ValueError("Point is out of range and cannot be interpolated or extrapolated.")

        result = y1 + ((y2 - y1) / (x2 - x1)) * (point - x1)

    # Plot the graph
    xs, ys = zip(*table_points)
    plt.plot(xs, ys, 'o-', label='Table Points', color='blue')
    plt.scatter([point], [result], color='red', label=f'Interpolated Point ({point}, {round(result, 4)})')
    plt.title('Linear Interpolation')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.grid(True)
    plt.show()

    print(bcolors.OKGREEN, f"\nThe approximation of the point {point} is: ", bcolors.ENDC, round(result, 4))
    return result

if __name__ == '__main__':
    table_points = [(0, 0), (1, 0.8415), (2, 0.9093), (3, 0.1411), (4, -0.7568), (5, -0.9589), (6, -0.2794)]
    x = 2.5
    print(bcolors.OKBLUE, "----------------- Interpolation & Extrapolation Methods -----------------\n", bcolors.ENDC)
    print(bcolors.OKBLUE, "Table Points: ", bcolors.ENDC, table_points)
    print(bcolors.OKBLUE, "Finding an approximation to the point: ", bcolors.ENDC, x)
    linearInterpolation(table_points, x)
    print(bcolors.OKBLUE, "\n---------------------------------------------------------------------------\n", bcolors.ENDC)