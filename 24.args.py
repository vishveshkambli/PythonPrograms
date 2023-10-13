def details(*name):
    print(name)
       
details('Sai','Amit')  # form -> Tuple | Reson -> immutable | Iteration -> Possible

def fullname(*fname):
    for i in fname:
        print(i)
        
fullname('My_firstname','My_lastname','My_Middlename')

def numbers(*num): # *args can be use when you don't know how many args will be passed
    sum=0
    for i in num:
        sum=sum+i
        print(sum)
        
numbers(1,2,3,4,5,6,7,8,9)
