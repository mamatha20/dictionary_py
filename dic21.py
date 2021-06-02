a={(1,2):1,(2,3):2}
print(a[1,2])
#1saral output:=1
a={'a':1,'b':2,'c':3}
print(a['a','b'])
#2saral output:=key error
fruit = {}

def addone(index):
    if index in fruit:
        fruit[index] += 1
    else:
        fruit[index] = 1

addone('Apple')
addone('Banana')
addone('apple')
addone('Apple')

print (len(fruit))
print(fruit) 
#3saral output=3,{'Apple':2,'Banana':1,'apple':1}
Student = {}
Age = {}
Details = {}
Student['name'] = "bikki"
Age['student_age'] = 14
Details['Student'] = Student
Details['Age'] = Age

print (len(Details["Student"]))
#4 saral output=1