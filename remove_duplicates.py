def removeduplicates(st):
    
    output = ''
    for char in st:
        if char not in output:
            output+=char
    return output

st = '22aaabbcc11122'
res = removeduplicates(st)
print(res)