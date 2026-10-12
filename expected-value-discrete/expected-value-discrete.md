## What Is Expected Value?

The expected value (also called expectation or mean) is the **long-run average** of a random variable. It represents the center of the probability distribution and answers the question: "What value do I expect on average?"

For a discrete random variable, it is the weighted average of all possible values, where the weights are the probabilities.

---

## Definition for Discrete Random Variables

For a discrete random variable $X$ that takes values $x_1, x_2, ..., x_n$ with probabilities $P(X = x_i)$:

$$
E[X] = \sum_{i=1}^{n} x_i \cdot P(X = x_i)
$$

**Notation:** $E[X]$, $\mu$, $\mu_X$, or $\langle X \rangle$ all denote expected value.

The expected value may not be a value that $X$ can actually take.

---

## Intuitive Understanding

Imagine repeating the random experiment many times:
1. Each time, you observe a value of $X$
2. You record all the values
3. You compute the average of all recorded values

As the number of repetitions approaches infinity, this average converges to $E[X]$.

This is the **Law of Large Numbers**.

---

## Worked Example: Fair Die

**Setup:** Roll a fair 6-sided die. Let $X$ be the number shown.

**Possible values:** $x \in \{1, 2, 3, 4, 5, 6\}$

**Probabilities:** $P(X = x) = 1/6$ for each value.

**Expected value:**

$$
E[X] = 1 \cdot \frac{1}{6} + 2 \cdot \frac{1}{6} + 3 \cdot \frac{1}{6} + 4 \cdot \frac{1}{6} + 5 \cdot \frac{1}{6} + 6 \cdot \frac{1}{6}
$$

$$
= \frac{1}{6}(1 + 2 + 3 + 4 + 5 + 6) = \frac{21}{6} = 3.5
$$

The expected value is 3.5, even though you can never roll a 3.5.

---

## Worked Example: Loaded Die

**Setup:** A loaded die has the following probabilities:

- $P(X = 1) = 0.1$
- $P(X = 2) = 0.1$
- $P(X = 3) = 0.1$
- $P(X = 4) = 0.1$
- $P(X = 5) = 0.2$
- $P(X = 6) = 0.4$

**Verification:** $0.1 + 0.1 + 0.1 + 0.1 + 0.2 + 0.4 = 1$ ✓

**Expected value:**

$$
E[X] = 1(0.1) + 2(0.1) + 3(0.1) + 4(0.1) + 5(0.2) + 6(0.4)
$$

$$
= 0.1 + 0.2 + 0.3 + 0.4 + 1.0 + 2.4 = 4.4
$$

Higher than 3.5 because the die is biased toward higher numbers.

---

## Worked Example: Bernoulli Random Variable

**Setup:** $X \sim \text{Bernoulli}(p)$ with $P(X = 1) = p$ and $P(X = 0) = 1 - p$.

**Expected value:**

$$
E[X] = 0 \cdot (1-p) + 1 \cdot p = p
$$

The expected value of a Bernoulli random variable equals the probability of success.

**Example:** For a fair coin ($p = 0.5$), $E[X] = 0.5$.

---

## Worked Example: Number of Heads in Two Flips

**Setup:** Flip a fair coin twice. Let $X$ = number of heads.

**Possible outcomes:**
- TT: $X = 0$, probability $= 0.25$
- TH or HT: $X = 1$, probability $= 0.50$
- HH: $X = 2$, probability $= 0.25$

**Expected value:**

$$
E[X] = 0(0.25) + 1(0.50) + 2(0.25)
$$

$$
= 0 + 0.5 + 0.5 = 1
$$

On average, you expect 1 head in 2 flips.

---

## Properties of Expected Value

**1. Linearity:**

$$
E[aX + b] = aE[X] + b
$$

where $a$ and $b$ are constants.

**2. Sum of random variables:**

$$
E[X + Y] = E[X] + E[Y]
$$

This holds even if $X$ and $Y$ are dependent.

**3. Constant:**

$$
E[c] = c
$$

for any constant $c$.

---

## Linearity Examples

**Example 1:** If $E[X] = 5$, find $E[3X + 2]$.

