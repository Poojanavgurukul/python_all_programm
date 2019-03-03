counter=1
while counter<=100:
    x=counter
    x_didgits=list(str(x))
    count=0
    sum=0
    while count<len(x_didgits):
        sum+=int(x_didgits[count])
        count+=1
    if x%sum==0:
        print x,True
    else:
        print x,False
    counter+=1