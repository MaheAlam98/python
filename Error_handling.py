x=input("Enter the :")
try:
    for i in range(1,11):
        print(f"{i} x {x} = {i*int(x)}")

except Exception as e:
    print(e)
print("Code word")

# final keyword that always execute

#create a custom Error
a=int(input("Enter a value in range 0 to 9:"))
if(a<0 or a>9):
    raise ValueError("value must be between 0 and 9")
b=input("Enter a string:")
if(b!="quit"):
    raise ValueError("Invalid string")
            
