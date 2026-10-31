students = [
    ("Ankita", 85),
    ("Riya", 92),
    ("Priya", 78),
    ("Sneha", 95)
]
# It is tuple

a = sorted(students, key = lambda x: x[1])
b = sorted(students, key = lambda x: x[1], reverse = True)

print(a)
print(b)