s = "programming"
print(s.find("g"))
print(s.find("z"))


print(s.index("g"))
# print(s.index("z"))
# If the character doesn't exist: it raises an error.

print("-"*10, " count ", "-"*10)
print("banana".count("a"))


print("-"*10, " STARTWITH() ", "-"*10)
s = "Python Developer"
print(s.startswith("Python"))
print(s.endswith("ankita"))



print("-"*10, " strip ", "-"*10)
r = "  Ankita  Das  "
print(r.strip())
print(r.lstrip())
print(r.rstrip())



print("-"*10, " SPLIT ", "-"*10)
sen = "I Love Python"
words = sen.split()
print(words)
print(len(words))
print(type(words))
# String --> split() --> List of words
print(words[1])
print(words[-1])


print("-"*10, " JOIN ", "-"*10)
w = ["I", "love", "Ankita"]
s = " ".join(w)
print(s)

a = "-".join(["2026", "09", "16"])
print(a)

# split() → String → List
# join()  → List   → String
