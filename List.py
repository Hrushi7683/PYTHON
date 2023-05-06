
#list = [1,2,3,4,5,6,7,8,9,10]

#this is a simple list

#Constructors

#list()-->This converts an object into list 

print(list('godavari'))
print(list('1234565789'))
print(list([1,2,3,4,5]))
print(list((1,2,3,4,5)))
print(list({'on':1 , 'off':2}))


#List comprehensions
#used to create a list directly in one line

print([n for n in range(5)])


man='himmat_wala'
print([n*2 for n in man])


print([n+3 for n in range(0,50,3)])


#Literal syntax of list

list1=[2,34,5,6]
print(list)

om='ganesh'
shree='himmat'
man='daatr'

list1=[om,shree,man]
print(list1)



#Methods of adding element

#INSERT -->insert item at given position

#syntax= list.insert(index , object)

list2=[12,24,36,48,60]

list2.insert(3,00)


#APPEND-->It adds the element at the end of list

list3=['a','b' , 'c' , 'd' , 'e']
list3.append('z')


#extend-->extends the list by appending all item given in iterable
#syntax-->list.extend(iterable)
#here iterable can be another list


list4=[2,3,4,5,6,7]
list4.extend([8,9,9,8,9,8,9])


#Methods of deleting element from list

#remove-->removes the first element from list as it founds , if not found then error is raised
#list.remove(object)


l=[1,2,3]
l.remove(2)

#pop --> list.pop([index])
#elemnt will be poped out from given index

li=[1,4,7,0]
li.pop([3])

#by deafult it will take last index [o(1)]


#Information

#list.index(item)-->will return the value from list as you pass the valid index

#list.count(item)-->return the count of value you passed from list

#Modifying




