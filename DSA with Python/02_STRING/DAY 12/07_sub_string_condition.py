# # Task:
# # Check whether there is any substring of length k 
# # containing all unique characters.

s = "abcabcbb"
# s = "aaaaaaabc"
k = 3
uni = False

for i in range(len(s) - k + 1):

    window = s[i:i+k] #abc
    freq = {}
    for j in window:
        freq[j] = freq.get(j, 0) + 1
    # a:1, b:1, c:1
    uni = True

    for j in window:
        if freq[j] != 1:
            uni = False
            break

    if uni:
        break

if uni:
    print("True")
else:
    print("False")



# ////////2nd way
# s = "abcabcbb"
# k = 3

# for i in range(len(s) - k + 1):

#     window = s[i:i+k]

#     if len(window) == len(set(window)):
#         print("True")
#         break
# else:
#     print("False")

