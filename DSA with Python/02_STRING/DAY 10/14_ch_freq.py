# Find:
# Number of unique characters
# Number of duplicate characters

# Expected:
# Unique characters: 5
# Duplicate characters: 3

s = "programming"
uni = 0
dch = 0 
freq = {}
for i in s:
    freq[i] = freq.get(i, 0) + 1 
for i in freq:
    if freq[i] == 1:
        uni += 1 
    else:
        dch += 1 
print("Unique characters: ", uni)
print("Duplicate characters: ", dch)
