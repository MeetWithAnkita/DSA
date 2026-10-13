arr = [2, 4, 2, 7, 2]
target = 2
# occu = []
# for i in range(len(arr)):
#     if arr[i] == target:
#         occu.append(i)
# print("First Occurrence: ", occu[0])
# print("Last Occurrence: ", occu.pop())

first = -1
last = -1

for i in range(len(arr)):
    if arr[i] == target:
        if first == -1:
            first = i
        last = i
print("First Occurrence: ", first)
print("Last Occurrence: ", last)




