## What Is Gaussian Blur?

Gaussian blur is the most widely used smoothing filter in image processing. It removes high-frequency noise while preserving edges better than simple averaging. The blur effect is controlled by a parameter called sigma ($\sigma$).

---

## The Gaussian Function

The 2D Gaussian function is:

$$
G(x, y) = \frac{1}{2\pi\sigma^2} e^{-\frac{x^2 + y^2}{2\sigma^2}}
$$

Where:
- $(x, y)$ is the offset from the kernel center
- $\sigma$ is the standard deviation (controls blur amount)
- The function is symmetric around the center

---

## Building the Kernel

To create a Gaussian kernel:

**Step 1: Choose kernel size**
- Usually odd (3, 5, 7, etc.) so there is a center pixel
- Rule of thumb: size >= 6*sigma (capture most of the Gaussian)

**Step 2: Compute offsets**
- For size=5: center is at position 2
- Offsets range from -2 to +2

**Step 3: Apply Gaussian formula**
- For each position, compute G(x, y)
- This gives unnormalized weights

**Step 4: Normalize**
- Divide all values by their sum
- Ensures kernel sums to 1 (preserves brightness)

---

## Step-by-Step Example

**Parameters:** size = 3, sigma = 1.0

**Offsets:**

(-1,-1) (-1,0) (-1,1)
(0,-1)  (0,0)  (0,1)
(1,-1)  (1,0)  (1,1)

**Unnormalized weights (computing G(x,y)):**
- G(-1,-1) = exp(-(1+1)/2) = exp(-1) = 0.368
- G(-1,0) = exp(-(1+0)/2) = exp(-0.5) = 0.607
- G(0,0) = exp(-(0+0)/2) = exp(0) = 1.0
- (and so on for other positions)

**Kernel before normalization:**

0.368  0.607  0.368
0.607  1.000  0.607
0.368  0.607  0.368

**Sum:** 0.368*4 + 0.607*4 + 1.0 = 4.9

**Normalized kernel:**

0.075  0.124  0.075
0.124  0.204  0.124
0.075  0.124  0.075

This sums to 1.0.

---

## The Effect of Sigma

**Small sigma (e.g., 0.5):**
- Sharp Gaussian
- Most weight concentrated at center
- Minimal blurring
- Kernel can be small

**Medium sigma (e.g., 1.0):**
- Moderate spread
- Balanced blur
- Common default

**Large sigma (e.g., 3.0):**
- Wide Gaussian
- Weights spread far from center
- Strong blurring
- Needs larger kernel to capture tails

---

## Kernel Size vs. Sigma

The kernel should be large enough to capture most of the Gaussian:

**Rule of thumb:** kernel_size = ceil(6 * sigma) + 1 (round up to odd)

For sigma = 1: size >= 7 (but 5 or 3 often works)
For sigma = 2: size >= 13 (typically use 9 or 11)

If kernel is too small:
- Truncates the Gaussian tails
- Sum of raw values is less than expected
- Normalization compensates, but blur is slightly different

---

## Properties of Gaussian Blur

**Separability:**
The 2D Gaussian is separable:

$$
G(x, y) = G(x) \cdot G(y)
$$

This means a 2D convolution can be done as two 1D convolutions:
1. Blur horizontally with 1D kernel
2. Blur vertically with 1D kernel

This is much faster: O(n*k) instead of O(n*k^2) per pixel.

**Linearity:**
Blurring twice with sigma1 and sigma2 equals blurring once with:

$$
\sigma_{combined} = \sqrt{\sigma_1^2 + \sigma_2^2}
$$

---

## Gaussian vs. Box Blur

**Box blur (simple averaging):**
- All kernel weights equal (1/k^2)
- Faster to compute
- Creates visible artifacts (blocky edges)
- Not separable in the same nice way

**Gaussian blur:**
- Weights decay smoothly from center
- More natural-looking blur
- Better edge preservation
- Mathematically well-behaved

Gaussian blur is preferred for most applications.

---

## Applications

**Noise reduction:**
- Averaging reduces random noise
- Gaussian preserves edges better than uniform averaging

**Scale-space:**
- Different sigmas reveal features at different scales
- Used in SIFT feature detection

**Pre-processing:**
- Before edge detection (reduce noise sensitivity)
- Before downsampling (anti-aliasing)

**Artistic effects:**
- Background blur (bokeh simulation)
- Glow effects

---

## Implementation Tips

**Avoid computing exp() repeatedly:**
- The exponential is expensive
- Pre-compute all kernel values once

**Use symmetry:**
- Kernel is symmetric: G(-x,-y) = G(x,y)
- Can compute only one quadrant and mirror

**Handle normalization carefully:**
- Sum all values first
- Then divide each by the sum
- Ensures brightness is preserved