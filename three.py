num1 = 2
num2 = 3
num3 = 12
num1 = int(input("Input1: "))
num2 = int(input("Input2: "))
num3 = int(input("Input3: "))
if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number between",num1,",",num2,"and",num3,"is",largest)
