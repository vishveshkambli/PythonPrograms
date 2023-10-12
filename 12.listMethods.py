lst=[1,2]  # list : mutable, ordered, indexible, allows duplicate values
#1
lst.append(3)
print(lst,"adds value at the last index")
#2
lst.pop(0)
print(lst,"removes value from the mentioned index")
#3
lst.insert(0,7)
print(lst,"insert's 7 at 0'th index")
#4
newlst=lst.copy()
print(newlst,"This is a copy of list, changes made will differ from orignal list")
#5
lst.reverse()
print(lst)
#6
lst.remove(7)
print(lst)
#7
lst.sort()
print(lst)
#8
print(lst.index(3))
#9
print(lst.count(3))
#10
lst1=[1,2,3,4]
lst.extend(lst1)
print(lst)
#11
lst.clear()
print(lst)
