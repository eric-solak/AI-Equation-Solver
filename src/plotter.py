# plotter.py
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

def plot_equation(equation_str):
    """
    Converts the equation string into a sympy expression and plots it.
    Assumes the equation is in terms of 'x'.
    """
    try:
        x = sp.symbols('x')
        eq = sp.sympify(equation_str)
        f = sp.lambdify(x, eq, 'numpy')
        x_vals = np.linspace(-10, 10, 400)
        y_vals = f(x_vals)
        
        plt.figure(figsize=(8,6))
        plt.plot(x_vals, y_vals, label=f"${sp.latex(eq)}$")
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Equation Graph')
        plt.legend()
        plt.grid(True)
        plt.show()
    except Exception as e:
        print(f"Error plotting equation: {e}")
