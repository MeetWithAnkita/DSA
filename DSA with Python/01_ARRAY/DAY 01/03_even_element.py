arr = [5, 10, 15, 20, 22, 31, 40, 51]
e = 0 
for i in arr: 
    if i % 2 == 0:
        print(i)
        e += 1 
print("Total no of even elements: ", e)