## What Is the Trace?

The **trace** of a square matrix is the sum of its diagonal elements. It is one of the simplest yet most useful matrix operations.

For an $n \times n$ matrix $A$:

$$
\text{tr}(A) = \sum_{i=1}^{n} A_{ii} = A_{11} + A_{22} + ... + A_{nn}
$$

Only square matrices have a trace. The diagonal runs from top-left to bottom-right.

---

## Computing the Trace

**Example 1: 2x2 matrix**

$$
A = \begin{bmatrix} 5 & 3 \\ 2 & 7 \end{bmatrix}
$$

$\text{tr}(A) = 5 + 7 = 12$

**Example 2: 3x3 matrix**

$$
B = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{bmatrix}
$$

$\text{tr}(B) = 1 + 5 + 9 = 15$

**Example 3: Identity matrix**

$$
I_3 = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}
$$

$\text{tr}(I_3) = 1 + 1 + 1 = 3$

The trace of the $n \times n$ identity matrix is always $n$.

---

## Properties of the Trace

**Linearity:**

$$
\text{tr}(A + B) = \text{tr}(A) + \text{tr}(B)
$$

$$
\text{tr}(cA) = c \cdot \text{tr}(A)
$$

**Transpose invariance:**

$$
\text{tr}(A) = \text{tr}(A^T)
$$

The trace is unchanged by transposition because the diagonal elements stay the same.

**Cyclic property:**

For two matrices:

$$
\text{tr}(AB) = \text{tr}(BA)
$$

This holds even for rectangular matrices: if $A$ is $n \times p$ and $B$ is $p \times n$, then $AB$ is $n \times n$ and $BA$ is $p \times p$, but both traces are equal.

More generally, you can cycle any number of matrices:

$$
\text{tr}(ABC) = \text{tr}(BCA) = \text{tr}(CAB)
$$

You can cycle the order, but not arbitrarily reorder them. Note: $\text{tr}(ABC) \neq \text{tr}(BAC)$ in general.

**Similarity invariance:**

$$
\text{tr}(PAP^{-1}) = \text{tr}(A)
$$

The trace is unchanged under similarity transforms. This follows directly from the cyclic property: $\text{tr}(PAP^{-1}) = \text{tr}(P^{-1}PA) = \text{tr}(A)$. Since similar matrices share eigenvalues, this is consistent with trace equaling the sum of eigenvalues.

**Product with transpose:**

$$
\text{tr}(A^T B) = \sum_{i,j} A_{ij} B_{ij}
$$

This equals the sum of element-wise products (related to the Frobenius inner product).

---

## Trace and Eigenvalues

A fundamental result: the trace equals the sum of eigenvalues.

$$
\text{tr}(A) = \sum_{i=1}^{n} \lambda_i
$$

where $\lambda_1, \lambda_2, ..., \lambda_n$ are the eigenvalues of $A$ (counted with multiplicity).

**Example:**

$$
A = \begin{bmatrix} 4 & 2 \\ 1 & 3 \end{bmatrix}
$$

$\text{tr}(A) = 4 + 3 = 7$

The eigenvalues are $\lambda_1 = 5$ and $\lambda_2 = 2$.

$\lambda_1 + \lambda_2 = 5 + 2 = 7$ (matches the trace)

This connection is useful because:
- Computing the trace is O(n)
- Computing all eigenvalues is O(n³)
- The trace gives partial information about eigenvalues cheaply

---

## Trace and Determinant

Another fundamental result: the determinant equals the product of eigenvalues.

$$
\det(A) = \prod_{i=1}^{n} \lambda_i
$$

Together, trace and determinant give you:
- Sum of eigenvalues (trace)
- Product of eigenvalues (determinant)

For a 2x2 matrix, knowing both fully determines the eigenvalues via the quadratic formula.

---

## Trace in Machine Learning

**Covariance matrix analysis:**

The trace of a covariance matrix equals the total variance:

$$
\text{tr}(\Sigma) = \sum_{i=1}^{n} \text{Var}(X_i)
$$

**Nuclear norm (trace norm):**

The nuclear norm of a matrix is the sum of its singular values:

$$
||A||_* = \sum_i \sigma_i = \text{tr}(\sqrt{A^T A})
$$

Used in low-rank matrix approximation and regularization.

**Frobenius norm:**

$$
||A||_F^2 = \text{tr}(A^T A) = \sum_{i,j} A_{ij}^2
$$

The squared Frobenius norm is the trace of $A^T A$.

**Loss functions:**

Some loss functions are expressed using trace:

$$
L = \text{tr}(A^T B)
$$

This computes the sum of element-wise products between matrices.

---

## Trace of Special Matrices

**Identity matrix:** $\text{tr}(I_n) = n$

**Zero matrix:** $\text{tr}(0) = 0$

**Diagonal matrix:** The eigenvalues are the diagonal entries, so $\text{tr}(D) = \sum_i D_{ii}$ gives the sum of eigenvalues directly.

**Triangular matrix:** Same as diagonal: the eigenvalues are the diagonal entries, so the trace is their sum.

**Projection matrix:** For any projection matrix $P$ (satisfying $P^2 = P$), $\text{tr}(P)$ equals the rank of $P$ (dimension of the subspace being projected onto).

---

## Trace Derivative

In matrix calculus, trace appears frequently because of this identity:

$$
\frac{\partial}{\partial A} \text{tr}(A^T B) = B
$$

And:

$$
\frac{\partial}{\partial A} \text{tr}(A B) = B^T
$$

These are used extensively in deriving gradients for machine learning.

---

## Computational Complexity

Computing the trace requires:
- Accessing $n$ diagonal elements
- Summing $n$ numbers
- Time complexity: $O(n)$
- Space complexity: $O(1)$

This makes trace one of the cheapest matrix operations. In contrast:
- Matrix multiplication: $O(n^3)$
- Eigenvalue decomposition: $O(n^3)$
- Determinant: $O(n^3)$

---

## Implementation Notes

**NumPy:**

The trace is computed by summing the diagonal:

1. Extract diagonal elements
2. Sum them

For a matrix stored in row-major order, diagonal elements are at positions $0, n+1, 2(n+1), ...$, which are not contiguous. Memory access is strided but still efficient.

**Numerical stability:**

Trace computation is numerically stable. No division, no subtraction of similar numbers. Just addition.