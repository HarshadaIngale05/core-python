# Using For Loop
num = 153
digits = str(num)
total = 0
power = len(digits)

for digit in digits:
    total += int(digit) ** power
if total == num:
    print("Armstrong number")
else:
    print("Not Armstrong Number")        

# Using While Loop
num = 153
temp = num
total = 0
power = len(str(num))

while num >0:
    digit = num % 10
    total += digit ** power
    num = num // 10

if total == temp:
    print("Armstrong number")
else:
    print("Not an Armstrong number")       


# Prime number using For Loop and While Loop
num = 7
count = 0

for i in range(1,8):
    if num % i == 0:
         count += 1

if count == 2:
        print("Prime number")
else:
       print("Not a Prime number")   


num = 7
count = 0
i = 1

while i <= num:
     if num % i == 0:
          count += 1
     i+=1

if count == 2:
    print("This is a prime number")
else:
     print("Not a Prime number")
                   