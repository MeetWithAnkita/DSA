s = "Python is a powerful language"
w = s.split()
print("First: ",w[0])
print("Last: ", w[len(w) - 1])


# ⏱️ Complexity
# split() → O(n) time
# Index access → O(1)
# Space → O(n) because split() creates the list