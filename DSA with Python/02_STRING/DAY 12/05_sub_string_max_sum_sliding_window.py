arr = [1, 4, 2, 7, 3, 6]
k = 3

window_sum = sum(arr[:k])
max_sum = window_sum

for i in range(k, len(arr)):
    window_sum = window_sum - arr[i - k] + arr[i]
    if max_sum < window_sum :
        max_sum = window_sum 
print(max_sum)


# Complexity
# Time: O(n)
# Space: O(1)

# And most importantly, you've now implemented fixed-size Sliding Window successfully. 🎉