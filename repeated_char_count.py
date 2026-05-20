def getcharcount(st):
    output = ''
    count = 1
    for i in range(len(st)-1):
        if st[i] == st[i+1]:
            count += 1
        else:
            output += st[i] + str(count)
            count = 1
    else:
        output += st[i+1] + str(count)
    return output

x = 'aaabbacca'
res = getcharcount(x)
print(res)