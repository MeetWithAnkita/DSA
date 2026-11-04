words = ["bella", "label", "roller", "hello"]



# Step 1: Frequency of first word
freq = {}

for ch in words[0]:
    freq[ch] = freq.get(ch, 0) + 1

    # Step 2: Process remaining words
for word in words[1:]:
    current = {}
    for ch in word:
        current[ch] = current.get(ch, 0) + 1

    # Step 3: Keep minimum common frequency
    for ch in freq:
        freq[ch] = min(freq[ch], current.get(ch, 0))

# Step 4: Construct result
result = []

for ch, count in freq.items():
    result.extend([ch] * count)

print(result)
