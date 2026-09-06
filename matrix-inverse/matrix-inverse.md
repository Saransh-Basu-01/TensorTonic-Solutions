## What Is a Matrix Inverse?

The inverse of a matrix $A$ is another matrix, denoted $A^{-1}$, such that:

$$
A A^{-1} = A^{-1} A = I
$$

Where $I$ is the identity matrix (ones on the diagonal, zeros elsewhere).

Think of it like division for matrices. If $Ax = b$, then $x = A^{-1}b$. The inverse "undoes" the effect of multiplying by $A$.

---

## When Does an Inverse Exist?

Not every matrix has an inverse. For an inverse to exist, the matrix must be:

**Square:** The matrix must have the same number of rows and columns ($n \times n$).

**Non-singular:** The determinant must be non-zero: $\det(A) \neq 0$.

A matrix without an inverse is called **singular** or **non-invertible**. Singular matrices have:
- Determinant equal to zero
- At least one zero eigenvalue
- Linearly dependent rows (or columns)
- A null space larger than just the zero vector

---

## The 2x2 Case

For a $2 \times 2$ matrix, there is a simple formula:

$$
A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}
$$

$$
A^{-1} = \frac{1}{ad - bc} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}
$$

The term $ad - bc$ is the determinant. If it equals zero, the inverse does not exist.

**Example:**

$$
A = \begin{bmatrix} 4 & 7 \\ 2 & 6 \end{bmatrix}
$$

Determinant: $4(6) - 7(2) = 24 - 14 = 10$

$$
A^{-1} = \frac{1}{10} \begin{bmatrix} 6 & -7 \\ -2 & 4 \end{bmatrix} = \begin{bmatrix} 0.6 & -0.7 \\ -0.2 & 0.4 \end{bmatrix}
$$

**Verification:**

$$
A A^{-1} = \begin{bmatrix} 4 & 7 \\ 2 & 6 \end{bmatrix} \begin{bmatrix} 0.6 & -0.7 \\ -0.2 & 0.4 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}
$$

---

## Why Inverses Matter

**Solving linear systems:**

The system $Ax = b$ has solution $x = A^{-1}b$ (when $A$ is invertible). However, computing the inverse explicitly is usually not the best approach numerically. Direct solvers like LU decomposition are preferred.

**Understanding linear transformations:**

If $A$ represents a transformation (rotation, scaling, shearing), then $A^{-1}$ represents the inverse transformation. If $A$ rotates by 30 degrees, $A^{-1}$ rotates by -30 degrees.

**Change of basis:**

If $P$ is a change-of-basis matrix, then $P^{-1}$ converts back to the original basis. The formula for transforming a matrix to a new basis is $P^{-1}AP$.

---

## Properties of the Inverse

**Inverse of a product (order reverses!):**

$$
(AB)^{-1} = B^{-1} A^{-1}
$$

This is analogous to the transpose rule. To undo $AB$, first undo $B$, then undo $A$.

**Inverse of a transpose:**

$$
(A^T)^{-1} = (A^{-1})^T
$$

You can transpose first then invert, or invert first then transpose.

**Inverse of an inverse:**

$$
(A^{-1})^{-1} = A
$$

**Determinant of the inverse:**

$$
\det(A^{-1}) = \frac{1}{\det(A)}
$$

---

## Special Cases with Simple Inverses

**Diagonal matrices:**

If $D = \text{diag}(d_1, d_2, \ldots, d_n)$, then:

$$
D^{-1} = \text{diag}(1/d_1, 1/d_2, \ldots, 1/d_n)
$$

Just invert each diagonal element. Requires all $d_i \neq 0$.

**Orthogonal matrices:**

If $Q$ is orthogonal ($Q^T Q = I$), then:

$$
Q^{-1} = Q^T
$$

The inverse is just the transpose! Rotation matrices are orthogonal, which is why they are easy to invert.

**Triangular matrices:**

Upper and lower triangular matrices can be inverted efficiently using back-substitution. The inverse of a triangular matrix is also triangular.

---

## The General Formula (Adjugate)

For any invertible $n \times n$ matrix:

$$
A^{-1} = \frac{1}{\det(A)} \text{adj}(A)
$$

Where $\text{adj}(A)$ is the adjugate (or classical adjoint) matrix, formed by:
1. Computing the cofactor of each element
2. Transposing the result

This formula is elegant but computationally expensive for large matrices ($O(n!)$ for naive determinant computation). Practical algorithms use Gaussian elimination or decomposition methods.

---

## Numerical Considerations

**Ill-conditioned matrices:**

Even when an inverse technically exists, it may be numerically unstable. The condition number $\kappa(A)$ measures this:

$$
\kappa(A) = ||A|| \cdot ||A^{-1}||
$$

A large condition number (e.g., $10^{10}$) means small changes in $A$ or $b$ cause huge changes in $A^{-1}b$. The matrix is "nearly singular."

**Avoid explicit inversion:**

In practice, you rarely compute $A^{-1}$ explicitly. Instead:
- To solve $Ax = b$, use LU decomposition or QR decomposition
- To compute $A^{-1}b$, solve the system directly
- NumPy's \texttt{np.linalg.solve(A, b)} is more accurate than \texttt{np.linalg.inv(A) @ b}

---

## Singular Matrices: What Happens?

When $A$ is singular:
- $\det(A) = 0$
- The system $Ax = b$ has either no solution or infinitely many solutions
- $A$ maps some non-zero vectors to zero (the null space is non-trivial)

Attempting to invert a singular matrix in code will either raise an error or produce garbage due to division by zero (or near-zero values).

---

## The Moore-Penrose Pseudoinverse

When $A$ is not invertible (or not even square), the pseudoinverse $A^+$ provides a generalized inverse:
- For overdetermined systems: $A^+ = (A^T A)^{-1} A^T$ (least squares)
- For underdetermined systems: $A^+ = A^T (A A^T)^{-1}$ (minimum norm)

The pseudoinverse always exists and gives the "best" solution in a least-squares sense.