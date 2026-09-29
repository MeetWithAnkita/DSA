# Substring  → Continuous
# Subsequence → Order matters, continuity doesn't

# Every substring is a subsequence, but every subsequence is NOT a substring. ✅

# For a string of length n:
# Number of substrings = [n(n+1)​] // 2


# 🧠 Formula
# For a string of length n and fixed window size k:
# Number of windows=n−k+1


s = "abc"
for i in range(len(s)):             #i = 0 , j = 1,2,3,4 || i = 1 , j = 2, 3, 4 ||
    for j in range(i+1, len(s)+1):
        print(s[i : j])

# Complexity

# There are O(n²) possible substrings.

# Time: O(n²) loop combinations (ignoring the cost of slicing/printing)
# Extra space: O(1) apart from the temporary substring/output