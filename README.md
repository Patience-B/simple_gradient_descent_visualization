# 📉 Simple Gradient Descent Visualization

A simple interactive app to **visualize how gradient descent works** by adjusting the **learning rate** and **number of iterations**. This tool is ideal for building an **intuition** about how these parameters affect the optimization process.

🌐 **Live Demo**: [Try the App on Streamlit](https://simplegradientdescentvisualization-yybepffs5w2itvgyz5ljti.streamlit.app/)

---

## 💡 What Does the App Do?

This app demonstrates how the **gradient descent algorithm** behaves for a quadratic function:

\[
u(t) = t^2 + 7t - 2
\]

Users can interactively modify:
- **Learning Rate** – controls the step size in each iteration.
- **Number of Iterations** – determines how many steps the algorithm takes.

It then visualizes:
- The function curve.
- The path taken by gradient descent.
- The start and end points.

---

## 🧮 The Gradient Descent Algorithm Used

```python
# Define the function u(t) = t^2 + 7t - 2
def u(t):
    return t**2 + 7 * t - 2

# Derivative (gradient): du/dt = 2t + 7
def grad_u(t):
    return 2 * t + 7

# Gradient descent algorithm
def gradient_descent(learning_rate=0.1, num_iterations=50):
    t = 10  # Starting point
    path = [t]

    for _ in range(num_iterations):
        gradient = grad_u(t)
        step = learning_rate * gradient
        t = t - step
        path.append(t)

    return np.array(path)
```
---

## 🧪 Example: Try It with These Parameters

If you run the algorithm with:

    learning_rate = 0.1

    num_iterations = 3

The textual output will be:
|--------------|-------|
| Initial t    | 10    |
| Gradient     | 27    |
| Updated t    | 7.3   |
| Gradient     | 21.6  |
| Updated t    | 5.14  |
| Gradient     | 17.28 |
| Updated t    | 3.412 |

As shown, the value of t is decreasing toward the minimum, but hasn't yet reached it — because the number of iterations is too small.
Try these same values in the app to see the descent path visually!

---

## 🧠 What Is Gradient Descent?

Gradient Descent is an optimization algorithm used to find the minimum of a function. Here's how it works in simple terms:

    Start at a point on the curve.

    Compute the gradient (slope) at that point.

    Take a step opposite to the gradient — moving downhill.

    Repeat until the slope is near zero (i.e., a minimum point).

---

## 🏔️ Analogy

Imagine you're on a mountain trying to reach the lowest valley. You walk downhill in the steepest direction — this is essentially what gradient descent does.
🧠 In Machine Learning

In machine learning, gradient descent is used to minimize a loss function by tweaking model parameters (like weights in neural networks), ultimately improving the model’s performance.
