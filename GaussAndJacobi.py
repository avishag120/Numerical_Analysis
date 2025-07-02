from math import pi

def is_diagonally_dominant(mat):
    """
    Checks if a matrix is diagonally dominant.
    :param mat: A 2D list representing the matrix.
    :return: True if the matrix is diagonally dominant, False otherwise.
    """
    if mat is None:
        return False

    for i in range(len(mat)):
        diagonal_element = abs(mat[i][i])
        row_sum = sum(abs(mat[i][j]) for j in range(len(mat[i])) if j != i)
        if diagonal_element <= row_sum:
            return False

    return True

def partial_pivoting_with_vector(A, b):
    """
    Performs partial pivoting on matrix A and vector b.
    :param A: 2D list (matrix)
    :param b: 1D list (vector)
    :return: Tuple of (A, b) after pivoting
    """
    n = len(A)
    for i in range(n):
        # Find the pivot row with the largest absolute value in the current column
        pivot_row = i + max(range(len(A[i:])), key=lambda x: abs(A[i + x][i]))

        # Swap rows in A
        if pivot_row != i:
            custom_swap_rows(A, i, pivot_row)
            # Swap corresponding elements in b
            b[i], b[pivot_row] = b[pivot_row], b[i]

    return A, b

def fix(matrix, b):
    """
    Rearranges the rows and columns of a matrix to make it diagonally dominant.
    :param matrix: A square matrix (2D list or numpy array)
    :param b: A vector (1D list or numpy array)
    :return: A tuple containing the diagonally dominant matrix and the modified vector
    """
    n = len(matrix)
    matrix = custom_array(matrix, dtype=float)
    b = custom_array(b, dtype=float)

    for i in range(n):
        # Find the row with the largest absolute value in column i
        max_row = i
        for j in range(i, n):
            if abs(matrix[j][i]) > abs(matrix[max_row][i]):
                max_row = j

        # Swap rows in the matrix and the vector if necessary
        if max_row != i:
            custom_swap_rows(matrix, i, max_row)
            b[i], b[max_row] = b[max_row], b[i]

        # Check if the diagonal element is dominant
        if abs(matrix[i][i]) < sum(abs(matrix[i][j]) for j in range(n) if j != i):
            raise ValueError("Cannot make the matrix diagonally dominant.")

    return matrix, b

def gauss_seidel(A, b, X0, TOL=0.00001, N=200):
    """
    Gauss-Seidel iterative method for solving linear equations Ax = b.
    Args:
        A: 2D list (matrix) representing the coefficients of the linear equations.
        b: 1D list (vector) representing the constants of the linear equations.
        X0: vector of initial guesses for the solution.
        TOL: Tolerance for convergence (default is 0.00001).
        N: Maximum number of iterations (default is 200).

    Returns: A tuple representing the approximate solution to the system of equations.

    """
    n = len(A)
    k = 1

    if is_diagonally_dominant(A):
        print('Matrix is diagonally dominant - preforming gauss seidel algorithm\n')

    print( "Iteration" + "\t\t\t".join([" {:>12}".format(var) for var in ["x{}".format(i) for i in range(1, len(A) + 1)]]))
    print("-----------------------------------------------------------------------------------------------")
    x = [0.0 for _ in range(n)]
    while k <= N:

        for i in range(n):
            sigma = 0
            for j in range(n):
                if A[i][i] == 0:
                    raise ZeroDivisionError(f"Zero on diagonal at row {i}, cannot divide by zero.")
                if j != i:
                    sigma += A[i][j] * x[j]
            x[i] = (b[i] - sigma) / A[i][i]

        print("{:<15} ".format(k) + "\t\t".join(["{:<15} ".format(val) for val in x]))

        max_diff = max(abs(x[i] - X0[i]) for i in range(n))
        if max_diff < TOL:
            return tuple(x)

        k += 1
        X0 = x.copy()

    print("Maximum number of iterations exceeded")
    return (pi, pi, pi)

