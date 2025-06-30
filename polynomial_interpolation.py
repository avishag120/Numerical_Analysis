from colors import bcolors
from matrix_utility import *
from GaussAndJacobi import gauss_seidel
import matplotlib.pyplot as plt

def polynomialInterpolation(table_points, x):
    matrix = [[point[0] ** i for i in range(len(table_points))] for point in table_points]  # Create the Vandermonde matrix
    b = [point[1] for point in table_points]  # Extract the vector b

    print(bcolors.OKBLUE, "The matrix obtained from the points: ", bcolors.ENDC, '\n', np.array(matrix))
    print(bcolors.OKBLUE, "\nb vector: ", bcolors.ENDC, '\n', np.array(b))

    # Solve the system using Gauss-Seidel
    matrixSol = gauss_seidel(matrix, b, X0=[0.0] * len(b))

    print(f"matrixSol: {matrixSol}, type: {type(matrixSol)}")
    result = sum([matrixSol[i] * (x ** i) for i in range(len(matrixSol))])  # Compute the polynomial value

    print(bcolors.OKBLUE, "\nThe polynom:", bcolors.ENDC)
    print('P(X) = ' + ' + '.join([f'({matrixSol[i]}) * x^{i}' for i in range(len(matrixSol))]))
    print(bcolors.OKGREEN, f"\nThe Result of P(X={x}) is:", bcolors.ENDC)
    print(result)

    # Plotting the graph
    x_vals = np.linspace(min([p[0] for p in table_points]) - 1, max([p[0] for p in table_points]) + 1, 500)
    y_vals = [sum([matrixSol[i] * (xi ** i) for i in range(len(matrixSol))]) for xi in x_vals]

    plt.scatter([p[0] for p in table_points], [p[1] for p in table_points], color='red', label='Data Points')
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
    print(bcolors.OKBLUE, "----------------- Interpolation & Extrapolation Methods -----------------\n", bcolors.ENDC)
    print(bcolors.OKBLUE, "Table Points: ", bcolors.ENDC, table_points)
    print(bcolors.OKBLUE, "Finding an approximation to the point: ", bcolors.ENDC, x,'\n')
    polynomialInterpolation(table_points, x)
    print(bcolors.OKBLUE, "\n-------------------------------------")