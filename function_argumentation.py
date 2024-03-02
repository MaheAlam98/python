# 2 arguments pass and two arguments recieve
def avg(a,b):
    print("Average:",(a+b)/2)
avg(20,30)

def avg(a=20,b=30):
    print("Average:",(a+b)/2)
avg(2,3) #here this value is use as the a and b values

def avg(a=20,b=30):
    print("Average:",(a+b)/2)

avg()
