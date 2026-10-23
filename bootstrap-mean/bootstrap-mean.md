## What Is Bootstrapping?

Bootstrapping is a powerful **resampling technique** that allows us to estimate the variability of a statistic without making strong assumptions about the underlying distribution.

The core idea: treat your sample as if it were the population, and repeatedly sample from it **with replacement** to understand how your statistic might vary.

Named by Bradley Efron in 1979, the term comes from the phrase "pulling yourself up by your bootstraps," as the method creates information seemingly from nothing.

---

## Why Use Bootstrapping?

**Problem:** You have a sample and want to know how much your estimate (like the mean) might vary if you collected new data.

**Traditional approach:** Use formulas that assume the data follows a specific distribution (often Normal).

**Bootstrap approach:** Simulate the sampling process by resampling from your data.

**Advantages:**
- Works for any statistic (mean, median, correlation, regression coefficients)
- Makes minimal assumptions about the data distribution
- Provides confidence intervals when formulas are unavailable or unreliable
- Works well with small samples

---

## The Bootstrap Procedure

**Step 1:** Start with your original sample of size $n$

**Step 2:** Draw a bootstrap sample of size $n$ **with replacement** from the original sample

**Step 3:** Compute the statistic of interest (e.g., mean) for this bootstrap sample

**Step 4:** Repeat Steps 2-3 a large number of times (typically $B = 1000$ to $10000$)

**Step 5:** Analyze the distribution of the $B$ bootstrap statistics

---

## Sampling With Replacement

**With replacement** means each observation can be selected multiple times in a single bootstrap sample.

**Example:** Original sample = [3, 7, 2, 9, 5]

Possible bootstrap samples:
- [3, 3, 7, 2, 5] (3 appears twice, 9 not included)
- [9, 9, 9, 7, 2] (9 appears three times)
- [5, 2, 7, 3, 9] (same elements, different order)

Each bootstrap sample has the same size as the original but may contain duplicates and miss some original values.

---

## Bootstrap Distribution of the Mean

**Goal:** Estimate the sampling distribution of the sample mean $\bar{X}$.

**Process:**

1. Original sample: $x_1, x_2, ..., x_n$ with mean $\bar{x}$
2. For $b = 1, 2, ..., B$:
   - Draw bootstrap sample $x_1^{*b}, x_2^{*b}, ..., x_n^{*b}$
   - Compute bootstrap mean: $\bar{x}^{*b} = \frac{1}{n}\sum_{i=1}^{n} x_i^{*b}$
3. The set $\{\bar{x}^{*1}, \bar{x}^{*2}, ..., \bar{x}^{*B}\}$ approximates the sampling distribution

---

## Worked Example

**Original sample:** [4, 7, 3, 8, 5] (n = 5)

**Original mean:** $\bar{x} = (4 + 7 + 3 + 8 + 5)/5 = 27/5 = 5.4$

**Bootstrap iteration 1:**
- Bootstrap sample: [7, 3, 3, 8, 4]
- Bootstrap mean: $(7 + 3 + 3 + 8 + 4)/5 = 25/5 = 5.0$

**Bootstrap iteration 2:**
- Bootstrap sample: [5, 8, 8, 7, 3]
- Bootstrap mean: $(5 + 8 + 8 + 7 + 3)/5 = 31/5 = 6.2$

**Bootstrap iteration 3:**
- Bootstrap sample: [4, 4, 5, 3, 7]
- Bootstrap mean: $(4 + 4 + 5 + 3 + 7)/5 = 23/5 = 4.6$

After $B = 1000$ iterations, we have 1000 bootstrap means to analyze.

---

## Bootstrap Standard Error

The **bootstrap standard error** estimates the standard deviation of the sampling distribution:

$$
SE_{boot} = \sqrt{\frac{1}{B-1}\sum_{b=1}^{B}(\bar{x}^{*b} - \bar{\bar{x}}^*)^2}
$$

where $\bar{\bar{x}}^* = \frac{1}{B}\sum_{b=1}^{B}\bar{x}^{*b}$ is the mean of bootstrap means.

This estimates how much $\bar{x}$ would vary across different samples from the population.

---

## Bootstrap Confidence Intervals

Several methods exist for constructing confidence intervals:

**1. Percentile Method:**

For a 95% CI, take the 2.5th and 97.5th percentiles of bootstrap means:

$$
CI_{95\%} = [\bar{x}^*_{(0.025)}, \bar{x}^*_{(0.975)}]
$$

**2. Basic Bootstrap (Reverse Percentile):**

$$
CI_{95\%} = [2\bar{x} - \bar{x}^*_{(0.975)}, 2\bar{x} - \bar{x}^*_{(0.025)}]
$$

