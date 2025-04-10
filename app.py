import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Define the function u(t) = t^2 + 7t - 2
def u(t):
    return t**2 + 7 * t - 2

# Define the gradient (derivative) of the function du/dt = 2t + 7
def grad_u(t):
    return 2 * t + 7

# Gradient descent algorithm
def gradient_descent(learning_rate=0.1, num_iterations=50):
    # Start at t = 10
    t = 10
    path = [t]  # To store the path of t during gradient descent
    
    for _ in range(num_iterations):
        gradient = grad_u(t)  # Compute gradient at t
        step = learning_rate * gradient  # Calculate the step
        t = t - step  # Update t
        path.append(t)  # Store the new position of t
    
    return np.array(path)

# Streamlit app
st.title("Gradient Descent Visualization")
st.markdown("""
    Check out the [README file](https://github.com/Patience-B/simple_gradient_descent_visualization/blob/main/README.md) 
    to learn more about how the app works.

    ### How to use:
    1. **Learning Rate**: This controls how much to move in each step. A high learning rate might make you overshoot the minimum, 
    while a small one makes the descent slow.
    2. **Number of Iterations**: The number of steps the gradient descent will take before stopping.
    
    Example Inputs:
    - Learning Rate: 0.5
    - Number of Iterations: 10
""")

# User inputs for learning rate and number of iterations
learning_rate = st.slider("Choose the Learning Rate", min_value=0.01, max_value=1.0, value=0.5, step=0.01)
num_iterations = st.slider("Choose the Number of Iterations", min_value=1, max_value=100, value=50, step=1)

# Run gradient descent with user inputs
path = gradient_descent(learning_rate=learning_rate, num_iterations=num_iterations)

# Generate values for t for plotting the function
t_values = np.linspace(-20, 10, 100)
u_values = u(t_values)

# Plot the function u(t)
fig, ax = plt.subplots()
ax.plot(t_values, u_values, 'g', label="u(t) = t^2 + 7t - 2")

# Plot the path taken by gradient descent
ax.plot(path, u(path), marker='o', color='r', label='Gradient Descent Path')

# Highlight the starting and ending points
ax.scatter(path[0], u(path[0]), color='blue', s=100, label='Start')
ax.scatter(path[-1], u(path[-1]), color='green', s=100, label='End')

# Labels and title
ax.set_title("Gradient Descent on u(t) = t^2 + 7t - 2")
ax.set_xlabel('t')
ax.set_ylabel('u(t)')
ax.legend()
ax.grid(True)

# Show plot in Streamlit
st.pyplot(fig)
