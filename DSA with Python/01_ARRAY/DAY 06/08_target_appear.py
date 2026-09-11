arr = [2, 5, 3, 2, 8, 5, 2, 9, 5]
target = 5
# task: Find how many times target appears in the array.

freq= {}
for i in arr:
    if i in freq:
        freq[i] += 1 
    else:
        freq[i] = 1
print(f"{target} appears {freq[target]} times.")

# Time: O(n) average
# Extra Space: O(n)