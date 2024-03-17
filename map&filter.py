# map is use to pass all element in a list and get output
cube =lambda x: x*x*x

l=[1,2,3,4,5,6]
print(list(map(cube,l)))

#filter functions is use to filter all elements base on a condition
def filter_function(a):
    return a>4
print(list(filter(filter_function,l)))