**3. Normal Interval:**

$$
CI_{95\%} = [\bar{x} - 1.96 \cdot SE_{boot}, \bar{x} + 1.96 \cdot SE_{boot}]
$$

---

## Percentile Method Example

**Setup:** After 1000 bootstrap iterations, suppose we have bootstrap means ranging from 4.2 to 6.8.

**Sorted bootstrap means:** $\bar{x}^*_{(1)}, \bar{x}^*_{(2)}, ..., \bar{x}^*_{(1000)}$

**2.5th percentile:** $\bar{x}^*_{(25)} = 4.85$ (25th smallest value)

**97.5th percentile:** $\bar{x}^*_{(975)} = 6.12$ (975th smallest value)

**95% CI:** [4.85, 6.12]

We are 95% confident the population mean lies in this interval.

---

## Bias Estimation

Bootstrap can estimate the bias of an estimator:

$$
\text{Bias} = \bar{\bar{x}}^* - \bar{x}
$$

where:
- $\bar{\bar{x}}^*$ is the mean of bootstrap estimates
- $\bar{x}$ is the original sample estimate

**Bias-corrected estimate:**

$$
\hat{\theta}_{corrected} = \bar{x} - \text{Bias} = 2\bar{x} - \bar{\bar{x}}^*
$$

For the sample mean, bias is typically near zero.

---

## BCa Confidence Intervals

The **Bias-Corrected and Accelerated (BCa)** method improves on the percentile method by adjusting for:

1. **Bias:** If bootstrap distribution is not centered on the estimate
2. **Skewness:** If bootstrap distribution is asymmetric

BCa intervals are generally recommended but more complex to compute.

---

## How Many Bootstrap Samples?

**Rule of thumb:**
- For standard errors: $B = 200$ to $500$ is often sufficient
- For confidence intervals: $B = 1000$ to $10000$ is recommended
- For hypothesis testing: $B = 10000$ or more

More bootstrap samples give more stable estimates but require more computation.

**Checking stability:** Run bootstrap twice with different random seeds. If results differ substantially, increase $B$.

---

## Properties of Bootstrap

**Consistency:**

As sample size $n \to \infty$, the bootstrap distribution converges to the true sampling distribution.

**Coverage:**

For smooth statistics, bootstrap confidence intervals achieve approximately correct coverage probability.

**Limitations:**
- May fail for statistics at boundaries (e.g., max, min)
- Requires exchangeable observations
- Can be biased for small samples

---

## When Bootstrap Works Well

**Works well for:**
- Smooth statistics (mean, variance, regression coefficients)
- Reasonably-sized samples ($n \geq 20$)
- Statistics that are functions of the empirical distribution

**May have issues with:**
- Extreme order statistics (min, max)
- Very small samples ($n < 10$)
- Heavy-tailed distributions
- Time series data (requires block bootstrap)

---

## Parametric vs Non-Parametric Bootstrap

**Non-parametric bootstrap (standard):**
- Resample directly from the data
- Makes no distributional assumptions

**Parametric bootstrap:**
1. Fit a parametric model to the data
2. Generate bootstrap samples from the fitted model
3. More efficient if the model is correct

**Example:** If data appears Normal, fit $N(\hat{\mu}, \hat{\sigma}^2)$ and sample from it.

---

## Bootstrap for Other Statistics

The same procedure works for any statistic:

**Median:**
- Compute median for each bootstrap sample
- Analyze the distribution of bootstrap medians

**Correlation:**
- Resample pairs $(x_i, y_i)$ together
- Compute correlation for each bootstrap sample

**Regression coefficients:**
- Resample residuals or cases
- Re-fit regression for each bootstrap sample

---

## Bootstrap vs Traditional Methods

**Traditional (e.g., t-interval for mean):**
- Assumes Normal distribution or large sample
- Uses $\bar{x} \pm t_{n-1, \alpha/2} \cdot s/\sqrt{n}$
- Simple formula

**Bootstrap:**
- No distributional assumption
- Works for complex statistics
- Computationally intensive

For the mean with Normal data, both give similar results. Bootstrap shines for non-standard situations.

---

## Computational Considerations

**Memory:** Store $B$ statistics, not $B$ full samples

**Speed:** For mean, each bootstrap iteration is $O(n)$

**Parallelization:** Bootstrap iterations are independent, easily parallelized

**Random seeds:** Set seed for reproducibility

---

## Applications in Machine Learning

**Model validation:**
- Bootstrap to estimate prediction error variability

**Feature importance:**
- Bootstrap to assess stability of feature rankings

**Ensemble methods:**
- Bagging uses bootstrap samples to train multiple models

**Uncertainty quantification:**
- Bootstrap predictions for confidence intervals