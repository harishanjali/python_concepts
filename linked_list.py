# x = [1,2,2,1]
# org = str(x).join('')
# reverse = str(x[::-1])
# print(reverse)

def reverse(st):
    if len(st)==0:
        return st
    return st[len(st)-1] + reverse(st[:len(st)-1])

st = 'harish'
res = reverse(st)
print(res)
