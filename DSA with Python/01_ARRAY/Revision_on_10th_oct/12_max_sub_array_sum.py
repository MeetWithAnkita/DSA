arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum = float('-inf')
total = 0

for i in arr:
    total += i
    if total < i:
        total = i 
    if total > max_sum:
        max_sum = total
print(max_sum)

