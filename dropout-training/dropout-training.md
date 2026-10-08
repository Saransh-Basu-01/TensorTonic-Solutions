## The Overfitting Problem

A neural network with millions of parameters can memorize the training data instead of learning general patterns. It achieves near-perfect accuracy on training examples but performs poorly on new, unseen data. This is **overfitting**.

Signs of overfitting:

- Training loss keeps decreasing, but validation loss starts increasing
- The model learns noise and quirks specific to the training set
- Performance degrades on real-world inputs

Several techniques exist to combat this (weight decay, data augmentation, early stopping), but dropout is one of the most effective and widely used.

---

## What Dropout Does

During each training step, dropout **randomly sets a fraction of the neurons to zero**. Each neuron has a probability $p$ of being "dropped" (set to zero) and a probability $1 - p$ of being "kept."

For example, with $p = 0.5$ and a layer of 4 neurons with values $[3.0, 1.0, 4.0, 2.0]$, one possible outcome is:

- Neuron 1: kept
- Neuron 2: **dropped** (set to 0)
- Neuron 3: kept
- Neuron 4: **dropped** (set to 0)

Result before scaling: $[3.0, 0.0, 4.0, 0.0]$

The dropped neurons are chosen randomly and independently. Each training step uses a **different random pattern**. The network never knows which neurons will be available, so it cannot rely on any single neuron or any specific combination of neurons.

---

## Why Random Dropping Helps

The key intuition: dropout prevents **co-adaptation**.

Without dropout, neurons can develop complex co-dependencies. Neuron A might learn to rely on neuron B always being there to correct its errors. If B is always present during training, this strategy works on the training set. But it makes the network fragile. Any small perturbation can break the delicate coordination.

With dropout, neuron A cannot count on neuron B being present. On some training steps B is there, on others it is not. So A must learn to be useful **on its own**. Every neuron is forced to learn features that are independently valuable.

This has several effects:

- **Reduces overfitting**: the network cannot memorize specific patterns that depend on all neurons being active simultaneously
- **Implicit ensemble**: each training step trains a slightly different sub-network (a random subset of neurons). The final model is like an average of all these sub-networks, similar to an ensemble of many smaller models
- **Robustness**: the network learns to function even when parts of it are missing, making it more resilient to noise

---

## The Scaling Problem

There is a catch. If you randomly zero out a fraction $p$ of the neurons, the expected sum of the layer's output drops by a factor of $(1 - p)$.

Without dropout, the expected output of a neuron with value $x_i$ is just $x_i$.

With dropout at rate $p$, the expected output is:

$$
E[\text{output}_i] = (1 - p) \cdot x_i + p \cdot 0 = (1 - p) \cdot x_i
$$

The expected value is now smaller by a factor of $(1 - p)$. This matters because the next layer in the network expects inputs of a certain magnitude. If the expected magnitude changes between training (with dropout) and inference (without dropout), the network's behavior will be inconsistent.

---

## Inverted Dropout: The Fix

The solution is to **scale up the surviving neurons** during training to compensate for the dropped ones. Each kept neuron gets multiplied by $\frac{1}{1-p}$:

$$
\text{output}_i = \begin{cases} 0 & \text{with probability } p \\ x_i \cdot \frac{1}{1-p} & \text{with probability } (1-p) \end{cases}
$$

Now check the expected value:

$$
E[\text{output}_i] = p \cdot 0 + (1-p) \cdot x_i \cdot \frac{1}{1-p} = x_i
$$

The expected value is exactly $x_i$, the same as without dropout. This is called **inverted dropout**, and it is the standard implementation used in practice (PyTorch, TensorFlow, etc.).

The alternative (standard dropout) does not scale during training and instead multiplies all outputs by $(1 - p)$ at inference time. Inverted dropout is preferred because it keeps inference simple: at test time, you just use all neurons without any modification.

---

## The Dropout Mask

The randomness in dropout is captured by a **mask** (also called the dropout pattern). The mask is an array with the same shape as the input:

- $0$ where the neuron is dropped
- $\frac{1}{1-p}$ where the neuron is kept

The output is simply: $\text{output} = x \cdot \text{mask}$ (element-wise multiplication).

For $p = 0.5$ and input $[2.0, 4.0]$, a possible mask is $[0, 2.0]$, giving output $[0, 8.0]$. Another possible mask is $[2.0, 0]$, giving $[4.0, 0]$.

Returning the mask alongside the output is useful because:

- During **backpropagation**, the same mask is applied to the gradients (dropped neurons get zero gradient)
- It makes the computation reproducible when using a seeded random generator

---

## Training vs. Inference

This is a critical distinction:

**During training**:
- Generate a random mask each forward pass
- Zero out dropped neurons
- Scale kept neurons by $\frac{1}{1-p}$

**During inference** (with inverted dropout):
- Use all neurons
- No scaling needed
- No randomness

The network uses its full capacity at test time. Because the training-time scaling already compensated for the missing neurons, no adjustment is needed at inference.

---

## Choosing the Dropout Rate

The dropout rate $p$ controls how aggressively you regularize:

- $p = 0$: No dropout at all. Every neuron is always active. No regularization effect.
- $p = 0.1$ to $0.2$: Light dropout. Common for input layers or when you have lots of training data.
- $p = 0.5$: The most common default for hidden layers. Each neuron is dropped half the time. This was the value used in the original dropout paper (Srivastava et al., 2014).
- $p = 0.8$ or higher: Very aggressive. Only 20% of neurons survive each step. Used when overfitting is severe or the model is very large.
- $p \ge 1.0$: Invalid. Would drop all neurons, producing all zeros.

Different layers can use different dropout rates. A common pattern is lighter dropout (or none) on the input layer and heavier dropout on the larger hidden layers.

---

## Where Dropout Shows Up

- **Fully connected layers**: the original and most common use case. Standard practice in almost every MLP.
- **Convolutional networks**: spatial dropout drops entire feature maps instead of individual pixels, since neighboring pixels are highly correlated and dropping individual pixels is less effective.
- **Transformers**: dropout is applied after attention weights and after the feed-forward layers. GPT, BERT, and most large language models use dropout during training.
- **Recurrent networks**: dropout is applied to the inputs and outputs of RNN layers (but typically not to the recurrent connections, where a technique called variational dropout is used instead).
- **Fine-tuning**: increasing dropout when fine-tuning a pretrained model on a small dataset is a common strategy to prevent overfitting to the new data.