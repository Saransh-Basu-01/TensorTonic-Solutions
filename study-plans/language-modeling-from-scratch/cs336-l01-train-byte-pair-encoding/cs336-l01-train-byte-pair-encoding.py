def train_bpe(corpus, vocab_size):
    # Step 1: strings -> lists of UTF-8 byte ints
    tokenized = [list(s.encode("utf-8")) for s in corpus]

    # Step 2: token ID -> byte values
    token_bytes = {i: [i] for i in range(256)}

    # Step 3: outputs
    vocab = []
    merges = []
    next_id = 256

    # Step 4: early exit
    if vocab_size <= 256:
        return {"vocab": vocab, "merges": merges}

    # Step 5: main loop
    while next_id < vocab_size:
        # Step 6: count adjacent pairs (overlapping, per string)
        pair_counts = {}
        for tokens in tokenized:
            for i in range(len(tokens) - 1):
                pair = (tokens[i], tokens[i + 1])
                pair_counts[pair] = pair_counts.get(pair, 0) + 1

        # Step 7: no pairs left
        if not pair_counts:
            break

        max_count = max(pair_counts.values())

        # Tie-break: compare the PAIR of byte strings (left first, then right),
        # NOT the concatenation, and NOT the token IDs.
        best_pair = None
        best_key = None
        for pair, count in pair_counts.items():
            if count != max_count:
                continue
            key = (token_bytes[pair[0]], token_bytes[pair[1]])
            if best_key is None or key > best_key:
                best_key = key
                best_pair = pair

        left, right = best_pair

        # Step 8: create new token
        new_id = next_id
        token_bytes[new_id] = token_bytes[left] + token_bytes[right]
        merges.append([left, right, new_id])
        vocab.append([new_id, token_bytes[new_id]])
        next_id += 1

        # Step 9: replace left-to-right, non-overlapping
        new_tokenized = []
        for tokens in tokenized:
            out = []
            i = 0
            n = len(tokens)
            while i < n:
                if i < n - 1 and tokens[i] == left and tokens[i + 1] == right:
                    out.append(new_id)
                    i += 2
                else:
                    out.append(tokens[i])
                    i += 1
            new_tokenized.append(out)
        tokenized = new_tokenized

    return {"vocab": vocab, "merges": merges}

