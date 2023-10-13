def details(*name):
    print(name)
       
details('Sai','Amit')  # form -> Tuple | Reson -> immutable | Iteration -> Possible

def fullname(*fname):
    for i in fname:
        print(i)
        
fullname('My_firstname','My_lastname','My_Middlename')

