arr = [10, 9, 5, 9, 5, 3, 5]
# find the element with the highest frequency.

max = float('-inf')
high = 0
freq = {} #dict

for i in arr:
    if i in freq:
        freq[i] += 1 
    else:
        freq[i] = 1 
    if max < freq[i]:
        max = freq[i]
        high = i
print("Highest frequency: ", high)

# Complexity
# Time: O(n) average
# Extra Space: O(n)