x=int(input("Enter a number:"))
match x:

    case 1:
        print("one")
    case 2:
        print("two")
    case 3:
        print("three")
    case 4:
        print("four")
    case _ if(x/2==0):
        print("EVEN")
    case _ if(x/2!=0):
        print("odd")
    case _:
        print("unknown")