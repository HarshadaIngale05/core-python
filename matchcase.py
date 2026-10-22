# Using marks
marks = 80
match marks :
    case 90|91|92|93|94|95:
        print("A Grade")
    case 80|81|82|83|84|85:
        print("B Grade")
    case 70|71|72|73|74|75:
        print("C Grade")
    case 60|61|62|63|64|65:
        print("D Grade")
    case 30|31|32|33|34|35: 
        print("Fail")
    case _:
        print("Invalid input")      

# Using Month Quarter
month = input("Enter the month :")
match month :
    case "January"|"February"|"March":
        print("quarter 1")
    case "April"|"May"|"June":
        print("quarter 2")
    case "July"|"August"|"September":
        print("quarter 3")
    case "October"|"November"|"December":
        print("quarter 4")
    case _:
        print("Invalid input")    

# Using Arithmetic Operator
a = 10
b = 5
operator = "%"
match operator:
    case "+":
        print("Addition of",a+b)
    case "-":
        print("Subtraction of", a-b)
    case "*":
        print("Multuiplication of" , a*b)
    case "/":
        print("Division of" , a/b)
    case _:
        print("invalid input")  


a = int(input("enter first number"))
b = int(input("enter second number"))
operator = input("enter operator: + , - , *, / ")

match operator:
    case "+":
        print("Addition of ", a+b)
    case "-":
        print("subtraction of", a-b)
    case "*":
        print("multiplication of", a*b)
    case "/":
        print("division of", a/b)
    case _:
        print("invalid input")    


#Vowel or Consonant 
ch = "a"
match ch:
    case "a"|"e"|"i"|"o"|"u" :
        print("this is a vowel")
    case _:
        print("consonant")    

# number to words 
num = 6
match num:
    case 1:
        print("one")        
    case 2:
        print("two")
    case 3:
        print("three")
    case 4:
        print("four")
    case 5:
        print("five")
    case 6:
        print("six")
    case _:
        print("invalid number")  

# Traffic Light
light = "red"
match light:
    case "red":
        print("STOP...!")
    case "yellow":
        print("Wait...!")
    case "green":
        print("Go...!")                        
    case _:
        print("Invalid light")

# Number of days in a month
month = int(input("enter a month"))
match month :
    case 1|3|5|7|8|10|12:
        print("31 days")
    case 2:
        print("28 days")
    case 4|6|9|11:
        print("30 days")
    case _:
        print("invalid month")                