$$
E[3X + 2] = 3E[X] + 2 = 3(5) + 2 = 17
$$

**Example 2:** If $E[X] = 10$ and $E[Y] = 7$, find $E[X + Y]$.

$$
E[X + Y] = E[X] + E[Y] = 10 + 7 = 17
$$

**Example 3:** Find $E[2X - 3Y + 5]$.

$$
E[2X - 3Y + 5] = 2E[X] - 3E[Y] + 5 = 2(10) - 3(7) + 5 = 20 - 21 + 5 = 4
$$

---

## Expected Value of a Product

For **independent** random variables:

$$
E[XY] = E[X] \cdot E[Y]
$$

This does NOT hold in general. For dependent variables:

$$
E[XY] = E[X]E[Y] + \text{Cov}(X, Y)
$$

---

## Expected Value vs Mean of a Sample

**Expected value (population mean, $\mu$):**
- Theoretical value for a probability distribution
- Computed using probabilities
- Fixed (not random)

**Sample mean ($\bar{x}$):**
- Computed from observed data
- $\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i$
- Varies from sample to sample

The sample mean estimates the expected value:

$$
E[\bar{X}] = \mu
$$

---

## Expected Value of Common Distributions

**Bernoulli$(p)$:**

$$
E[X] = p
$$

**Binomial$(n, p)$:**

$$
E[X] = np
$$

**Geometric$(p)$:**

$$
E[X] = \frac{1}{p}
$$

**Poisson$(\lambda)$:**

$$
E[X] = \lambda
$$

**Uniform (discrete) on $\{1, 2, ..., n\}$:**

$$
E[X] = \frac{n + 1}{2}
$$

---

## Expected Value and Decision Making

Expected value is central to decision theory and risk analysis.

**Example:** A game pays \$1 with probability $0.3$ and \$1 otherwise. Entry costs \$1.

Expected winnings: $E[W] = 10(0.3) + 0(0.7) = 3$

Expected profit: $E[P] = 3 - 2 = 1$

On average, you gain \$1 per game. The game is favorable.

---

## Law of the Unconscious Statistician (LOTUS)

To find $E[g(X)]$ where $g$ is a function:

$$
E[g(X)] = \sum_{x} g(x) \cdot P(X = x)
$$

You do NOT need to find the distribution of $g(X)$ first.

**Example:** Find $E[X^2]$ for a fair die.

$$
E[X^2] = \frac{1}{6}(1^2 + 2^2 + 3^2 + 4^2 + 5^2 + 6^2)
$$

$$
= \frac{1}{6}(1 + 4 + 9 + 16 + 25 + 36) = \frac{91}{6} \approx 15.17
$$

Note: $E[X^2] \neq (E[X])^2 = 3.5^2 = 12.25$

---

## Variance from Expected Values

Variance can be computed using expected values:

$$
\text{Var}(X) = E[X^2] - (E[X])^2
$$

**Example:** For the fair die:

$$
\text{Var}(X) = E[X^2] - (E[X])^2 = 15.17 - 12.25 = 2.92
$$

---

## When Expected Value Does Not Exist

Some distributions have undefined expected values:

**Cauchy distribution:**

$$
E[X] = \int_{-\infty}^{\infty} x \cdot \frac{1}{\pi(1 + x^2)} dx
$$

This integral does not converge. The expected value is undefined.

For discrete distributions, $E[X]$ may be undefined if $\sum |x_i| P(x_i) = \infty$.

---

## Conditional Expected Value

The expected value of $X$ given that $Y = y$:

$$
E[X | Y = y] = \sum_{x} x \cdot P(X = x | Y = y)
$$

**Law of total expectation:**

$$
E[X] = E[E[X | Y]] = \sum_{y} E[X | Y = y] \cdot P(Y = y)
$$

---

## Applications in Machine Learning

**Loss functions:**
Expected loss over the data distribution guides model training.

**Risk minimization:**
$E[L(Y, \hat{Y})]$ is minimized when $\hat{Y} = E[Y | X]$ for squared error loss.

**Reinforcement learning:**
Expected cumulative reward (value function) guides action selection.

**Model evaluation:**
Expected accuracy, precision, recall over the data distribution.