def find_maximum(a,b):
    if(a>b):
        print(a,"is greater than",b)
    elif(a<b):
        print(a," is less than ",b)
    else:
        print("both and are equal")

a=int(input("Enter a number:"))
b=int(input("Enter b number:"))
find_maximum(a,b) #function called

def loop(a):
    for i in a:
        print(i)

p=input("Enter a name:")
loop(p) #function called
