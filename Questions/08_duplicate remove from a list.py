# list1=[1,2,3,4,5,2,3,4,10,8,5]
# num=list(set(list1))
# print(num)


list2=[1,2,3,4,5,2,3,4,8,5]
print('inputlist is:',list2)

result=[]
for i in list2:
    if i not in result:
       result.append(i)
print('now the list become:',result)