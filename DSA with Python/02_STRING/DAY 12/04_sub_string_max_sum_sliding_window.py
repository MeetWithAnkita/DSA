# Task:
# /the same problem using actual Sliding Window:

arr = [2, 1, 5, 1, 3, 2]
k = 3

window_sum = sum(arr[:k])
max_sum = window_sum 
for i in range(k, len(arr)):
    window_sum = window_sum - arr[i - k] + arr[i] 
    # 2 1 5 = 8 
    # - 1 5 1 = (8 - 2 + 1) = 7  
    # - - 5 1 3 = (7 - 1 + 3) = 9
    # - - - 1 3 2 = (9 - 5 + 2 ) = 6

    if window_sum > max_sum:
        max_sum = window_sum 
print(max_sum)

# | Approach         |     Time |    Space |
# | ---------------- | -------: | -------: |
# | Your brute force | O(n × k) |     O(1) |
# | Sliding Window   | **O(n)** | **O(1)** |


