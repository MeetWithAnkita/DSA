arr = [2, 1, 5, 1, 3, 2]
k = 3

max_t = 0
for i in range(len(arr) - k + 1):
    total = 0
    for j in range(i, i+k):
        total += arr[j]
    if max_t < total :
        max_t = total 
print(max_t)


# Time: O(n × k)
# Space: O(1)