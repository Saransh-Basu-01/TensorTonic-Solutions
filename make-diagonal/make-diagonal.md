## What Is a Diagonal Matrix?

A **diagonal matrix** is a square matrix where all elements outside the main diagonal are zero. Only the entries $A_{ii}$ (where row index equals column index) can be nonzero.

$$
D = \begin{bmatrix} d_1 & 0 & 0 \\ 0 & d_2 & 0 \\ 0 & 0 & d_3 \end{bmatrix}
$$

The main diagonal runs from top-left to bottom-right.

---

## Creating a Diagonal Matrix

Given a vector of values $[d_1, d_2, ..., d_n]$, the diagonal matrix places each value on the corresponding diagonal position:

**Input vector:** $[3, 7, 2]$

**Output matrix:**

$$
\begin{bmatrix} 3 & 0 & 0 \\ 0 & 7 & 0 \\ 0 & 0 & 2 \end{bmatrix}
$$

Position $(0, 0)$ gets value 3, position $(1, 1)$ gets value 7, position $(2, 2)$ gets value 2. All other positions are 0.

---

## The Construction Process

**Step 1:** Create an $n \times n$ matrix filled with zeros, where $n$ is the length of the input vector.

**Step 2:** For each index $i$ from 0 to $n-1$, set position $(i, i)$ to the $i$-th element of the input vector.

**Example:**

Input: $[5, -2, 8, 1]$

Step 1: Create 4x4 zero matrix

$$
\begin{bmatrix} 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}
$$

Step 2: Fill diagonal positions

$$
\begin{bmatrix} 5 & 0 & 0 & 0 \\ 0 & -2 & 0 & 0 \\ 0 & 0 & 8 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}
$$

---

## Special Diagonal Matrices

**Identity matrix:**

Diagonal matrix with all 1s on the diagonal.

$$
I_3 = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}
$$

Created from vector $[1, 1, 1]$.

**Scalar matrix:**

Diagonal matrix with the same value repeated.

$$
\begin{bmatrix} 5 & 0 & 0 \\ 0 & 5 & 0 \\ 0 & 0 & 5 \end{bmatrix} = 5I_3
$$

Created from vector $[5, 5, 5]$.

**Zero matrix:**

Diagonal matrix with all zeros (trivially, the zero matrix itself).

---

## Properties of Diagonal Matrices

**Addition:**

The sum of two diagonal matrices is diagonal. Just add the corresponding diagonal elements.

$$
\begin{bmatrix} a & 0 \\ 0 & b \end{bmatrix} + \begin{bmatrix} c & 0 \\ 0 & d \end{bmatrix} = \begin{bmatrix} a+c & 0 \\ 0 & b+d \end{bmatrix}
$$

**Multiplication:**

The product of two diagonal matrices is diagonal. Multiply corresponding diagonal elements.

$$
\begin{bmatrix} a & 0 \\ 0 & b \end{bmatrix} \times \begin{bmatrix} c & 0 \\ 0 & d \end{bmatrix} = \begin{bmatrix} ac & 0 \\ 0 & bd \end{bmatrix}
$$

This is much simpler than general matrix multiplication.

**Powers:**

Raising a diagonal matrix to a power just raises each diagonal element to that power.

$$
D^k = \begin{bmatrix} d_1^k & 0 & 0 \\ 0 & d_2^k & 0 \\ 0 & 0 & d_3^k \end{bmatrix}
$$

**Inverse:**

The inverse of a diagonal matrix (if it exists) is diagonal with reciprocal elements.

$$
D^{-1} = \begin{bmatrix} 1/d_1 & 0 & 0 \\ 0 & 1/d_2 & 0 \\ 0 & 0 & 1/d_3 \end{bmatrix}
$$

The inverse exists only if no diagonal element is zero.

**Determinant:**

The determinant is the product of diagonal elements.

$$
\det(D) = d_1 \times d_2 \times ... \times d_n
$$

**Trace:**

The trace is the sum of diagonal elements.

$$
\text{tr}(D) = d_1 + d_2 + ... + d_n
$$

**Eigenvalues:**

The eigenvalues of a diagonal matrix are exactly the diagonal elements. The eigenvectors are the standard basis vectors.

---

## Diagonal Matrix Multiplication with Vectors

Multiplying a diagonal matrix by a vector scales each component independently:

$$
\begin{bmatrix} d_1 & 0 & 0 \\ 0 & d_2 & 0 \\ 0 & 0 & d_3 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} d_1 x_1 \\ d_2 x_2 \\ d_3 x_3 \end{bmatrix}
$$

This is equivalent to element-wise multiplication of the diagonal vector with the input vector.

**Computational advantage:** $O(n)$ instead of $O(n^2)$ for general matrix-vector multiplication.

---

## Applications in Machine Learning

**Scaling features:**

Diagonal matrices represent independent scaling of each feature dimension.

$$
X_{\text{scaled}} = X \cdot D
$$

where $D$ contains the scaling factors.

**Covariance matrices:**

When features are uncorrelated, the covariance matrix is diagonal. The diagonal elements are the variances.

$$
\Sigma = \begin{bmatrix} \sigma_1^2 & 0 & 0 \\ 0 & \sigma_2^2 & 0 \\ 0 & 0 & \sigma_3^2 \end{bmatrix}
$$

**Eigenvalue decomposition:**

Any diagonalizable matrix $A$ can be written as:

$$
A = V D V^{-1}
$$

where $D$ is a diagonal matrix of eigenvalues.

**Singular Value Decomposition (SVD):**

$$
A = U \Sigma V^T
$$

where $\Sigma$ is a diagonal matrix of singular values.

**Neural network weight initialization:**

Diagonal matrices can initialize weights for independent scaling per feature.

**Attention mechanisms:**

Diagonal attention matrices represent self-attention where each position only attends to itself.

---

## Extracting the Diagonal

The reverse operation extracts the diagonal from a matrix:

$$
A = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{bmatrix}
$$

Diagonal: $[1, 5, 9]$

This is useful for:
- Getting eigenvalues from a diagonalized matrix
- Computing the trace (sum of diagonal)
- Extracting variances from a covariance matrix

---

## Sparse Representation

Diagonal matrices are highly sparse. For an $n \times n$ diagonal matrix:
- Total elements: $n^2$
- Nonzero elements: at most $n$
- Sparsity: $(n^2 - n) / n^2 = 1 - 1/n$

For large $n$, this approaches 100% sparsity.

**Storage efficiency:**

Instead of storing $n^2$ values, store only $n$ diagonal values.

**Computational efficiency:**

Operations on diagonal matrices are $O(n)$ instead of $O(n^2)$ or $O(n^3)$.

---

## Off-Diagonal Matrices

Related concepts:

**Upper triangular:** All elements below the diagonal are zero.

**Lower triangular:** All elements above the diagonal are zero.

**Tridiagonal:** Nonzero elements only on the main diagonal and the two adjacent diagonals.

**Band matrix:** Nonzero elements only within a band around the diagonal.

Diagonal matrices are a special case where the band width is 1.