## What RMSProp Fixes

AdaGrad was a breakthrough: it gave each parameter its own learning rate by dividing by the accumulated squared gradients. But AdaGrad's accumulator only grows, so the effective learning rate eventually shrinks to near zero and the model stops learning.

RMSProp (Root Mean Square Propagation) fixes this with one simple change: **use a decaying average instead of a sum.**

Geoffrey Hinton proposed RMSProp in a Coursera lecture in 2012. It was never published in a formal paper, yet it became one of the most widely used optimizers.

---

## The Key Change: Exponential Decay

AdaGrad's accumulator sums all past squared gradients:

$$
G_t = G_{t-1} + g_t^2 \quad \text{(only grows)}
$$

RMSProp replaces this with an **exponentially decaying average**:

$$
s_t = \beta \cdot s_{t-1} + (1 - \beta) \cdot g_t^2
$$

- $\beta$ is the decay rate (typically 0.9 or 0.99)
- $s_t$ is a **weighted average** of recent squared gradients
- Old gradients fade away exponentially
- The accumulator does **not** grow without bound

Then the parameter update uses the same formula as AdaGrad:

$$
w_t = w_{t-1} - \frac{\eta}{\sqrt{s_t + \epsilon}} \cdot g_t
$$

The only difference is $s_t$ (decaying average) instead of $G_t$ (ever-growing sum).

---

## Understanding the Exponential Average

The exponential average is a "leaky" accumulator. To see why, expand a few steps with $\beta = 0.9$:

- $s_1 = 0.9 \times 0 + 0.1 \times g_1^2 = 0.1 g_1^2$
- $s_2 = 0.9 \times 0.1 g_1^2 + 0.1 g_2^2 = 0.09 g_1^2 + 0.1 g_2^2$
- $s_3 = 0.081 g_1^2 + 0.09 g_2^2 + 0.1 g_3^2$

Each past gradient gets multiplied by $\beta$ one more time at each step:

- The gradient from 1 step ago has weight $\beta(1-\beta) = 0.09$
- The gradient from 5 steps ago has weight $\beta^5(1-\beta) \approx 0.059$
- The gradient from 10 steps ago has weight $\beta^{10}(1-\beta) \approx 0.035$
- The gradient from 50 steps ago has weight $\beta^{50}(1-\beta) \approx 0.0005$ (essentially forgotten)

The **effective window** is approximately $\frac{1}{1-\beta}$ steps:

- $\beta = 0.9$: window of ~10 steps
- $\beta = 0.99$: window of ~100 steps
- $\beta = 0.999$: window of ~1000 steps

---

## Why This Fixes AdaGrad's Problem

The crucial difference: **the effective learning rate can increase again.**

With AdaGrad:
- If parameter $w_i$ had large gradients in steps 1-100, its $G_i$ is large
- Even if gradients become small in steps 101-200, $G_i$ stays large (it only grows)
- The learning rate stays small forever

With RMSProp:
- If parameter $w_i$ had large gradients in steps 1-100, its $s_i$ is large
- If gradients become small in steps 101-200, the old large values fade away
- $s_i$ decreases, and the effective learning rate **increases** again
- The optimizer adapts to the **current** gradient regime, not the entire history

This means the model can keep making meaningful progress throughout training, even if the character of the gradients changes over time.

---

## A Detailed Example

Parameters: $w = [1.0, 2.0]$, accumulators: $s = [0.0, 0.0]$, $\eta = 0.01$, $\beta = 0.9$

**Step 1 with gradient $g = [0.5, 2.0]$**:

Update accumulators:
- $s_1 = 0.9 \times 0 + 0.1 \times (0.5)^2 = 0.025$
- $s_2 = 0.9 \times 0 + 0.1 \times (2.0)^2 = 0.4$

Effective learning rates:
- Parameter 1: $\frac{0.01}{\sqrt{0.025 + 10^{-8}}} = \frac{0.01}{0.158} \approx 0.0632$
- Parameter 2: $\frac{0.01}{\sqrt{0.4 + 10^{-8}}} = \frac{0.01}{0.632} \approx 0.0158$

Update parameters:
- $w_1 = 1.0 - 0.0632 \times 0.5 = 1.0 - 0.0316 = 0.968$
- $w_2 = 2.0 - 0.0158 \times 2.0 = 2.0 - 0.0316 = 1.968$

Both parameters moved by approximately $0.032$, even though parameter 2's gradient was 4x larger. RMSProp equalized the step sizes.

**Step 2 with gradient $g = [0.5, 0.1]$** (parameter 2's gradient dropped):

Update accumulators:
- $s_1 = 0.9 \times 0.025 + 0.1 \times 0.25 = 0.0225 + 0.025 = 0.0475$
- $s_2 = 0.9 \times 0.4 + 0.1 \times 0.01 = 0.36 + 0.001 = 0.361$

Effective learning rates:
- Parameter 1: $\frac{0.01}{\sqrt{0.0475}} \approx 0.0459$
- Parameter 2: $\frac{0.01}{\sqrt{0.361}} \approx 0.0166$ (still small because of the large gradient at step 1)

After many more steps with small gradients for parameter 2, $s_2$ would shrink toward $0.1 \times 0.01 = 0.001$, and its effective learning rate would recover. With AdaGrad, it would have stayed at $0.4 + 0.01 = 0.41$ forever.

---

## Choosing Beta

The decay rate $\beta$ controls the memory length:

- **$\beta = 0.9$** (the most common default): remembers roughly the last 10 steps. Quick adaptation to changing gradient conditions. Good for most tasks.
- **$\beta = 0.99$**: remembers the last ~100 steps. Slower adaptation, smoother estimates. Good when gradients are very noisy.
- **$\beta = 0.0$**: no memory at all. $s_t = g_t^2$ (uses only the current squared gradient). This is very noisy and not recommended.
- **$\beta = 1.0$**: infinite memory. $s_t = s_{t-1}$ (never updates). The accumulator is stuck at its initial value. Useless.

---

## RMSProp in the Optimizer Family

RMSProp sits in a clear lineage:

- **SGD**: $w_t = w_{t-1} - \eta g_t$. One learning rate, no adaptation. Fast to compute.
- **AdaGrad**: divides by $\sqrt{G_t}$ (sum of squared gradients). Adaptive, but learning rate decays to zero.
- **RMSProp**: divides by $\sqrt{s_t}$ (decaying average of squared gradients). Adaptive, learning rate recovers. No momentum.
- **Adam**: RMSProp + momentum. Adds a decaying average of the gradient itself (first moment) and bias correction. The most popular optimizer.

If you set $\beta_1 = 0$ in Adam (no momentum) and remove bias correction, you get RMSProp.

---

## Where RMSProp Is Used

- **Reinforcement learning**: RMSProp was the default optimizer for DQN (the Atari game-playing agent), A3C, and many other RL algorithms. It is still commonly used in RL because the gradient statistics change rapidly as the policy evolves.
- **Recurrent networks**: before Adam, RMSProp was the recommended optimizer for RNNs and LSTMs. It handles the varying gradient magnitudes across time steps well.
- **When you want something simpler than Adam**: RMSProp has fewer hyperparameters (no $\beta_1$, no bias correction). Sometimes simpler is better.
- **When Adam overfits**: removing momentum can act as implicit regularization. Some researchers report better generalization with RMSProp than Adam on certain tasks.