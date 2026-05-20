#map
x = [1,2,3,4,5,6]
res = list(map(lambda x:x**2,x))#if you dont convert to list, it will give map object
#print(res)
#filter
res = list(filter(lambda x:x%2==0,x))
# print(res)
from functools import reduce
#reduce
#combine all the avalues and get ony one value

res = reduce(lambda a,b:a+b,x)
print(res)