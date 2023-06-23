# swappingof two number without using temp variable
# num1=int(input("Enter num1:"))
# num2=int(input("Enter num2:"))
# num1,num2=num2,num1
# print(f'num1 is {num1}')
# print(f'num2 is {num2}')

#swappingof two number  using temp variable
num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))

temp=num1
num1=num2
num2=temp
print(f'num1 is {num1}')
print(f'num2 is {num2}')