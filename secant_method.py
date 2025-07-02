import math


def secant_method(func, x0, x1, tol=1e-6, max_iter=100):
    """
    Secant Method with improvements:
    - Handles zero or near-zero denominators
    - Handles invalid function evaluations
    - Adds additional convergence criteria
    """
    # Print the header for the iteration table
    print(f"{'Iter':<6}{'x0':<15}{'x1':<15}{'f(x1)':<15}{'Δx':<15}")

    for i in range(max_iter):
        try:
            # Evaluate the function at the current guesses x0 and x1
            f_x0 = func(x0)
            f_x1 = func(x1)
        except Exception as e:
            # Handle any errors during function evaluation
            print(f"Error evaluating function at iteration {i}: {e}")
            return None
        # Check if the function value at x1 is within the tolerance (root found)
        if abs(f_x1) < tol:
            print(f"Root found at x = {x1} after {i} iterations.")
            return x1
        # Calculate the denominator for the Secant Method formula
        denominator = f_x1 - f_x0
        if abs(denominator) < 1e-12:
            # Handle cases where the denominator is too small (near-zero division)
            print("Denominator too small; possible division by near-zero.")
            return None
        # Apply the Secant Method formula to compute the next approximation
        x2 = x1 - f_x1 * (x1 - x0) / denominator
        # Calculate the change in x (Δx) for convergence check
        delta_x = abs(x2 - x1)
        print(f"{i:<6}{x0:<15.10f}{x1:<15.10f}{f_x1:<15.10f}{delta_x:<15.10f}")
        # Check if the change in x is within the tolerance (convergence achieved)
        if delta_x < tol:
            print(f"Root converged to x = {x2} after {i + 1} iterations (Δx < tol).")
            return x2
        # Update x0 and x1 for the next iteration
        x0, x1 = x1, x2

    print("Maximum iterations reached without finding the root.")
    return None


if __name__ == "__main__":
    def f(x):
        return x ** 3 - math.cos(x)


    x0 = 1.0
    x1 = 0.0

    root = secant_method(f, x0, x1)
    print(f"Approximate root: {root}")


