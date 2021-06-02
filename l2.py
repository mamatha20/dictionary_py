dict = {'gfg' : [5, 6, 7, 8],'is' : [10, 11, 7, 5],'best' : [6, 12, 10, 8],'for' : [1, 2, 5]}
a=0
i=0
while i<len(dict):
    j=0
    while j<len(dict):
        if dict[i]<dict[j]:
            a=dict[j]
            dict[j]=dict[i]
            dict[i]=a
        j=j+1
    i=i+1
print(dict)