def norm(mat):
    """Computes the max row sum (infinity norm) of a matrix"""
    size = len(mat)
    max_row = 0
    for row in range(size):
        sum_row = sum(abs(mat[row][col]) for col in range(size))
        if sum_row > max_row:
            max_row = sum_row
    return max_row


def print_matrix(mat):
    """Prints a matrix in clean format"""
    for row in mat:
        print("  ".join(f"{val:8.4f}" for val in row))
    print()


def identity_matrix(size):
    """Returns an identity matrix of given size"""
    return [[1 if i == j else 0 for j in range(size)] for i in range(size)]



def solve_gaussian(A, b):
    """Solves Ax = b using Gaussian elimination with pivoting"""
    n = len(A)
    if n == 0 or len(b) == 0:
        raise ValueError("Matrix or vector is empty.")
    if any(len(row) != n for row in A):
        raise ValueError("Matrix is not square.")

    A = [row[:] for row in A]
    b = b[:]

    for i in range(n):
        # Pivoting: Find the maximum element in the column and swap rows
        max_row = max(range(i, n), key=lambda r: abs(A[r][i]))
        if A[max_row][i] == 0:
            raise ValueError("Matrix is singular – zero on diagonal.")
        if max_row != i:
            A[i], A[max_row] = A[max_row], A[i]
            b[i], b[max_row] = b[max_row], b[i]

        # Normalize pivot row
        for j in range(i + 1, n):
            factor = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]
            b[j] -= factor * b[i]

    x = [0] * n
    for i in range(n - 1, -1, -1):
        s = sum(A[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (b[i] - s) / A[i][i]

    return x


def inverse(A):
    """Computes the inverse of matrix A using Gauss-Jordan elimination with pivoting"""
    n = len(A)
    if n == 0 or any(len(row) != n for row in A):
        raise ValueError("Matrix is empty or not square.")

    A = [row[:] for row in A]
    I = identity_matrix(n)

    for i in range(n):
        # Pivoting: Find the maximum element in the column and swap rows
        max_row = max(range(i, n), key=lambda r: abs(A[r][i]))
        if A[max_row][i] == 0:
            raise ValueError("Matrix is singular – zero on diagonal.")
        if max_row != i:
            A[i], A[max_row] = A[max_row], A[i]
            I[i], I[max_row] = I[max_row], I[i]

        # Normalize pivot row
        factor = A[i][i]
        for j in range(n):
            A[i][j] /= factor
            I[i][j] /= factor

        # Eliminate other rows
        for k in range(n):
            if k != i:
                factor = A[k][i]
                for j in range(n):
                    A[k][j] -= factor * A[i][j]
                    I[k][j] -= factor * I[i][j]

    return I

def condition_number(A):
    norm_A = norm(A)
    A_inv = inverse(A)
    norm_A_inv = norm(A_inv)
    cond = norm_A * norm_A_inv

    print("\nMatrix A:")
    print_matrix(A)

    print("Inverse of A:")
    print_matrix(A_inv)

    print("‖A‖∞ =", norm_A)
    print("‖A⁻¹‖∞ =", norm_A_inv)
    print("Condition number =", cond)

    if cond < 10:
        print(" The system is well-posed.")
    elif cond < 1000:
        print("⚠ The system is moderately sensitive.")
    else:
        print(" The system is ill-posed.")

    return cond


if __name__ == '__main__':
    A = [
        [0.913, 0.659],
        [0.457, 0.330],

    ]
    b = [0.255, 0.126]  # Example vector for solving Ax = b

    print("=== Solving Ax = b ===")
    x = solve_gaussian(A, b)
    print("Solution x:")
    for val in x:
        print(f"{val:.6f}")

    print("\n=== Checking Condition Number ===")
    condition_number(A)