# 6.Reverse a string ? 
a = 'python'
# print(a[::-1])

# 7.Count vowels?
a = 'python'
count = 0
for ch in a:
    if ch in 'aeiouAEIOU':
        count+=1
# print(count)

# 8.Capitalize First Letter of Words ? 
a = 'python'
b = a.capitalize()
# print(b)
# 9.Check palindrome?
a = 'madam'
if a[::-1] == a:
    pass
    # print('palindrome')
else:
    # print('not a palindrome')
    pass
# 10.Count Occurrences of Substring?

# 1.Write a Python program to check whether a given string is empty or not?
a = ''
# print(a=='')
# 2.Write a Python program to remove all vowels from a given string?
a = 'python'
res=''
for ch in a:
    if ch not in 'aeiouAEIOU':
        res+=ch
# print(res)
# 3.Write a Python program to count the number of words in a given string?
a = 'python is a programming language'
b = a.split(' ')
# print(len(b))
# 4.Write a Python program to check whether a given string is a palindrome (ignoring spaces)?
# done
# 5.Write a Python program to encode a string by replacing each letter with the next letter?
a = 'python'
res = ''
for ch in a:
    res += chr(ord(ch)+1)
# print(res)
# 6.Write a Python program to find the longest word in a given sentence?
a = 'python is a programming language'
b = a.split(' ')
highest_length = b[0]
for word in b:
    if len(word) > len(highest_length):
        highest_length = word
# print(highest_length)

# 7.Write a Python program to check whether two given strings are anagrams?
a = 'silent'
b = 'listen'
#one way
# if len(set(a) ^ set(b)) == 0:
#     print('anagram')
# else:
#     print('not an anagram')
#second way
if len(a)>len(b):
    test = a
    test_1 = b
else:
    test = b
    test_1 = a
for ch in test:
    if ch not in test_1:
        print('Not angram')
        break
else:
    print('anagram')
# 8.Write a Python program to count the number of consonants in a given string?