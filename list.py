marks=[1,2,3,4.5,5,6,7.5,8,9,10,'tuhin',True]
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
print(marks[5])
print(marks[6])
print(marks[7])
print(marks[8])
print(marks[9])
print(marks[11])
print(marks[-9]) #-9 means len(marks)-9
print(marks[-5])
print(marks[0:])
print(marks[0:len(marks)])
print(marks[0:len(marks):2])

if 10 in marks:
    print("Yes")

# list comprehensions
    
lst=[i*4 for i in range(5)] # i ar value 1-5 ar modda and each i get value i*4 value in the list
print(lst)
lst=[i*3 for i in range(5) if i%2==0]
print(lst)


# list methods

l1=[4,3,2,4]
print(l1)
l1.append(1) 
print(l1)
# l1.sort(reverse=True)
# print(l1)
# l1.reverse() 
# print(l1) 
print(l1.index(2))
print(l1.count(4))
m=l1 #ai babe copy korla orginal list  pass korbe and kisu change hoila orginal list change hobe
m1=l1.copy() # ai copy corla orginal list change hobe na
print(m1)
l1.insert(3,100) # 3 number index ar value 100 insert korbe
m2=[90,100,30]
l1.extend(m2) # l1 list a append korce m2 means l1 list ar last a m2 ar sob element add hya jibo
print(l1)
k=l1+m2 # create another list k and append the value l1 and m2
print (k)


