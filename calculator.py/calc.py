def addition(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  if y == 0:
   return "Cannot divide by zero"
  return x / y

print("Select operation:")
print("1. addition")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")


choice = input("Enter choice (1/2/3/4): ")
N1 = float(input("Enter first number: "))
N2 = float(input("Enter second number: "))


if choice == '1':
  result = addition(N1, N2)
elif choice == '2':
  result = subtract(N1, N2)
elif choice == '3':
  result = multiply(N1, N2)
elif choice == '4':
  result = divide(N1, N2)
else:
  result = "Invalid input"

if result == "Invalid input" or result == "Cannot divide by zero":
  print(result)
else:
  print("Result:", result)