numbers = [45, 12, 89, 23, 67, 10]
# 5, 2, 9, 3, 7, 0

results = sorted(numbers, key = lambda x: x%10)
# Sort according to the last digit:
print(results)