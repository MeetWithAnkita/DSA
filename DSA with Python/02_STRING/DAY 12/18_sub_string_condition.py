# s = "banana"
# target = "ana"

s = "aaaa"
target = "aa"

# Find how many times "ana" occurs in "banana".
# k = len(target)
# freq= {}
# for i in range(len(s) - k + 1):
#     freq[s[i: i+k]] = freq.get(s[i:i+k], 0) + 1 
# if target in freq:
#     print("Occurrences: ", freq[target])


count = 0
k = len(target)
for i in range(len(s) - k + 1):
    if s[i:i+k] == target:
        count += 1
print("Occurrences: ", count)


