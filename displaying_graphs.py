import matplotlib.pyplot as plt

def plot_points(x_vals, y_vals, title):
    """Plots the given x and y values on a graph."""
    plt.plot(x_vals, y_vals, linestyle='-', marker='o', color= 'green' , label='Data Points')
    plt.title(title)
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.legend()
    plt.show()