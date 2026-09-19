## The Two Big Ideas in Modern Optimizers

The evolution of optimizers for deep learning is built on two separate ideas, each solving a different problem:

**Idea 1: Momentum (the first moment)**

Instead of using only the current gradient, maintain a running average of past gradients. This is the "first moment" (the mean).

Why momentum helps:
- **Smooths noisy gradients**: mini-batch gradients are noisy estimates. Averaging over multiple steps gives a more reliable direction.
- **Accelerates in consistent directions**: if the gradient keeps pointing the same way, the running average grows larger, creating bigger steps.
- **Dampens oscillations**: in narrow valleys where the gradient alternates sign, the oscillations cancel out in the running average.

The formula:

$$
m_t = \beta_1 \cdot m_{t-1} + (1 - \beta_1) \cdot g_t
$$

With $\beta_1 = 0.9$, the current gradient contributes 10% and the accumulated history contributes 90%.

**Idea 2: Adaptive learning rates (the second moment)**

Track how large the gradients have been for each parameter and scale the update inversely. This is the "second moment" (the uncentered variance).

Why adaptive rates help:
- **Parameters with large gradients** (common features, frequently active neurons) get automatically smaller steps. They do not overshoot.
- **Parameters with small gradients** (rare features, rarely active neurons) get automatically larger steps. They do not get left behind.
- **Eliminates the need to tune one learning rate per parameter**: the adaptation happens automatically.

The formula:

$$
v_t = \beta_2 \cdot v_{t-1} + (1 - \beta_2) \cdot g_t^2
$$

With $\beta_2 = 0.999$, this is a slowly-changing average of squared gradients.

**SGD + momentum** uses only idea 1. **RMSProp** uses only idea 2. **Adam** combines both.

---

## The Bias Correction Problem

Both $m$ and $v$ are initialized to zero vectors. At the start of training, this creates a bias:

With $\beta_1 = 0.9$ and $m_0 = 0$:
- Step 1: $m_1 = 0.9 \times 0 + 0.1 \times g_1 = 0.1 g_1$

The estimate is only **10% of the true gradient**. This is not because the gradient is small; it is because the exponential average has not had time to warm up.

The same problem affects $v$. With $\beta_2 = 0.999$:
- Step 1: $v_1 = 0.001 \times g_1^2$. Only **0.1%** of the true squared gradient.

Without correction, the first few steps would have dramatically wrong magnitudes. The fix is **bias correction**:

$$
\hat{m}_t = \frac{m_t}{1 - \beta_1^t}
$$

$$
\hat{v}_t = \frac{v_t}{1 - \beta_2^t}
$$

How the correction works at step 1:
- $\hat{m}_1 = \frac{0.1 g_1}{1 - 0.9^1} = \frac{0.1 g_1}{0.1} = g_1$ (correct!)
- $\hat{v}_1 = \frac{0.001 g_1^2}{1 - 0.999^1} = \frac{0.001 g_1^2}{0.001} = g_1^2$ (correct!)

How it fades out over time:
- Step 10: $1 - 0.9^{10} = 1 - 0.349 = 0.651$ (moderate correction)
- Step 100: $1 - 0.9^{100} \approx 1.0$ (almost no correction needed)
- Step 1000: $1 - \beta_2^{1000} \approx 1.0$ for both moments

The correction is crucial for the first ~10-20 steps and becomes negligible afterward.

---

## The Full Adam Update

Given parameters $w$, gradient $g_t$, and step count $t$:

**Step 1**: Update first moment (momentum)

$$
m_t = \beta_1 \cdot m_{t-1} + (1 - \beta_1) \cdot g_t
$$

**Step 2**: Update second moment (adaptive rate)

$$
v_t = \beta_2 \cdot v_{t-1} + (1 - \beta_2) \cdot g_t^2
$$

**Step 3**: Bias-correct both moments

$$
\hat{m}_t = \frac{m_t}{1 - \beta_1^t} \qquad \hat{v}_t = \frac{v_t}{1 - \beta_2^t}
$$

**Step 4**: Update parameters

$$
w_t = w_{t-1} - \eta \cdot \frac{\hat{m}_t}{\sqrt{\hat{v}_t} + \epsilon}
$$

The update decomposes into:
- **Direction**: determined by $\hat{m}_t$ (which way to move)
- **Magnitude per parameter**: scaled by $\frac{1}{\sqrt{\hat{v}_t} + \epsilon}$ (how far to move for each parameter)
- **Global scale**: controlled by $\eta$ (the overall learning rate)

---

## A Worked Example

Parameters: $w = [1.0]$, moments: $m = [0]$, $v = [0]$, gradient: $g = [0.5]$, step $t = 1$, $\eta = 0.001$

**Step 1**: $m_1 = 0.9 \times 0 + 0.1 \times 0.5 = 0.05$

**Step 2**: $v_1 = 0.999 \times 0 + 0.001 \times 0.25 = 0.00025$

**Step 3** (bias correction):
- $\hat{m}_1 = \frac{0.05}{1 - 0.9} = \frac{0.05}{0.1} = 0.5$ (corrected from 0.05 to 0.5)
- $\hat{v}_1 = \frac{0.00025}{1 - 0.999} = \frac{0.00025}{0.001} = 0.25$ (corrected from 0.00025 to 0.25)

**Step 4**: $w_1 = 1.0 - 0.001 \times \frac{0.5}{\sqrt{0.25} + 10^{-8}} = 1.0 - 0.001 \times \frac{0.5}{0.5} = 1.0 - 0.001 = 0.999$

Without bias correction, $\hat{m}_1$ would have been 0.05 and $\hat{v}_1$ would have been 0.00025, giving a very different (wrong) update.

---

## The Default Hyperparameters

The Adam paper (Kingma and Ba, 2015) recommended:

- $\eta = 0.001$: the learning rate. This is the main knob to tune.
- $\beta_1 = 0.9$: first moment decay. Averages ~10 recent gradients.
- $\beta_2 = 0.999$: second moment decay. Averages ~1000 recent squared gradients.
- $\epsilon = 10^{-8}$: numerical stability constant. Prevents division by zero when $\hat{v}_t$ is very small.

Why $\beta_2$ is so much larger than $\beta_1$:
- Gradient **directions** can change rapidly (you might be descending one feature now, another next)
- Gradient **magnitudes** change slowly (a parameter that has large gradients tends to keep having large gradients)
- So the second moment should have a **longer memory** than the first

These defaults work well across a wide range of tasks. Most practitioners only tune $\eta$ and leave the rest at defaults.

---

## Why Adam Became the Default Optimizer

Adam became the most popular optimizer in deep learning because:

- **Works out of the box**: the default hyperparameters work well for most tasks. Much less tuning than SGD.
- **Fast convergence**: momentum + adaptive rates navigate the loss landscape efficiently.
- **Handles sparse gradients**: the adaptive rates automatically give rare features larger updates (inherited from AdaGrad/RMSProp).
- **Robust to hyperparameter choice**: even if $\eta$ is not perfectly tuned, Adam performs reasonably.

Known limitations:

- **Generalization gap**: on some tasks (especially image classification with CNNs), well-tuned SGD + momentum can produce models that generalize better to test data.
- **Weight decay interaction**: when you add L2 regularization to Adam, the adaptive rates interfere with the regularization. This is why **AdamW** (decoupled weight decay) was invented.
- **Memory cost**: Adam stores $m$ and $v$ (same size as parameters), tripling memory usage compared to SGD.
- **Bias toward sharp minima**: some research suggests Adam tends to converge to sharper minima than SGD, which may explain the generalization gap.