n='MISSISSIPPI'
list1=list(n)
print(list1)
list2=[]
dict1={}
for i in range(len(list1)):
    if list1[i] not in list2:
        list2.append(list1[i])
print(list2)
for i in range(len(list2)):
    count=0
    for j in range(len(list1)):
        if list2[i]==list1[j]:
            count+=1
    print(list2[i], count)
    dict1[list2[i]]=count
print(dict1)