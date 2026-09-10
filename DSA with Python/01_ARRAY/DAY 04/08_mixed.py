# Your task

# Find and print:

# First occurrence of target
# Last occurrence of target
# Frequency of target
# First negative number and its index

arr = [12, -5, 8, 12, -3, 20, 12, 7]
target = 12
count = 0 

#index storing variable 
target_1st , target_last, N_1st = - 1 , - 1, -1 

for i in range(len(arr)):
    if arr[i] < 0:
        if N_1st == -1:
            N_1st = i 
    if arr[i] == target: 
        count += 1 
        if target_1st == -1:
            target_1st =  i 
        target_last = i 

print("Target First Occurrence: ", target_1st)
print("Target Last Occurrence: ", target_last)
print("Target Frequency: ", count)
print("First negative index: ", N_1st)
print("Fisrt negative value: ", arr[N_1st])

