# def star(num):
#     print('o' *num)
#     if num==1:
#         return
        
#     star(num-1)
    
# star(5)

# ooooo
# oooo
# ooo
# oo
# o

# def star(num):
#     print('o' *num)
#     if num==5:
#         return
        
#     star(num+1)
# star(1)

# def star(num):
#     for i in range(1, num + 1):
#         print('o' * i)

# star(5)

# o
# oo
# ooo
# oooo
# ooooo


# def print_diamond_recursive(size, current_row=0):
#     if current_row < size:
#         print(" " * (size - current_row - 1) + "*" * (2 * current_row + 1))
#         print_diamond_recursive(size, current_row + 1)
#         print(" " * (size - current_row - 1) + "*" * (2 * current_row + 1))
#     else:
#         return

# size = int(input("Enter the size of the diamond: "))
# print_diamond_recursive(size)

#     *
#    ***
#   *****
#  *******
# *********
# *********
#  *******
#   *****
#    ***
#     *

# start=1
# stop=22
# step=2
# for i in range(start,stop,step):
#     print(f"{'o'*(stop//2-abs(i-stop//2)):^{2*stop}}")

#                      o
#                     ooo
#                    ooooo
#                   ooooooo
#                  ooooooooo
#                 ooooooooooo
#                  ooooooooo
#                   ooooooo
#                    ooooo
#                     ooo
#                      o

# start=1
# stop=22
# step=2
# for i in range(start,stop,step):
#     print(f"{'o'*(stop//2-abs(i-stop//2)):{2*stop}}")

# o
# ooo
# ooooo
# ooooooo
# ooooooooo
# ooooooooooo
# ooooooooo
# ooooooo
# ooooo
# ooo
# o