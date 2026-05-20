# 1.Find the index of the first occurrence and last occurrence of a specific element in a tuple?
a = (1,2,3,4,5,1,5)

def index_last_occurence(ele,tpl):
    index = 0
    for i in range(len(tpl)):
        if ele in tpl[i+1:]:
            index+=1
        else:
            break
    return index
for ele in a:
    if a.count(ele) == 1:
        pass
        #print(ele,a.index(ele),'only once')
    else:
        pass
        #print(ele,index_last_occurence(ele,a))

# 2.Concatenate two tuples?

a = (1,2,3)
b = (4,5,6)
a = a+b
# print(a)
# 3.Count the occurrences of an element in a tuple? 
a = (1,2,3,4,5,6,5,7,8)
# print(a.count(5))

# 4.Check if an element exists in a tuple? 

a = (1,2,3,4)
# print(5 in a)

# 5.Reverse a tuple?  
a = (1,2,3,4)
# print(a[::-1])

# 6.Find the maximum and minimum elements in a tuple? 
a = (1,2,3,4)
# print(max(a))

# 7.Check if all elements in a tuple are the same? 
a = (1,1,1,1)
first_ele = a[0]
for num in a:
    if first_ele != num:
        # print('Not same')
        break
else:
    pass
    # print('All Are same')
# 8.Sort a tuple of numbers in ascending order?
a = (5,6,2,1,4)
# print(sorted(a))
 
# 9.Find the sum of all elements in a tuple?  
a = (1,2,3,4)
# print(sum(a))
# 10.Check if a tuple contains only unique elements?
a = (1,2,3,4,2,2)
for ele in a:
    if a.count(ele)>1:
        # print('NO unique')
        break
else:
    # print('Unique')
    pass

# Good evening Everyone,
# Today's Daily Task for Batch 79:
# 1.Multiply a tuple to repeat its elements? 
a = (1,2,3)
# print(a*2) 
# 2.Unpack a tuple into individual variables? 
a = (1,2,3)
x,y,z = a
# print(x,y,z)
# 3.Convert a tuple of strings into a single string? 
a = ('p','y','t','h','o','n')
# print(''.join(list(a)))
# 4.Merge two tuples into one using the + operator?
a = (1,2,3)
b = (4,5,6)
# print(a+b)
# 5.Find the product of all elements in a tuple of numbers?

a = (1,2,3,4)
a = list(i*i for i in a)
print(a)