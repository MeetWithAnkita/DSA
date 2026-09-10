# arr = [20, 10,  30, 20, 40, 20]
arr = [10, 20, 30, 40]
target = 20
count = 0 

Occurrence_1st = -1
Occurrence_last = -1

for i in range(len(arr)):
    if target == arr[i]:
        count += 1 
        if Occurrence_1st == -1:
            Occurrence_1st = i
        else:
            Occurrence_last = i 
print("Occurrence_1st: ", Occurrence_1st)
print("Occurrence_last: ", Occurrence_last)
print("Frequency: ",count)
