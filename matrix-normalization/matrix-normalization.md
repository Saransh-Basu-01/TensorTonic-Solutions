## What is Matrix Normalization?

Matrix normalization transforms the values in a matrix so that rows, columns, or the entire matrix meet certain criteria such as summing to one or having unit length. It ensures that different samples or features are comparable regardless of their original scales or magnitudes.

---

## Why Normalize Matrices?

**Probability interpretation**: When rows (or columns) sum to 1, entries can be interpreted as probabilities or proportions.

**Eliminating scale effects**: Samples with large absolute values do not dominate comparisons or distance calculations.

**Algorithm requirements**: Many algorithms (softmax, attention mechanisms, Markov chains) require normalized inputs.

**Numerical stability**: Normalization keeps values in reasonable ranges, preventing overflow/underflow.

---

## Types of Matrix Normalization

### Row Normalization (L1 - Sum to One)

Each row is divided by its sum so that all row entries add up to 1:

$$
x'_{ij} = \frac{x_{ij}}{\sum_{k} x_{ik}}
$$

**Use cases**:
- Converting counts to proportions
- Creating probability distributions over categories
- Transition matrices in Markov chains

**Example**:
- Original row: [2, 4, 4]
- Row sum: 2 + 4 + 4 = 10
- Normalized row: [0.2, 0.4, 0.4]

---

### Row Normalization (L2 - Unit Length)

Each row is divided by its Euclidean norm (L2 norm):

$$
x'_{ij} = \frac{x_{ij}}{\sqrt{\sum_{k} x_{ik}^2}}
$$

After normalization, each row has length 1: $\sqrt{\sum_k (x'_{ik})^2} = 1$

**Use cases**:
- Cosine similarity becomes dot product
- Text embeddings (TF-IDF vectors)
- Neural network weight initialization

**Example**:
- Original row: [3, 4]
- L2 norm: $\sqrt{3^2 + 4^2} = \sqrt{25} = 5$
- Normalized row: [0.6, 0.8]
- Verification: $\sqrt{0.6^2 + 0.8^2} = \sqrt{1} = 1$

---

### Column Normalization

Same operations applied column-wise instead of row-wise:

**L1 (sum to one)**:

$$
x'_{ij} = \frac{x_{ij}}{\sum_{k} x_{kj}}
$$

**L2 (unit length)**:

$$
x'_{ij} = \frac{x_{ij}}{\sqrt{\sum_{k} x_{kj}^2}}
$$

**Use cases**:
- Feature normalization when features are columns
- Doubly stochastic matrices (both rows and columns sum to 1)

---

### Global Normalization

Normalize using statistics computed over the entire matrix:

**Divide by global sum**:

$$
x'_{ij} = \frac{x_{ij}}{\sum_{m,n} x_{mn}}
$$

**Divide by global maximum**:

$$
x'_{ij} = \frac{x_{ij}}{\max_{m,n}(x_{mn})}
$$

---

## Mathematical Properties

**L1 normalization preserves**:
- Non-negativity (if original values are non-negative)
- Creates valid probability distributions

**L2 normalization preserves**:
- Direction of vectors (only magnitude changes)
- Angles between vectors

**Neither preserves**:
- Absolute magnitudes
- Differences between values (proportionally maintained but not absolutely)

---

## Worked Example: L1 Row Normalization

**Original matrix**:
- Row 0: [1, 2, 3]
- Row 1: [4, 0, 2]
- Row 2: [3, 3, 3]

**Step 1 - Compute row sums**:
- Row 0 sum: 1 + 2 + 3 = 6
- Row 1 sum: 4 + 0 + 2 = 6
- Row 2 sum: 3 + 3 + 3 = 9

**Step 2 - Divide each element by its row sum**:
- Row 0: [1/6, 2/6, 3/6] = [0.167, 0.333, 0.500]
- Row 1: [4/6, 0/6, 2/6] = [0.667, 0.000, 0.333]
- Row 2: [3/9, 3/9, 3/9] = [0.333, 0.333, 0.333]

**Verification**: Each row sums to 1.0

---

## Worked Example: L2 Row Normalization

**Original matrix**:
- Row 0: [3, 4]
- Row 1: [0, 5]

**Step 1 - Compute L2 norms**:
- Row 0: $\sqrt{3^2 + 4^2} = \sqrt{25} = 5$
- Row 1: $\sqrt{0^2 + 5^2} = \sqrt{25} = 5$

**Step 2 - Divide each element by its row norm**:
- Row 0: [3/5, 4/5] = [0.6, 0.8]
- Row 1: [0/5, 5/5] = [0.0, 1.0]

**Verification**: $\sqrt{0.6^2 + 0.8^2} = 1.0$ and $\sqrt{0^2 + 1^2} = 1.0$

---

## Handling Edge Cases

**Zero rows/columns**: If a row sums to zero (or has zero L2 norm), division is undefined.

Options:
- Leave as zeros (most common)
- Replace with uniform distribution [1/n, 1/n, ..., 1/n]
- Raise an error

**Negative values**: L1 normalization can produce negative probabilities if inputs are negative. Consider using absolute values or only applying to non-negative data.

**Very small denominators**: Can cause numerical instability. Add a small epsilon: $x'_{ij} = \frac{x_{ij}}{\text{norm} + \epsilon}$

---

## Normalization vs Standardization

**Normalization**: Scales values to a specific range or constraint
- L1: rows sum to 1
- L2: rows have unit length
- Min-max: values in [0, 1]

**Standardization**: Centers and scales by statistics
- Z-score: mean 0, standard deviation 1
- Does not constrain the range

The terms are sometimes used interchangeably, but they refer to different operations.

---

## Axis Selection

In matrix operations, "axis" determines the direction:
- **axis=0**: Operate along rows (result per column)
- **axis=1**: Operate along columns (result per row)

For row normalization (each sample normalized independently):
- Compute norm along axis=1
- Divide each row by its norm

For column normalization (each feature normalized independently):
- Compute norm along axis=0
- Divide each column by its norm

---

## Where Matrix Normalization Shows Up

- **Softmax Function**: Exponentiates and L1-normalizes to create probability distributions

- **Attention Mechanisms**: Query-key scores are normalized to create attention weights

- **Markov Chains**: Transition probability matrices have rows that sum to 1

- **PageRank**: Link matrices are L1 row-normalized

- **Information Retrieval**: TF-IDF vectors are L2-normalized for cosine similarity

- **Neural Networks**: Batch normalization, layer normalization, weight normalization

- **Recommender Systems**: User-item interaction matrices normalized for fair comparisons

- **Image Processing**: Pixel intensity normalization

- **Topic Modeling**: Document-topic and topic-word distributions

- **Bioinformatics**: Gene expression matrices normalized across samples
