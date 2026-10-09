s = "babad"
max_len = 0
max_pall = []
sub_strings = []

for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        if len(s[i:j]) != 1:
            if not sub_strings:
                sub_strings.append(s[i:j])
            else: 
                if s[i:j] not in sub_strings:
                    sub_strings.append(s[i:j])
print(sub_strings)

for j in sub_strings:
    l = 0 
    r = len(j)-1
    pal = True
    while l < r:
        if j[l] == j[r]:
            l += 1 
            r -= 1 
        else:
            pal = False
            break

    if pal: 
        cur_len = len(j)
        if max_len <= cur_len:
            max_len = cur_len
            max_pall.append(j)
print("Max Pallindrome: ", max_pall)
# print(sub_strings)
