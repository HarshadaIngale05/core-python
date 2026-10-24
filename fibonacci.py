# Using For Loop
a = 0
b = 1

for i in range(10):
    print(a, end="")
    a, b = b, a + b

# Using While loop
a = 0
b = 1
count = 0

while count < 10:
    print(a, end="")
    a,b = b,a + b
    count += 1

# Reverse a number using for loop and while loop
num = 1234
rev = 0
digit = 0

for i in range(len(str(num))):
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
print(rev)    

num = 1234
rev = 0
digit = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
print(rev)    
