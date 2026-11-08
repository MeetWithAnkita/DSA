'''
Given a string, determine whether it is a palindrome, considering only alphanumeric characters and ignoring cases.
'''

s = "A man, a plan, a canal: Panama"

def check_pallindrome(s):
    left = 0 
    right = len(s) - 1 
    s = s.lower()
    while left < right:
        if s[left].isalnum() == False:
            left += 1 
            continue
        if s[right].isalnum() == False:
            right -= 1 
            continue
        if s[left] == s[right]:
            left += 1 
            right -= 1

        else:
            return False 
    return True

print(check_pallindrome(s))


'''
Complexity	Value	Reason
Time	O(n)	Each pointer traverses the string at most once
Auxiliary space	O(1)	Only two pointers are used

Strictly speaking, s.lower() creates a new string, so total auxiliary space including that conversion is O(n). If we use s[left].lower() and s[right].lower() during comparisons instead, the auxiliary space is O(1).
4. Interview explanation
You can explain:

"I used the Two Pointers approach. 
One pointer starts from the beginning and the other from 
the end. I skip non-alphanumeric characters and compare the
remaining characters without considering case. If any pair 
doesn't match, I return False. Otherwise, I return True."

'''