#if condition
a=int(input("Enter your age: "))
if(a>18):
    print("adult")

elif(a==18):
    print("loading")

else:
    print("child")

#nested loops

mark=int(input("Enter the mark"))  
if(mark>=80):
    print("A+")

elif(mark>=70 and mark<80):
    if(mark<=74):
        print("B+")
    elif(mark>=75):
        print("A")

else:
    print("F")



