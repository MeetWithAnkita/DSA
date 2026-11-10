arr = [1, 12, -5, -6, 50, 3]
k = 4

def max_avg(arr, k):
    total = sum(arr[:k])
    max_avg = (total / k)
    for i in range(k, len(arr)):
        total = total - arr[i-k] + arr[i]
        max_avg = max(max_avg, total/k)
    return max_avg

print(max_avg(arr, k))