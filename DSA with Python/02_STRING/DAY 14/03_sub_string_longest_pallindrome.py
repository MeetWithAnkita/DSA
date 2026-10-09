# s = "babad"
s = "forgeeksskeegfor"

# create sub-strings
# pallindrome 
# longest pallidrome -> string + length
sub_strings = []
for i in range(len(s)):
    for j in range(i+1, len(s) + 1):
        sub_strings.append(s[i: j])
max_len = 0
max_pall = []
for j in sub_strings:
    if len(j) != 1:
        if j == j[::-1]:
            if len(j) >= max_len:
                max_len = len(j)
                max_pall.append(j)
print("Max length: ",max_len)
print("Max Pallindrome: ", max_pall)

        