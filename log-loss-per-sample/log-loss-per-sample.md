## Binary Classification Setup

In binary classification:
- Input: a sample $x$
- True label: $y \in \{0, 1\}$
- Predicted probability: $\hat{y} = P(y=1|x)$

The model outputs a single probability for the positive class. The probability of the negative class is $1 - \hat{y}$.

---

## Log Loss for a Single Sample

The log loss (also called binary cross-entropy) for one sample is:

$$
L = -[y \log(\hat{y}) + (1-y) \log(1-\hat{y})]
$$

This formula has two cases:

**When y = 1 (positive class):**

$$
L = -\log(\hat{y})
$$
The loss is the negative log of the predicted probability for the positive class.

**When y = 0 (negative class):**

$$
L = -\log(1-\hat{y})
$$
The loss is the negative log of the predicted probability for the negative class.

---

## Understanding the Formula

The loss measures how surprised you should be given your prediction:

**Correct and confident:**
- True: y = 1, predicted: p = 0.95
- Loss: -log(0.95) = 0.05
- Low loss because prediction matches reality

**Correct but uncertain:**
- True: y = 1, predicted: p = 0.6
- Loss: -log(0.6) = 0.51
- Higher loss due to uncertainty

**Wrong and uncertain:**
- True: y = 1, predicted: p = 0.4
- Loss: -log(0.4) = 0.92
- High loss for wrong prediction

**Wrong and confident:**
- True: y = 1, predicted: p = 0.05
- Loss: -log(0.05) = 3.0
- Very high loss for confident mistake

---

## The Loss Curve

For a positive sample (y = 1), loss as function of predicted probability:

**p = 0.99:** loss = 0.01
**p = 0.90:** loss = 0.105
**p = 0.70:** loss = 0.357
**p = 0.50:** loss = 0.693
**p = 0.30:** loss = 1.204
**p = 0.10:** loss = 2.303
**p = 0.01:** loss = 4.605

Key observations:
- Loss is near 0 for confident correct predictions
- Loss is 0.693 (log 2) for uncertain predictions (p = 0.5)
- Loss grows rapidly for confident wrong predictions
- Loss approaches infinity as p approaches 0

---

## Why Logarithm?

The logarithm is not arbitrary. It comes from information theory:

**Information content:** The information gained from observing an event with probability $p$ is $-\log(p)$.

**Surprise:** If you predict $p = 0.9$ and the event happens, you are not surprised (low information gain). If you predict $p = 0.1$ and it happens, you are very surprised (high information gain).

**Proper scoring rule:** Log loss is a proper scoring rule, meaning the optimal prediction is always the true probability. You cannot game the metric by predicting something other than your true belief.

---

## Aggregating Over Multiple Samples

For a dataset with $n$ samples:

$$
L_{\text{total}} = -\frac{1}{n}\sum_{i=1}^{n}[y_i \log(\hat{y}_i) + (1-y_i) \log(1-\hat{y}_i)]
$$

This is the mean log loss, which:
- Averages the per-sample losses
- Gives equal weight to each sample
- Is comparable across datasets of different sizes

---

## Connection to Cross-Entropy

Log loss and binary cross-entropy are the same thing:

$$
L = -[y \log(\hat{y}) + (1-y) \log(1-\hat{y})] = H(y, \hat{y})
$$

Where $H(y, \hat{y})$ is the cross-entropy between the true distribution $y$ (a delta at 0 or 1) and the predicted distribution $\hat{y}$.

Multi-class cross-entropy is the generalization to more than 2 classes.

---

## The Gradient

The gradient of log loss with respect to the predicted probability:

$$
\frac{\partial L}{\partial \hat{y}} = -\frac{y}{\hat{y}} + \frac{1-y}{1-\hat{y}}
$$

For y = 1: gradient = $-1/\hat{y}$ (negative, push prediction up)
For y = 0: gradient = $1/(1-\hat{y})$ (positive, push prediction down)

The gradient magnitude:
- Small when prediction is correct and confident
- Large when prediction is wrong, especially when confident

---

## Numerical Stability

Computing log(p) is dangerous when p is near 0:
- log(0) = negative infinity
- log(1e-100) = -230.26 (very large)

Solutions:

**Clipping:** Clip predictions to [epsilon, 1-epsilon] where epsilon = 1e-7
- p_clipped = clip(p, 1e-7, 1-1e-7)
- Loss = -log(p_clipped)

**Log-sum-exp trick:** Compute log(sigmoid(z)) directly from logit z
- More numerically stable than sigmoid(z) then log

**Framework functions:** Use built-in functions like torch.nn.BCEWithLogitsLoss that handle stability internally.

---

## Log Loss vs. Other Metrics

**Accuracy:**
- Only cares about correct/incorrect
- No credit for confidence
- Threshold-dependent (usually 0.5)

**Log loss:**
- Cares about predicted probability
- Rewards confident correct predictions
- Punishes confident wrong predictions
- Threshold-independent

Example with two models predicting y=1:
- Model A: p = 0.51 (correct by threshold, loss = 0.67)
- Model B: p = 0.99 (correct by threshold, loss = 0.01)

Accuracy sees both as correct. Log loss sees Model B as much better.

---

## Where Log Loss Is Used

- **Logistic regression**: the standard loss function
- **Binary neural network classifiers**: final sigmoid layer with BCE loss
- **Probabilistic predictions**: any model outputting probabilities
- **Kaggle competitions**: common evaluation metric
- **Click-through rate prediction**: predicting probability of clicks
- **Medical diagnosis**: when calibrated probabilities matter