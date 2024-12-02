#Booleans problem 1
number = int(input("Enter an integer: "))
if number % 2 == 0:
        print("Even")
else:
        print("Odd")

#Comparison Operators problem 2
grade = int(input("Enter a grade: "))

if grade <= 50:
     print("Fail")
else:
     print("Pass")

#Decision Making problem 2
age = int(input("How old are you?: "))
city_status = input("Are you a citizen? (yes/no): ")

if age >= 18 and city_status == "yes":
    print("Eligible to vote")
else:
    print("Not eligible to vote")

#List Comprehension problem 1
cubes = [x**3 for x in range(1, 11)]
print(cubes)

#Logical Operators problem 1

#Loops problem
count = 20
while count >= 0:
    print(count)
    count -= 1  
#Min/Max problem

#Random problem

#Ranges and Enumerators problem

#Zip problem