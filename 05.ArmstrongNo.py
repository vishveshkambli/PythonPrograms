num = '153'
sum = 0
for i in num:
    sum=sum+int(i)**len(num)
print(sum)
if int(num) == sum:
    print('Armstrong')
else:
    print('Not Armstrong')
