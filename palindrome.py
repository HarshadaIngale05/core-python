# Using For Loop
num = 1221
original = num
rev = 0
digit = 0

for i in range(len(str(num))):
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
if original == rev:
    print("This number is Palindrome")
else:
    print("Number is not Palindrome")     

# Using While Loop
num = 1222
original = num
rev = 0
digit = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

if original == rev:
    print("This is a Palindrome number")
else:
    print("This is not a Palindrome number")        

# Using String
text = "ram"

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")    