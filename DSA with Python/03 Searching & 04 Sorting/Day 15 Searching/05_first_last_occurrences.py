arr = [4, 7, 2, 7, 9, 7, 5]
target = 7
# index = []
# for i in range(len(arr)):
#     if target == arr[i]:
#         index.append(i)
# print("First Occurrences: ", index[0])
# print("Last Occurrences: ", index[-1])

first = -1 
last = -1 

for i in range(len(arr)):
    if target == arr[i]:
        if first == -1:
            first = i
        last = i
print("First ", first)
print("Last: ", last)



    