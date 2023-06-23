

# list=[1,2,3,4,5]
# sum=0
# for i in range(0,len(list)):
#     sum=sum+list[i]
# print(sum)

# using sum
list2=[1,2,3,4,5]
sums=sum(list2)
print(sums)

# using add
from operator import*
list3=[1,2,3]
total=0
for i in list3:
    total=add(i,total)

print(total)