## What Logistic Regression Does

Logistic regression is a **binary classification** algorithm. Given input features, it predicts the probability that an example belongs to the positive class (class 1).

Despite its name, logistic regression is used for **classification**, not regression. The "regression" part refers to the fact that we are fitting a model to data, similar to linear regression, but the output is a probability between 0 and 1.

The model answers questions like:

- Is this email spam or not spam?
- Will this customer churn or stay?
- Is this tumor malignant or benign?

---

## The Model Structure

Logistic regression combines two parts:

**Part 1: Linear combination**

$$
z = Xw + b
$$

where:

- $X$ is the input matrix with shape (n_samples, n_features)
- $w$ is the weight vector with shape (n_features,)
- $b$ is the bias, a scalar broadcast across all samples
- $z$ is the linear output with shape (n_samples,), one logit per example

**Part 2: Sigmoid activation**

$$
p = \sigma(z) = \frac{1}{1 + e^{-z}}
$$

The sigmoid function squashes any real number into the range $(0, 1)$, which we interpret as a probability.

The complete model:

$$
p = \sigma(Xw + b) = \frac{1}{1 + e^{-(Xw + b)}}
$$

---

## Understanding the Sigmoid Function

The sigmoid function $\sigma(z) = \frac{1}{1 + e^{-z}}$ has these properties:

- Output is always between 0 and 1
- $\sigma(0) = 0.5$ (the decision boundary)
- $\sigma(z) \to 1$ as $z \to +\infty$
- $\sigma(z) \to 0$ as $z \to -\infty$
- The function is symmetric: $\sigma(-z) = 1 - \sigma(z)$

Some example values:

- $\sigma(-5) \approx 0.0067$
- $\sigma(-2) \approx 0.119$
- $\sigma(0) = 0.5$
- $\sigma(2) \approx 0.881$
- $\sigma(5) \approx 0.9933$

The sigmoid's derivative has a convenient form:

$$
\frac{d\sigma}{dz} = \sigma(z) \cdot (1 - \sigma(z))
$$

This derivative is used during backpropagation.

---

## Binary Cross-Entropy Loss

To train logistic regression, we need a loss function that measures how wrong our predictions are. For binary classification, we use **binary cross-entropy** (also called log loss):

$$
L = -\frac{1}{n} \sum_{i=1}^{n} \left[ y_i \log(p_i) + (1 - y_i) \log(1 - p_i) \right]
$$

where:

- $n$ is the number of training examples
- $y_i$ is the true label (0 or 1)
- $p_i$ is the predicted probability for example $i$

**Why this formula works:**

When $y_i = 1$ (positive class):
- The loss becomes $-\log(p_i)$
- If $p_i$ is close to 1 (correct prediction), $-\log(p_i) \approx 0$ (low loss)
- If $p_i$ is close to 0 (wrong prediction), $-\log(p_i) \to \infty$ (high loss)

When $y_i = 0$ (negative class):
- The loss becomes $-\log(1 - p_i)$
- If $p_i$ is close to 0 (correct prediction), $-\log(1 - p_i) \approx 0$ (low loss)
- If $p_i$ is close to 1 (wrong prediction), $-\log(1 - p_i) \to \infty$ (high loss)

---

## Gradient Descent for Logistic Regression

Training means finding the weights $w$ and bias $b$ that minimize the loss. We use **gradient descent**:

1. Start with initial values for $w$ and $b$ (often zeros)
2. Compute the predictions $p = \sigma(Xw + b)$
3. Compute the loss $L$
4. Compute the gradients $\frac{\partial L}{\partial w}$ and $\frac{\partial L}{\partial b}$
5. Update the parameters in the opposite direction of the gradient
6. Repeat until convergence

**The gradients:**

For logistic regression with binary cross-entropy, the gradients have elegant forms:

$$
\frac{\partial L}{\partial w} = \frac{1}{n} X^T (p - y)
$$

$$
\frac{\partial L}{\partial b} = \frac{1}{n} \sum_{i=1}^{n} (p_i - y_i)
$$

where $(p - y)$ is the vector of prediction errors.

**The update rules:**

$$
w \leftarrow w - \alpha \cdot \frac{\partial L}{\partial w}
$$

$$
b \leftarrow b - \alpha \cdot \frac{\partial L}{\partial b}
$$

where $\alpha$ is the learning rate.

---

## Deriving the Gradients

The gradient derivation combines the chain rule with the sigmoid derivative. For a single example:

$$
\frac{\partial L}{\partial z} = p - y
$$

This remarkably simple result comes from the fact that cross-entropy and sigmoid are mathematically paired. The derivative of the loss with respect to the logit is just the prediction error.

Then by the chain rule:

$$
\frac{\partial L}{\partial w} = \frac{\partial L}{\partial z} \cdot \frac{\partial z}{\partial w} = (p - y) \cdot x
$$

$$
\frac{\partial L}{\partial b} = \frac{\partial L}{\partial z} \cdot \frac{\partial z}{\partial b} = (p - y) \cdot 1
$$

Averaging over all examples gives the batch gradients.

---

## A Training Example

Consider a simple dataset with 2 features and 4 examples:

Features $X$:

- Example 1: [1.0, 2.0]
- Example 2: [2.0, 1.0]
- Example 3: [-1.0, -1.0]
- Example 4: [-2.0, -2.0]

Labels $y$: [1, 1, 0, 0]

**Initialization:**

$w = [0, 0]$, $b = 0$

**First forward pass:**

$z = Xw + b = [0, 0, 0, 0]$

$p = \sigma(z) = [0.5, 0.5, 0.5, 0.5]$

All predictions are 0.5 (maximum uncertainty).

**Compute gradients:**

Error vector: $p - y = [0.5 - 1, 0.5 - 1, 0.5 - 0, 0.5 - 0] = [-0.5, -0.5, 0.5, 0.5]$

$\frac{\partial L}{\partial w} = \frac{1}{4} X^T (p - y)$

$\frac{\partial L}{\partial b} = \frac{1}{4} \sum(p - y) = 0$

**Update parameters:**

With learning rate $\alpha = 0.1$, update $w$ and $b$. The weights will adjust to increase predictions for positive examples and decrease predictions for negative examples.

After many iterations, the model learns weights that separate the two classes.

---

## Convergence and Learning Rate

The learning rate $\alpha$ controls how big each update step is:

- Too large: the algorithm may overshoot and diverge
- Too small: the algorithm converges very slowly
- Just right: smooth convergence to the minimum

Typical values range from 0.001 to 0.1 depending on the problem.

**Signs of good convergence:**

- Loss decreases steadily over iterations
- Loss eventually plateaus at a minimum value
- Parameter values stabilize

**Signs of problems:**

- Loss increases or oscillates wildly (learning rate too high)
- Loss decreases extremely slowly (learning rate too low)
- Loss reaches NaN (numerical overflow, often from extreme predictions)

---

## Making Predictions

After training, use the learned $w$ and $b$ to make predictions:

1. Compute $p = \sigma(Xw + b)$
2. If $p \geq 0.5$, predict class 1
3. If $p < 0.5$, predict class 0

The threshold 0.5 is the default decision boundary. In practice, you might adjust this threshold based on the costs of false positives vs. false negatives.