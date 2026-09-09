arr = [25, 10, 45, 5, 30, 15]

largest = float('-inf')
Index_l = 0
smallest = float('inf')
Index_s = 0

for i, value in enumerate(arr):
    if value > largest:
        largest = value
        Index_l = i
    if value < smallest:
        smallest = value 
        Index_s = i
print("Largest: ", largest, "Index: ", Index_l)
print("Smallest: ", smallest, "Index: ", Index_s)