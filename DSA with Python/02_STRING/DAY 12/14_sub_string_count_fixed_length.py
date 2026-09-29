s = "abcdef"
k = 3
count = 0

for i in range(len(s) - k + 1):
    count += 1 
    print(s[i: i+k])
print("Total: ", count)