def jacobi_iterative(A, b, X0, TOL=0.00001, N=200):
    """
    Jacobi iterative method for solving linear equations Ax = b.
    Args:
        A: 2D list (matrix) representing the coefficients of the linear equations.
        b: 1D list (vector) representing the constants of the linear equations.
        X0: vector of initial guesses for the solution.
        TOL: Tolerance for convergence (default is 0.00001).
        N: Maximum number of iterations (default is 200).

    Returns: A tuple representing the approximate solution to the system of equations.

    """
    n = len(A)
    k = 1

    if is_diagonally_dominant(A):
        print('Matrix is diagonally dominant - preforming jacobi algorithm\n')

    print( "Iteration" + "\t\t\t".join([" {:>12}".format(var) for var in ["x{}".format(i) for i in range(1, len(A) + 1)]]))
    print("-----------------------------------------------------------------------------------------------")

    while k <= N:
        x = [0.0 for _ in range(n)]
        for i in range(n):
            sigma = 0
            for j in range(n):
                if A[i][i] == 0:
                    raise ZeroDivisionError(f"Zero on diagonal at row {i}, cannot divide by zero.")
                if j != i:
                    sigma += A[i][j] * X0[j]
            x[i] = (b[i] - sigma) / A[i][i]

        print("{:<15} ".format(k) + "\t\t".join(["{:<15} ".format(val) for val in x]))

        max_diff = max(abs(x[i] - X0[i]) for i in range(n))
        if max_diff < TOL:
            return tuple(x)

        k += 1
        X0 = x.copy()

    print("Maximum number of iterations exceeded")
    return (pi, pi, pi)

def custom_array(data, dtype=float):
    """
    Custom implementation of an array-like function to replace np.array.

    :param data: Input data (list, tuple, etc.)
    :param dtype: Desired data type (default is float)
    :return: A nested list structure mimicking an array
    """
    def convert(value):
        try:
            return dtype(value)
        except ValueError:
            raise TypeError(f"Cannot convert {value} to {dtype}")

    if isinstance(data, (list, tuple)):
        return [custom_array(item, dtype) if isinstance(item, (list, tuple)) else convert(item) for item in data]
    else:
        return convert(data)

def custom_swap_rows(matrix, row1, row2):
    """
    Swaps two rows in a nested list structure.
    :param matrix: Nested list representing the matrix.
    :param row1: Index of the first row.
    :param row2: Index of the second row.
    """
    matrix[row1], matrix[row2] = matrix[row2], matrix[row1]


if __name__ == '__main__':

    matrixA = custom_array( [[4,2,0],[2,10,4],[0,4,5]])
    vectorB = custom_array([2, 6, 5])
    X0 = [0.0] * len(matrixA)

    if not is_diagonally_dominant(matrixA):
        try:
            matrixA, vectorB = fix(matrixA, vectorB)
        except ValueError as e:
            print('the matrix is not diagonally dominant, moving to try')

    solution = ()
    x = int(input('Enter 1 for Gauss Seidel or 2 for Jacobi: '))
    if x == 1:
        try:
            solution = gauss_seidel(matrixA, vectorB, X0)
        except ZeroDivisionError as i:
            print(f"Zero on diagonal at row {i}, cannot divide by zero.")

    elif x == 2:
        matrixA, vectorB = partial_pivoting_with_vector(matrixA, vectorB)
        try:
            solution = jacobi_iterative(matrixA, vectorB, X0)
            if solution == (pi, pi, pi):
                print("The system does not converge")
            elif not (is_diagonally_dominant(matrixA)):
                print("\n Although there is no dominant diagonal the alApproximate solution is:", solution)
        except ZeroDivisionError as i:
            print(f"Zero on diagonal at row {i}, cannot divide by zero.")

    print("\nthe approximate solution:", solution)