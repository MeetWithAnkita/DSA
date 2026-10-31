arr = [9, 3, 7, 1, 5]
a = arr.sort()
b = sorted(arr, reverse = True)
c = sorted(arr, reverse = False)

print(arr)
print(a)
print(b)
print(c)


# You correctly understood that 
# sort() modifies the original list, and 
# sorted() can sort that list in reverse order.