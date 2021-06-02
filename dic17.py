my_dict = {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20
    }
s=[]
for i in my_dict.values():
    s.append(i)
s=[50, 58, 56, 40, 100, 20]
i=0
l=len(s)
a1=[]
c=0
while i<l:
    j=0
    while j<l:
        if s[j]>s[i]:
            if s[j] not in a1:
                a1.append(s[j])
        j+=1
    break
    i+=1
print(a1)
