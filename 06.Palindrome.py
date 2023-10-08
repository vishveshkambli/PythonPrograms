word = 'madam'
temp = ''
for i in range(len(word)-1,-1,-1):
    temp=temp+word[i]
    print(temp)
if word == temp:
    print('palindrome')
else:
    print('Not palindrome')