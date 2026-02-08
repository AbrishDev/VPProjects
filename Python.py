print("Hello World!")

if 5 > 2:
    print("Five is greater than two")


name = "Meku"
age = 20
height = 1.75
is_student = True

print("Name:", name , type(name))
print("Age:", age, type(age))
print("Height:", height, type(height))
print("Is Student:", is_student, type(is_student))

a = 10
b = 3

# Arithmetic Operators
print(a + b)   # addition
print(a - b)   # subtraction
print(a * b)   # multiplication
print(a / b)   # division
print(a % b)   # remainder
print(a ** b)  # exponentiation
print(a // b)  # floor division

# Comparison Operators
print(a > b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

# Logical Operators
x = True
y = False

print(x and y)
print(x or y)
print(not x)

# Input and Output
name = input("Enter your name: ")
print("Hello", name)
age = int(input("Enter your age: "))
print("You are", age, "years old.")

# Conditional Statements

if age >= 18:
    print("You are an adult")
elif age == 17:
    print("Almost adult")
else:
    print("You are a minor")


# Loops
for i in range(5):
    print(i)

count = 0
while count < 5:
    print(count)
    count += 1

