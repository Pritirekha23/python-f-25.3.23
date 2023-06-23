# def prime(num):
#     if num<=1:
#         return False
  
#     for i in range(2,int(num**0.5)+1):
#         if num%i==0:
#             return False
#     return True

# num=int(input("Enter a number::"))
# if prime(num):
#     print(f'{num} is a prime number')
# else:
#     print(f'{num} is not a prime numebr'
# num=int(input("Enter a number::"))

# 
  
# if num>1:
#     for i in range(2,int(num/2)+1):
#         if num%i==0:
#             print(f'{num} is not a prime number')
#             break
        
        
#     else:
#          print(f'{num} is a prime number')
# else:
#     print(f'{num} is not a prime number')



# m3

# number=int(input("ENter a umber:"))

# for p in range(2,number):
#     if number%p==0:
#         print("not a prime number")
#         break
# else:
#     print('prime number')




'''m4'''


# To take input from the user
'''
num = int(input("Enter a number: "))

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
          # print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print(num,"is not a prime number")

'''
# print(int(11**0.5))

def prime(num):
    if num<=1:
        return False
  
    for i in range(2,(num//2)+1):
        if num%i==0:
            return False
    return True

num=int(input("Enter a number::"))
if prime(num):
    print(f'{num} is a prime number')
else:
    print(f'{num} is not a prime numebr')
