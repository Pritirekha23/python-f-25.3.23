

number=int(input("Enter a number:"))
input_number=number
output_number=0
while number>0:
    remainder=number%10
    output_number=(output_number*10)+remainder
    number=number//10
if input_number==output_number:
    print('The number is palindrome number')
else:
    print('The number is not a palindrome number')


