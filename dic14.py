dic1=[]
dic2= []
dic={}
i=1
while i<=10:
    s=input("enter the name of student:=")
    m=int(input("enter the marks:="))
    dic1.append(s)
    dic2.append(m)
    i=i+1
j=0
while j<len(dic1):
    dic[dic1[j]]=dic2[j]
    j=j+1
print(dic)
