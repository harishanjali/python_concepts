import copy

x = [10,20,'vcube','python',True]

#list functions
x.append(30)#adds element last to the list
y = [[1,2],[3,4],5]

z = y#assignment normal copy address remains same
m = y.copy()#shallow copy, address of lists changes, but not elements addresses
print(id(y))
print(id(z))
print(id(m))

x = [1,2,3,4]
s = [5,6,7,8]
print(x)
print('count function',x.count(1))#count function
res = x.extend(s)
print('extends',res)
res = x.index(3)#gets index of the element
print('index of 3 is ',res)
x.insert(0,10)#insert element at specified index
x.pop()#we can remove element by index or remove last element
x.remove(4)
x.reverse()
print(s)

f = [1,2,3,4,5,6]
f.sort(reverse=True)
print(f)

