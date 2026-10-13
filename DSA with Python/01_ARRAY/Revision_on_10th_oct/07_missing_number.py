arr = [1, 2, 4, 5]
n = 5

# An array contains distinct numbers from 1 to n, with exactly one number missing.
total = (int(n) * (int(n) + 1)) // 2
t = 0
for i in arr:
    t += i
print(total - t)