list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16]
one_list=list1+list2
new_list=[]
counter=0
while counter<len(one_list):
    if  one_list[counter] not in new_list:
        new_list.append(one_list[counter])
    counter+=1
new_list.sort()
print new_list