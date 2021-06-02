my_dict = {
    'a':50, 
    'b':58,
    'c': 56,
    'd':40,
    'e':100, 
    'f':20
    } 
s=[]
s1=[]
for i in my_dict.values():
    s.append(i)
for j in my_dict.keys():
    s1.append(j)
var1=0
var2=0
n=0
l=len(s)
s2=[]
while n<l:
    n1=0
    while n1<l:
        if s[n1]>s[n]:
            if s1[n1] not in s2:
                s2.append(s1[n1])
        n1+=1
    break
    n+=1
print(s2)