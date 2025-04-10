Simple Gradient Descent Visualization

The project provides a simple app that is used to test the effect of adjusting the the learning rate and the number of iterations on the gradient descent. 
It helps people to have an intuition of how these parameters affect the learning rate.

This is the gradient descent algorith used in the app:
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

For example running the gradient descent with learning rate 0.1 and num_iterations=3 would give these results:
inital t: 10
gradient: 27
updated t: 7.3
gradient: 21.6
updated t: 5.14
gradient: 17.28
updated t: 3.4119999999999995
As one can see the final gradient value obtained is 17.28 and try using the above parameters in the app, has the minimum value been obained. The answer is no because the number of iterations are few.

To view the app, go to thsi link: https://simplegradientdescentvisualization-yybepffs5w2itvgyz5ljti.streamlit.app/

Gradient descent is an optimization algorithm used to find the lowest point on a graph, similar to hiking down a mountain to find the lowest valley. It works by iteratively adjusting parameters (like the slope of a line) to minimize a cost or loss function, which represents the error between the model's predictions and the actual data. 
Here's a simplified explanation:

    Imagine a graph: Think of a function (like a line, curve, or surface) as a landscape with hills and valleys. 

Start at a point: You begin at a random point on this landscape. 
Find the slope: Calculate the slope (or gradient) of the function at your current point. 
Move in the opposite direction: Move in the direction opposite the slope (down the hill) to find a lower point on the landscape. 
Repeat: Repeat steps 3 and 4 until you reach a point where the slope is close to zero (the lowest point). 

Analogy: Imagine you're standing on a mountain and want to find the lowest valley. You would walk down the steepest slope to reach the bottom, similar to how gradient descent finds the minimum of a function. 
In Machine Learning: Gradient descent is used to train machine learning models by adjusting the model's parameters (like weights and biases in a neural network) to minimize the error between the model's predictions and the actual data. 

