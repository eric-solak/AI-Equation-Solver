# main.py
import time
from imageParse import extractEquation
from equationParse import solve_equation
from plotter import plot_equation

def main(image_path):
    # Step 1: Extract equation text from the image using # ! 
    equation_text = extractEquation(image_path)
    print("Extracted Text:", equation_text)
    
    solutions = solve_equation(equation_text)
    print("Solutions:", solutions)
    
    # Step 4: Plot the equation using matplotlib
    plot_equation(solutions)

if __name__ == "__main__":
    # Path to your sample image (ensure this file exists)
    image_path = "images/example1.png"
    main(image_path)
