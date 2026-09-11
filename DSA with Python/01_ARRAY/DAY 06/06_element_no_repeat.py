arr = [5, 4, 1, 2, 4, 3, 1, 4, 2]

# Task: Find the first element whose frequency is exactly 1.
# Output: First non-repeating element: 3

freq= {} #dict
for i in arr:
    if i in freq:
        freq[i] += 1 
    else:
        freq[i] = 1 
print("First non-repeating element: ", )
for i in freq:
    if freq[i] == 1:
        print(i)
        break
# Complexity
# Frequency-building loop → O(n) average
# Finding first non-repeating → O(n)
# Total → O(n) average
# Extra space → O(n)