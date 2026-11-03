arr = [1, 2, 3, 2, 4, 3, 5, 1]

freq = {}
for i in arr:
    freq[i] = freq.get(i, 0) + 1
for num, count in freq.items():
    if count > 1:
        print(num)