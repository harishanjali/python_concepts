s = 'listen'
t = 'silent'

# if len(set(s) ^ set(t)) == 0:
#     print('anagram')
# else:
#     print('not an anagram')

# a = {1,2}
# b={1,2,3}

# print(a^b)

for char in t:
    if char not in s:
        print('not anagram')
        break
else:
    print('anagram')