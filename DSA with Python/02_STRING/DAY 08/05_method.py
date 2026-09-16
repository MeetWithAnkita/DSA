s = "PyThOn"
print("-"*10,"LOWER","-"*10)
print(s.lower())
print(s.islower())

print("-"*10,"UPPRR","-"*10)
print(s.upper())
print(s.isupper())

print("-"*10,"SWAPCASE","-"*10)
print(s.swapcase())

print("-"*10,"CHECK","-"*10)
print("Python".isalpha())
print("Python123".isalpha())
print("123".isdigit())
print("Python123".isalnum())


print("-"*10," SLICING ","-"*10)
# s = "PyThOn"
print(s[1:5]) #yThO
print(s[::2])   #PTO
print(s[::-1])  #nOhTyP
print(s[5:1:-1])    #nOhT

print(s[0])