s = "I am learning Python"
l = s.split()
print("List: ",l)
print("No of words: ", len(l))

# ⏱️ Complexity
# Time: O(n)
# Space: O(n) — because split() creates a list of words.

l1 = l[::-1]
print(" ".join(l1))

# ⏱️ Complexity
# Time: O(n)
# Space: O(n)