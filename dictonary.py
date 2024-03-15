dic={1:"tuhin", 2:"kamal", 3:"Jamal"}
print(dic)
print(dic[1]) # if 1 not exist in dictonary then error ossur
print(dic.get(1)) #if 1 not exist it return non 
print(dic.keys())
print(dic.values())

for i in dic.keys():
    print(dic[i])

print(dic.items()) # print keys, values 
for key,value in dic.items():
    print(key,value)

# dictionary method
s1={"name1":"tuhin","reg1":1030,"roll1":3346}
s2={"name2":"jamal","reg2":1090,"roll2":3356}
s1.update(s2)
print(s1)
s2.clear()
s1.pop("name1")
print(s1)

    