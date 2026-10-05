# s = "((()))"
# s = "))((()"
# s = "(()())"
s = "())("
s = ")(()))(("
# Task: Use a stack to check whether the parentheses are balanced.
# Balanced parentheses require two conditions:

# Number of ( = number of ) ✅
# At every point, we must have a ( available before we encounter its matching ) ❌

stack = []
for ch in s:
    if ch == "(":
        stack.append(ch)
    else:
        if not stack: #empty stack
            print("False")
            break
        stack.pop()
else:            
    if not stack :
        print("True")
    else:
        print("False")




