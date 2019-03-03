marks = [[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]]
counter=0
while counter<len(marks):
    max=None
    counter2=0
    while counter2<len(marks[counter]):
        if max<marks[counter][counter2]:
            max=marks[counter][counter2]
        counter2+=1
    print max
    counter+=1
