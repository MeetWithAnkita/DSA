s = "aabcccccaaa"

max_count = 0
var = ""
count = 1

for i in range(1, len(s)):
    if s[i] == s[i-1]:
        count += 1
    else:
        if count > max_count:
            max_count = count 
            var = s[i-1]
        count = 1
if count > max_count:
    max_count = count 
    var = s[i-1]
print(var)


