# def sum(x):
#     return x*5  #use normal function

sum =lambda x,y: x+x  #use lambda function
print(sum(5,5))

cube =lambda x:x*x*x
#function pass another function as parameter

def apply(fx,y):
    return 8+fx(y)

print(apply(lambda x:x*x*x,5))