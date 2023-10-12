# Unpacking is only is when we perform our operations on pairss

dict={'a':1,'b':2,'c':3,'d':4}
ndict = {x:y for x,y in dict.items()}
print(ndict)

lst=[(1,2),(3,4),(5,6),(7,8)]
for (i,j) in lst:
    print(i)
    print(j)
    
lst1 = [(1,2,3),(3,4,5),(5,6,7),(7,8,9)]
for (i,j,k) in lst1:
    print(i)
    print(j)
    print(k)
    