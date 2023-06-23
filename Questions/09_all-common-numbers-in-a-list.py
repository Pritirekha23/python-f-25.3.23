#finding the cooomon element from two list
list1=[5,10,15,20,25,30]
list2=[35,40,45,5,15,20]
common_element=list(set(list1) & set(list2))
print(common_element)