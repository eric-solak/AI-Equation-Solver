import matplotlib.pyplot as plt

def create_equation_image(equation, filename):
    # Create a new figure
    fig, ax = plt.subplots()

    # Hide axes
    ax.axis('off')

    # Render the equation as LaTeX
    ax.text(0.5, 0.5, f'${equation}$', fontsize=40, ha='center')

    # Save the image
    plt.savefig(filename, dpi=300, bbox_inches='tight')

# Example usage
equation = 'y = 2x + 2x + 1'  # Replace with any equation
create_equation_image(equation, 'equation_image.png')