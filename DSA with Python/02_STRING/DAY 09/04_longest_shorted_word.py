s = "I love programming"
w = s.split()
minimum = float('inf')
l = 0
maximum = float('-inf')
s = 0
for i in w:
    if len(i) < minimum:
        minimum = len(i)
        s = i
    if len(i) > maximum:
        maximum = len(i)
        l = i
print("Longest: ", l)
print("Shortest: ", s)
