## What Is Variance?

Variance measures the **spread** or **dispersion** of data points around the mean. It quantifies how far values typically deviate from the average.

**High variance:** Data points are spread far from the mean.

**Low variance:** Data points are clustered close to the mean.

**Zero variance:** All data points are identical.

---

## Population vs Sample

**Population variance ($\sigma^2$):**

Used when you have data for the entire population.

$$
\sigma^2 = \frac{1}{N}\sum_{i=1}^{N}(x_i - \mu)^2
$$

**Sample variance ($s^2$):**

Used when you have a sample from a larger population.

$$
s^2 = \frac{1}{n-1}\sum_{i=1}^{n}(x_i - \bar{x})^2
$$

The key difference is dividing by $n-1$ instead of $n$ for samples.

---

## Why Divide by $n-1$? (Bessel's Correction)

The sample variance uses $n-1$ instead of $n$ because:

**1. Unbiasedness:**

Dividing by $n$ underestimates the population variance. Using $n-1$ makes $s^2$ an **unbiased estimator** of $\sigma^2$:

$$
E[s^2] = \sigma^2
$$

**2. Degrees of freedom:**

After computing the sample mean $\bar{x}$, only $n-1$ deviations are "free" to vary. The last one is determined by the constraint that deviations sum to zero:

$$
\sum_{i=1}^{n}(x_i - \bar{x}) = 0
$$

---

## Step-by-Step Sample Variance Calculation

**Step 1:** Calculate the sample mean $\bar{x}$

**Step 2:** Subtract the mean from each data point to get deviations

**Step 3:** Square each deviation

**Step 4:** Sum the squared deviations

**Step 5:** Divide by $n-1$

---

## Worked Example

**Data:** [4, 8, 6, 5, 3, 9, 7] (n = 7)

**Step 1: Calculate mean**

$$
\bar{x} = \frac{4 + 8 + 6 + 5 + 3 + 9 + 7}{7} = \frac{42}{7} = 6
$$

**Step 2: Calculate deviations**

- $4 - 6 = -2$
- $8 - 6 = 2$
- $6 - 6 = 0$
- $5 - 6 = -1$
- $3 - 6 = -3$
- $9 - 6 = 3$
- $7 - 6 = 1$

**Step 3: Square deviations**

$(-2)^2 = 4$, $2^2 = 4$, $0^2 = 0$, $(-1)^2 = 1$, $(-3)^2 = 9$, $3^2 = 9$, $1^2 = 1$

**Step 4: Sum squared deviations**

$$
\sum(x_i - \bar{x})^2 = 4 + 4 + 0 + 1 + 9 + 9 + 1 = 28
$$

**Step 5: Divide by $n-1$**

$$
s^2 = \frac{28}{7-1} = \frac{28}{6} \approx 4.67
$$

---

## Standard Deviation

The standard deviation is the square root of variance:

**Population standard deviation:**

$$
\sigma = \sqrt{\sigma^2} = \sqrt{\frac{1}{N}\sum_{i=1}^{N}(x_i - \mu)^2}
$$

**Sample standard deviation:**

$$
s = \sqrt{s^2} = \sqrt{\frac{1}{n-1}\sum_{i=1}^{n}(x_i - \bar{x})^2}
$$

---

## Continuing the Example

From the previous example, $s^2 \approx 4.67$

$$
s = \sqrt{4.67} \approx 2.16
$$

**Interpretation:** On average, data points deviate about 2.16 units from the mean of 6.

---

## Why Standard Deviation?

**Same units as data:**

Variance is in squared units (e.g., meters$^2$). Standard deviation is in original units (meters).

**Interpretable:**

For roughly Normal data:
- About 68% of data falls within $\bar{x} \pm s$
- About 95% falls within $\bar{x} \pm 2s$
- About 99.7% falls within $\bar{x} \pm 3s$

---

## Alternative Variance Formula

A computationally convenient formula:

$$
s^2 = \frac{1}{n-1}\left[\sum_{i=1}^{n}x_i^2 - \frac{(\sum_{i=1}^{n}x_i)^2}{n}\right]
$$

Or equivalently:

$$
s^2 = \frac{n}{n-1}\left[\frac{\sum x_i^2}{n} - \bar{x}^2\right]
$$

This avoids computing deviations explicitly.

---

## Using the Alternative Formula

**Data:** [4, 8, 6, 5, 3, 9, 7]

