from colors import bcolors
from math import pi

def cubicSplineInterpolation(xList, yList, point):
    if len(xList) != len(yList) or len(xList) < 2:
        raise ValueError("xList and yList must have the same length and contain at least two points.")

    # Ensure xList is sorted and unique
    if sorted(xList) != xList or len(set(xList)) != len(xList):
        raise ValueError("xList must be sorted in ascending order with unique values.")

    n = len(xList) - 1  # Number of intervals
    h = [xList[i + 1] - xList[i] for i in range(n)]  # Step sizes

    # Step 1: Build the tridiagonal system
    alpha = [0] * (n - 1)
    for i in range(1, n):
        alpha[i - 1] = (3 / h[i] * (yList[i + 1] - yList[i]) - 3 / h[i - 1] * (yList[i] - yList[i - 1]))

    # Tridiagonal matrix coefficients
    l = [1] + [0] * n
    mu = [0] * n
    z = [0] * (n + 1)

    for i in range(1, n):
        l[i] = 2 * (xList[i + 1] - xList[i - 1]) - h[i - 1] * mu[i - 1]
        mu[i] = h[i] / l[i]
        z[i] = (alpha[i - 1] - h[i - 1] * z[i - 1]) / l[i]

    l[n] = 1
    z[n] = 0

    # Step 2: Solve for c, b, and d coefficients
    c = [0] * (n + 1)
    b = [0] * n
    d = [0] * n

    for j in range(n - 1, -1, -1):
        c[j] = z[j] - mu[j] * c[j + 1]
        b[j] = (yList[j + 1] - yList[j]) / h[j] - h[j] * (c[j + 1] + 2 * c[j]) / 3
        d[j] = (c[j + 1] - c[j]) / (3 * h[j])

    # Step 3: Find the interval [x_i, x_{i+1}] containing the point
    for i in range(n):
        if xList[i] <= point < xList[i + 1] or (i == n - 1 and point == xList[-1]):
            # Step 4: Evaluate the cubic spline at the point
            dx = point - xList[i]
            result = yList[i] + b[i] * dx + c[i] * dx ** 2 + d[i] * dx ** 3
            return result

    raise ValueError(f"Point {point} is out of interpolation range [{xList[0]}, {xList[-1]}].")


if __name__ == '__main__':
    xList = [0, pi/6, pi/4, pi/3, pi/2]
    yList = [0, 0.5, 0.7071, 0.8660, 1.0]  # Corresponding y values for sin(x)
    point = pi/3
    print(bcolors.OKBLUE, "----------------- Cubic Spline Interpolation -----------------\n", bcolors.ENDC)
    print(bcolors.OKBLUE, "xList: ", bcolors.ENDC, xList)
    print(bcolors.OKBLUE, "yList: ", bcolors.ENDC, yList)
    print(bcolors.OKBLUE, "Finding an approximation to the point: ", bcolors.ENDC, point)
    cubicSplineInterpolation(xList, yList, point)
    print(bcolors.OKBLUE, "\n---------------------------------------------------------------\n", bcolors.ENDC)