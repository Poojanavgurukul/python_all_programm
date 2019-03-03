sentence = "NavGurukul is an alternative to higher education reducing the barriers of current formal education system"
counter=0
word=""
new_list=[]
while counter<len(sentence):
    if sentence[counter]!=" ":
        word+=sentence[counter]
    elif sentence[counter]==" ":
        new_list.append(word)
        word=""
    counter+=1
if word!= " ":
    new_list.append(word)
print new_list