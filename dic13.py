dic={"first":1,
"second":2,
     "third": 1, 
     "four": 5,
     "five":5, 
     "six":9,
     "seven":7
}
l=[]
for val in dic.values():
    if val in l :
        continue
    else:
        l.append(val)
print(l)



