s = "python is easy python is powerful python"

# # output:  python is easy powerful

# l_s = s.split()
# s = []
# for i in l_s:
#     if i not in s:
#         s.append(i)
# print(" ".join(s))

# # Your version:
# # Time: potentially O(n²)
# # Space: O(n)

# /////// 2nd way ///////
words = s.split()
seen = set()
# result = []

for w in words:
    if w not in seen:
        seen.add(w)
        # result.append(w)
print(" ".join(seen))

