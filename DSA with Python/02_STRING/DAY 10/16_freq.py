# Find the first character whose frequency is exactly 1, and print:

# The character
# Its index
# Its frequency

# Expected:

# Character: c
# Index: 4
# Frequency: 1

s = "aabbcdde"
freq = {}
for i in s:
    freq[i] = freq.get(i, 0) + 1 
for i,value in enumerate(s): 
    if freq[value] == 1 :
        print("Character: ", value)
        print("Index: ", i)
        print("Frequency: ",freq[value])
        break
    
# ⏱️ Complexity
# Frequency calculation: O(n)
# Second traversal: O(n) worst case
# Overall: O(n)
# Space: O(k)