arr = [4, 2, 2, 8, 3, 3, 3, 1]

# Write Python code to sort the numbers by 
# their frequency in descending order.

freq = {}
for i in arr:
    freq[i] = freq.get(i, 0) + 1

print(freq)

arr1 = sorted(arr, key = lambda x: freq[x], reverse = True)
arr2 = sorted(arr, key = lambda x: freq[x])
print(arr1)
print(arr2)