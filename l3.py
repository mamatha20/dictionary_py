#Python program to find the sum of all items in a dictionary
m={'a': 100, 'b':200, 'c':300}
sum=0
for i in m:
    sum=sum+m[i]
print(sum)
