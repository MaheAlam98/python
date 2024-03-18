def greet(fx):
    def mfx(*args, **kwargs):
        print("Good Morning")
        fx(*args, **kwargs)
        print("Thank You for using this function")
    return mfx


def add(a,b):
    print(a+b)
greet(add)(4,5)

# @greet
# def ak():
#     print("Welcome to FEC")
#ak()  

def ak():
    print("Welcome to FEC")
greet(ak)()