$\sum x_i = 42$

$\sum x_i^2 = 16 + 64 + 36 + 25 + 9 + 81 + 49 = 280$

$$
s^2 = \frac{1}{6}\left[280 - \frac{42^2}{7}\right] = \frac{1}{6}\left[280 - \frac{1764}{7}\right] = \frac{1}{6}[280 - 252] = \frac{28}{6} \approx 4.67
$$

Same result as before.

---

## Properties of Variance

**1. Always non-negative:**

$$
s^2 \geq 0
$$

**2. Zero only when all values are equal**

**3. Adding a constant does not change variance:**

$$
\text{Var}(X + c) = \text{Var}(X)
$$

**4. Scaling by a constant:**

$$
\text{Var}(cX) = c^2 \cdot \text{Var}(X)
$$

**5. Linear transformation:**

$$
\text{Var}(aX + b) = a^2 \cdot \text{Var}(X)
$$

---

## Variance of Sum of Independent Variables

For independent random variables $X$ and $Y$:

$$
\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y)
$$

$$
\text{Var}(X - Y) = \text{Var}(X) + \text{Var}(Y)
$$

Note: Variances add even for subtraction!

---

## Coefficient of Variation

The coefficient of variation (CV) is a dimensionless measure of relative variability:

$$
CV = \frac{s}{\bar{x}} \times 100\%
$$

**Use cases:**
- Comparing variability across different scales
- Comparing variability when means differ

**Example:** Two datasets with $s = 10$:
- Dataset A: $\bar{x} = 100$, CV = 10%
- Dataset B: $\bar{x} = 20$, CV = 50%

Dataset B has more relative variability.

---

## Standard Error of the Mean

The standard error (SE) measures uncertainty in the sample mean:

$$
SE = \frac{s}{\sqrt{n}}
$$

As sample size increases, SE decreases (more precision).

**Example:** $s = 2.16$, $n = 7$

$$
SE = \frac{2.16}{\sqrt{7}} = \frac{2.16}{2.65} \approx 0.82
$$

---

## Pooled Variance

When combining samples from groups assumed to have equal variance:

$$
s_p^2 = \frac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2}
$$

This is a weighted average of the group variances, used in two-sample t-tests.

---

## Robust Alternatives

Standard deviation is sensitive to outliers. Robust alternatives include:

**Median Absolute Deviation (MAD):**

$$
MAD = \text{median}(|x_i - \text{median}(x)|)
$$

**Interquartile Range (IQR):**

$$
IQR = Q3 - Q1
$$

For Normal data: $\sigma \approx 1.4826 \times MAD \approx 0.7413 \times IQR$

---

## Sample Variance is Unbiased, Sample SD is Not

**Sample variance:** $E[s^2] = \sigma^2$ (unbiased)

**Sample standard deviation:** $E[s] \neq \sigma$ (slightly biased low)

The bias in $s$ is small and decreases with sample size. For most purposes, $s$ is used without correction.

---

## Numerical Stability

The formula $s^2 = \frac{\sum x_i^2 - n\bar{x}^2}{n-1}$ can have numerical issues when $\sum x_i^2$ and $n\bar{x}^2$ are both large.

**Welford's online algorithm** computes variance in a single pass with numerical stability:

$$
M_k = M_{k-1} + \frac{x_k - M_{k-1}}{k}
$$

$$
S_k = S_{k-1} + (x_k - M_{k-1})(x_k - M_k)
$$

$$
s^2 = \frac{S_n}{n-1}
$$

---

## Variance in Machine Learning

**Feature scaling:**
- Standardization: $z = (x - \bar{x})/s$
- Important for distance-based algorithms

**Model evaluation:**
- Variance of predictions indicates model stability

**Bias-variance tradeoff:**
- High variance models overfit
- Low variance may underfit

**Principal Component Analysis:**
- Finds directions of maximum variance
- Components ordered by variance explained

---

## Common Mistakes

**1. Using $n$ instead of $n-1$ for samples**

Results in biased (underestimated) variance.

**2. Forgetting to square the standard deviation**

Variance is $s^2$, not $s$.

**3. Confusing SD with SE**

SD measures data spread; SE measures uncertainty in the mean.

**4. Adding standard deviations directly**

Variances add, not standard deviations.

$$
\sigma_{X+Y} = \sqrt{\sigma_X^2 + \sigma_Y^2} \neq \sigma_X + \sigma_Y
$$