arr = [1, 2, 3]

for i in range(len(arr)):
    total = 0 
    for j in range(i, len(arr)):
        total += arr[j]
        # print(arr[i:j+1], "->", sum(arr[i:j+1]))
        print(arr[i:j+1], "->", total)

# Complexity

# For this approach:

# Time: O(n²) for processing all start/end combinations
# Extra Space: O(1) excluding the temporary slice used only for printing

# This same idea—maintaining a running sum—will be very important 
# when we reach ==> "Maximum Subarray Sum" / "Kadane's Algorithm".
