list1=['one','two','three','four','five']
list2=[1,2,3,4,5,]
dic={}
i=0
while i<len(list1):
    dic[list1[i]]=list2[i]
    i=i+1
print(dic)
# dic={
#     'one':1,
#     'two':2,
#     'three':3,
#     'four':4
# } 
# print(dic)

# Output :-

# {“one”:1,”two”:2,”three”:3,”four”:4,”five”:5}
