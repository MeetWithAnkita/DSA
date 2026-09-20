s1 = "listen"
s2 = "silent"
s1 = sorted(s1)
s2 = sorted(s2)

if s1 == s2:
    print("Anagram")
else:
    print("Not Anagram")

# ⏱️ Complexity

# For strings of length n:

# sorted(s1) → O(n log n)
# sorted(s2) → O(n log n)
# comparison → O(n)

# So overall:

# Time: O(n log n)

# Space: O(n) because sorted() creates lists.