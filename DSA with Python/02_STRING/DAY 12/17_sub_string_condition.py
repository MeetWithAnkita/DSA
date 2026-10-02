# Task:
# Count Distinct Fixed-Size Substrings
# Find the number of distinct substrings of length k.

# s = "abcabc"
# k = 3
# seen = set()
# # count = 0 
# freq = {}

# for i in range(k):
#     freq[s[i]] = freq.get(s[i], 0) + 1 
# if len(freq) == k:
#     print(s[:k])
#     seen.add(s[:k])

# for i in range(k, len(s)):
#         out = s[i - k]
#         freq[out] -= 1 
#         if freq[out] == 0 :
#              del freq[out]
#         freq[s[i]] = freq.get(s[i], 0) + 1 
#         w = s[i-k+1: i+1]
#         if w not in seen:
#             seen.add(w)
#             print(s[i-k+1: i+1])

# print("Count: ", len(seen))


s = "abcabc"
k = 3
seen = set()

for i in range(len(s) - k + 1):
    w = s[i: i+k]
    if w not in seen:
        seen.add(w)
print("COunt: ", len(seen))





