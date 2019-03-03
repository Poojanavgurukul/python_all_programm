def common_number(list1,list2):
    common_number_list=[]
    counter=0
    while counter<len(list1):
        if list1[counter] in list2:
            common_number_list.append(list1[counter])
        counter+=1
    print common_number_list
common_number([1, 342, 75, 23, 98],[75, 23, 98, 12, 78, 10, 1])