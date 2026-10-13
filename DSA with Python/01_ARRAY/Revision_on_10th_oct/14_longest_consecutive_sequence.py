arr = [100, 4, 200, 1, 3, 2]

# Task:
# Find the length of the longest sequence of consecutive numbers.
num_set = set(arr)
longest = 0 
for i in num_set:
    if (i-1) not in num_set:
        count = 1 
        current = i

        while (current + 1) in num_set:
            current += 1 
            count += 1 

        longest = max(longest, count)
print(longest)
