arr = [2, 4, 6, 8, 10]
k = 3

def avg_window(arr, k):
    result = []
    total = sum(arr[:k])
    result.append(total/k)
    for i in range(k, len(arr)):
        total = total - arr[i-k] + arr[i]
        result.append(total / k)
    return result

print(avg_window(arr, k))