# Task: Print all substrings of length k that contain the character 'e'.

s = "abcdef"
k = 3

for i in range(len(s) - k + 1):
    if 'e' in s[i: i+k]:
        print(s[i: i+k])