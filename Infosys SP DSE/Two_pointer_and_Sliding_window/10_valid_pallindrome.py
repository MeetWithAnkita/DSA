s = "A man, a plan, a canal: Panama"

# Expected output: True

def check_valid_pallindrome(s):
    s = s.lower()
    left = 0 
    right = len(s) - 1 
    while left < right:
        if s[left].isalnum() == False:
            left += 1
        elif s[right].isalnum() == False:
            right -= 1 
        elif s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


print(check_valid_pallindrome(s))