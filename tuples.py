tup=(1,2,3,4,4,5,True,"tuhin") # Create tuple using first bracket and create list using 3rd bracket
print(type(tup),tup) # tuple element cannot be change
print(tup[1])
print(tup[2])
print(tup[3])
print(tup[4])
print(tup[5])
print(tup[-3]) #same as list
print(tup[1:5]) #slicing same as list
if  3421 in tup:
  print("Yes 342 is present in this tuple")


#tuples method
tup1=(1,2,5,3,4,5,True) #tuple element cannot be change if you want to change the tuble element then first convert in ina list then the list change than the list element is convert in  tuple
li1=list(tup1) #tuple convert in list
li1.append("tuhin") #add element in list
li1.pop(3) #remove element from list
print(li1)
tup=tuple(li1) # convert list into tuple
print(tup)
print(tup.index(5)) #find index of 5
print(tup.index(5,2,4)) #find index of 5 in a tuple range 2-4
print(tup.count(5))


