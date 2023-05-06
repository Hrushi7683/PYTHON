# Iterables using Dictonary 

#Iterable: string , set , dict , tuple , list 
#iterte:one by one checks each value

#Int is not iterable 

user = {'Sush' : 8 , 'omkar' : 10 , 'pratham' : 39 , 'hrushikesh' : 67 }
#Sush is key and 8 is a value
for item in user :
    print(item)

for item in user.items():
    print(item)

for key , value in user.items():
    print(key , value)    

for item in user.values():
    print(item)

for item in user.keys():
    print(item)

    

#output

#Sush
#omkar
##pratham
#hrushikesh
#
#
#('Sush', 8)
#('omkar', 10)
#('pratham', 39)
#('hrushikesh', 67)
#
#
#Sush 8
#omkar 10
#pratham 39
#hrushikesh 67
#
#
#8
#10
#39
#67
#
#
#Sush
#omkar
#pratham
#hrushikesh
#

