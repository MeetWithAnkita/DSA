# For Case 
# s = "abCdEf"
# target = "ace"
# s = s.lower()
# target = target.lower()

s = "A b C d E"
target = "ace"

s = s.replace(" ","")
target = target.replace(" ","")

s = s.lower()
target = target.lower()

i = 0
j = 0 
while i<len(s) and j < len(target):
    if s[i] == target[j]:
        j+= 1 
    i += 1 
if j == len(target):
    print("True")
else:
    print("False")
