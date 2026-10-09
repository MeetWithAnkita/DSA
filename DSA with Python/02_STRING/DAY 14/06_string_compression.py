s = "aaabbccccd"
# expected Output: "a3b2c4d1"
# # //////////////one way/////////////////////
# result = ""
# count = 0
# for ch in s:
#     if ch not in result:
#         if not result:
#             result += ch
#             count += 1 
#         else:
#             result += str(count)
#             count = 1
#             result += ch
#     elif ch in result:
#         count += 1 
# if count:
#     result += str(count)
# print(result)

result = ""
count = 1

for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        count += 1
    else:
        result += s[i - 1] + str(count)
        count = 1

result += s[-1] + str(count)

print(result)

