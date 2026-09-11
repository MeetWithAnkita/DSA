# Task: We want to find which values occur more than once.
# Approach: Hashing

# Hashing = storing information so that we can quickly look it up later.
arr = [1, 3, 4, 3, 2, 2]
seen = {} #dict
for i in arr:
    if i not in seen:
        seen[i] = 1
        
    else:
        seen[i] += 1
        print("Duplicates: ", i)

# Average Time: O(n)
# Space: O(n)

 

