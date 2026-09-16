# /////////// 1st Way ///////////
# s = "Python"
# rev = ""
# for i in s:
#     rev = i + rev 
# print(rev)

# Complexity
# For this basic Python approach:
# Time: O(n²) in the worst case because strings are immutable and a new string is built repeatedly.
# Space: O(n)


# ////////// 2nd Way ///////////
# Print a string in reverse using indexing and range().
s = "Python"
rev = ""
for i in range(len(s)-1, -1, -1 ):
    rev += s[i]
print(rev)

# Complexity
# Time: O(n²) due to repeated string concatenation
# Space: O(n)