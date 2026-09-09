arr = [10, 45, 23, 67, 12]
# arr = [11, 20, 30, 40, 50]
# arr = [50, 40, 30, 20, 10]
# arr = [40, 10, 20, 30, 50]

# smallest = arr[len(arr) - 1] # very small = smallest 
# small_2nd = arr[len(arr) - 1]  # 2nd small 
smallest = float('inf')
small_2nd = float('inf')
#  [].. >> sm >> vsm]

for i in arr :
    if i < smallest:
        small_2nd = smallest 
        smallest = i 
    elif i < small_2nd:
        small_2nd = i

print("Second smallest: ", small_2nd)