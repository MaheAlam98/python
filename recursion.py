# factorial
def factorial(n):
    if(n==1 or n==0):
        return 1
    else:
        return n * factorial(n-1)

print(factorial(20))

# fibonacci
def fibonacci(n):
    if(n==0):
        return 0
      
    if(n==1):
        return 1
        
    else:

       print(fibonacci(n-1) + fibonacci(n-2)) 
       return fibonacci(n-1) + fibonacci(n-2)
    

print(fibonacci(20))