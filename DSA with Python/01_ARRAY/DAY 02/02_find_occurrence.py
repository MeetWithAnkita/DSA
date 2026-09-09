arr = [10, 20, 30, 20, 40, 20]
target = 20 

count = 0 
for i in range(len(arr)):
    if arr[i] == target:
        # print("Fitst Occurrence: ", i)
        # break

        # print all indexs  
        # print(i)

        # freq
        count += 1 
print("Target Frequency: ", count)
