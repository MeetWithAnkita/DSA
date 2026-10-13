arr = [3, 1, 3, 2, 1]

arr_l = []
for i in arr:
    if i not in arr_l:
            arr_l.append(i)
        
print(arr_l)