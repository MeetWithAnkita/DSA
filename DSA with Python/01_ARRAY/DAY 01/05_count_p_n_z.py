arr = [10, -5, 0, 20, -3, 0, 7]
p=0
n=0
z=0
for i in arr:
    if i == 0:
        z += 1 
    elif i > 0 : 
        p += 1  
    else:
        n += 1 
print("Positive: ", p)
print("Negative: ", n)
print("Zero: ", z)