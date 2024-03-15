a={1,'r',"tuhin",2,1}
print(a);
b=set() #empty set
for i in a:
    print(i)

# set method
#union operation
s1={1,2,3,4,5}
s2={1,4,2,7,8,9}
print(s1.union(s2))
print(s1.intersection(s2))
#s1.update(s2) #s2 ar all value s1 ar modda chole asbe and s1 change hoya jabe
s1.intersection_update(s2) #s1 and s2 intersection hobe and ta s1 ar modda update hobe

print(s1)
# symmetric difference:A U B - A n B means All item - common item
s3=s1.symmetric_difference(s2) 
print(s3)
 #difference :A -B
s4=s2.difference(s1) #s2 - s1 
print(s4)

#disjoin set:if there are no common item in set a and set b then it call disjoin set (a n b=null)
print(s1.isdisjoint(s2)) #it return true and false

# subset and supper set : if all item of b in exist in set a then a is the supper set of b and b is the sub set of a

print(s1.issuperset(s2)) #it return true or false
print(s2.issubset(s1)) #it return true or false

# remove item from the set
s1.remove(1) #if 1 is not have in s1 then it occur error

print(s1)
s1.discard(3) #if 3 is not have in s1 then it cannot occur  error

# delete set
# del s1 #s1 delete
#clear delete all value in the set
s1.clear() #delete all value in the set


 
