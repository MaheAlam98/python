# f=open("book.txt", "r") #file open in read mode
# #f=open("book.txt") #its works same
# test=f.read() #read the file and save it in test
# print(test)
# f.close()
# f=open("book2.txt", "w") #if this file not exist it automatic create a new file

#writing the file
# f=open("book2.txt", "w")
# f.write("Bangladesh play cricket not good in last five years")
f=open("book2.txt", "r") #file open in read mode
test=f.read() #read the file and save it in test
print(test)
f.close() 

# readline use for read line by line
