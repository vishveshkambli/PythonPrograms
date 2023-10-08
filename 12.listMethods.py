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