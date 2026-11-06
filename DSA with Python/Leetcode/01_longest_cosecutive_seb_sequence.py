def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0

    for num in num_set:

        # Step 1: Check whether num is the starting number
        if num-1 not in num_set:
            current = num 
            count = 1 
            while current + 1 in num_set:
                current += 1 
                count += 1
            longest = max(longest, count)  

            # Step 2: Initialize current_num and count

            # Step 3: Count consecutive numbers using while

            # Step 4: Update longest

    return longest


nums = [100, 4, 200, 1, 3, 2]
print(longest_consecutive(nums))  # Expected: 4