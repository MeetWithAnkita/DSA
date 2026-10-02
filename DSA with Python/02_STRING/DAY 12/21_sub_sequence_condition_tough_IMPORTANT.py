# Count how many times a target can be formed as a subsequence.
# /////////// DYNAMIC PROGRAMMING USE HERE /////////////////


s = "babgbag"
target = "bag"

dp = [0] * (len(target) + 1)
dp[0] = 1 

for ch in s:
    for j in range(len(target) -1, -1, -1): # j --> (2, 1, 0)
        if ch == target[j]:
            dp[j+1] += dp[j] # dp[1] += dp[0]

print(dp[len(target)])