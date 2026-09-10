# Task: Find how many even numbers are present in the array.
arr = [10, 15, 20, 25, 30, 35, 40]
count = 0 
for i in arr: 
    if i % 2 == 0:
        count+= 1 
print("Even Count: ", count)