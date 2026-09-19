## What is Sequence Padding?

Sequence padding transforms variable-length sequences into fixed-length ones by adding special padding tokens. In NLP, sentences have different word counts; in time series, recordings have different durations. Neural networks require fixed-size tensor inputs, so padding is essential for creating batches.

---

## Why Padding is Necessary

**Batch processing requirement**: Neural networks process data in batches for efficiency. A batch must be a rectangular tensor where all sequences have the same length.

**GPU efficiency**: GPUs perform best with fixed-size operations. Variable-length inputs require sequential processing, losing parallelism benefits.

**API constraints**: Framework functions expect arrays/tensors with consistent shapes.

---

## The Padding Process

Given sequences of different lengths:

1. Determine the target length (max length in batch or specified value)
2. For sequences shorter than target: add padding tokens
3. For sequences longer than target: truncate

**Padding position**:
- **Post-padding** (most common): Add padding at the end
- **Pre-padding**: Add padding at the beginning

---

## Mathematical Representation

For a batch of $B$ sequences with lengths $l_1, l_2, ..., l_B$ and target length $L$:

$$
L = \max(l_1, l_2, ..., l_B) \quad \text{if max\_len is None}
$$

For each sequence $s_i$ with length $l_i$:

$$
\text{padded\_length} = L
$$

$$
\text{padding\_needed} = \max(0, L - l_i)
$$

$$
\text{truncation\_needed} = \max(0, l_i - L)
$$

---

## Worked Example: Post-Padding

**Input sequences** (token IDs):
- Sequence 0: [5, 12, 8] (length 3)
- Sequence 1: [3, 7, 2, 9, 1] (length 5)
- Sequence 2: [6] (length 1)

**Target length**: max(3, 5, 1) = 5

**Padding value**: 0

**Post-padded result**:
- Sequence 0: [5, 12, 8, 0, 0]
- Sequence 1: [3, 7, 2, 9, 1]
- Sequence 2: [6, 0, 0, 0, 0]

**Output shape**: (3, 5) - a proper rectangular matrix

---

## Worked Example: Pre-Padding

**Same input sequences, pre-padding**:

- Sequence 0: [0, 0, 5, 12, 8]
- Sequence 1: [3, 7, 2, 9, 1]
- Sequence 2: [0, 0, 0, 0, 6]

**When to use pre-padding**: For sequence models where the last token is most important (e.g., classification based on final hidden state).

---

## Truncation

When sequences exceed the maximum length:

**Post-truncation**: Keep the first max_len tokens
- [1, 2, 3, 4, 5, 6, 7] with max_len=4 → [1, 2, 3, 4]

**Pre-truncation**: Keep the last max_len tokens
- [1, 2, 3, 4, 5, 6, 7] with max_len=4 → [4, 5, 6, 7]

**Choice depends on task**:
- Sentiment analysis: Beginning often contains thesis statement (post-truncation)
- Next word prediction: Recent context matters most (pre-truncation)

---

## Choosing the Padding Value

**Common choices**:
- 0: Most common, easy to identify
- -1: Distinguishes from valid token ID 0
- Special token ID: [PAD] token from vocabulary

**Requirements**:
- Should not conflict with valid data values
- Embedding layers should map padding to zero vectors
- Attention masks should exclude padding positions

---

## Handling Empty Input

When the input list of sequences is empty:

**Expected output**: Array with shape (0, 0)
- Zero sequences
- Zero features per sequence

This preserves type consistency and allows downstream operations to proceed without special cases.

---

## Interaction with Attention Masks

Padding tokens should not affect model predictions. Attention masks indicate which positions are real vs padded:

$$
\text{mask}_i = \begin{cases} 1 & \text{if position } i \text{ is real} \\ 0 & \text{if position } i \text{ is padding} \end{cases}
$$

**Example**: Sequence [5, 12, 8, 0, 0]
- Attention mask: [1, 1, 1, 0, 0]

Transformers use this mask to set attention weights to negative infinity for padded positions, effectively ignoring them.

---

## Determining Maximum Length

**Dynamic (per batch)**:
- max_len = max(sequence lengths in batch)
- Most memory efficient
- Different batches have different shapes

**Fixed**:
- max_len = predetermined constant
- Consistent tensor shapes
- May waste memory or lose information

**Considerations**:
- Training vs inference: Fixed shapes often required for compiled models
- Memory: Long sequences dominate memory usage
- Information loss: Truncating long sequences discards data

---

## Worked Example with Truncation

**Input sequences**:
- Sequence 0: [1, 2, 3, 4, 5, 6, 7, 8] (length 8)
- Sequence 1: [10, 20] (length 2)
- Sequence 2: [5, 6, 7, 8, 9] (length 5)

**max_len = 4, padding_value = 0, post-truncation**:

- Sequence 0: [1, 2, 3, 4] (truncated from 8 to 4)
- Sequence 1: [10, 20, 0, 0] (padded from 2 to 4)
- Sequence 2: [5, 6, 7, 8] (truncated from 5 to 4)

**Output shape**: (3, 4)

---

## Output Data Type

The output should be a NumPy array with integer dtype (typically int32 or int64):

- Token IDs are integers
- Padding values are integers
- Integer arrays are more memory efficient than float arrays
- Consistent dtype ensures compatibility with embedding lookups

---

## Bucketed Padding

For large datasets, grouping sequences by similar length before padding reduces wasted space:

**Bucket strategy**:
- Group sequences by length ranges (e.g., 0-50, 51-100, 101-150)
- Pad within each bucket
- Reduces total padding tokens significantly

**Trade-off**: More complex batching logic vs memory efficiency

---

## Where Sequence Padding Shows Up

- **Text Classification**: Variable-length reviews/tweets padded for batch processing

- **Machine Translation**: Source and target sequences padded independently

- **Named Entity Recognition**: Token-level predictions require consistent sequence lengths

- **Time Series Classification**: Variable-length recordings aligned

- **Speech Recognition**: Audio segments of different durations

- **DNA Sequence Analysis**: Gene sequences of varying lengths

- **Music Generation**: Musical phrases with different numbers of notes

- **Video Analysis**: Clips with different frame counts
