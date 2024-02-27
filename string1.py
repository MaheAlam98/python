print("tuhin")
print("tuhin")
name="tuhin"

# store multiple line string using """"""
st="""GitHub, Inc. is a developer platform that allows developers to create, store, manage and share their code. It uses Git software, providing the distributed version control of Git plus access control, bug tracking, software feature requests, task management, continuous integration, and wikis for every project."""
print(st)
# print string using index
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
# print(name[5])
# print string using loop
for i in st:
    print(i)



# string length
x=len(st)
print(x)

#print string using start and end index 
print(name[0:3])   #print index 0 to index 2 not include index 3
print(name[3:])    #print start index 3 to length of string
print(name[:4])    # print start index 0 to index 4
print(name[-1:-3]) # print start len(string)-1 to len(string)-3
print(name[-4:-1])  # print start len(string)-4 to len(string)-1
print(name[:])     # print start index 0 to length of string

# string methods
sub="Bangladesh!!!*"
print(sub.upper()) # convert full string in upper case
print(sub.lower()) #convert full string  in lower case
print(sub.rstrip("!")) # remove '!' if it is in the last of the string
print(sub.replace("desh","deshes")) #replace
print(sub.split(" ")) #convert string in a list
print(sub.capitalize()) #first character is capital and all other characters are lowercase
print(sub.center(87)) #give 87 - len(sub) space before string
print(sub.endswith("sh")) #it gives the result if our string is end in 'sh' then it gives true otherwise it give false
print(sub.endswith("ng",0,4)) #it gives the result if our new string  length between 0 and 4 is end in 'ng' then it gives true otherwise it give false
print(sub.startswith("ba")) ##it gives the result if our new string  start in 'ng' then it gives true otherwise it give false

a="2 ta bisoy mona rakte hobE\n"
a1="    "

print(a.find("oy")) #give the index number of 'oy' if in it exist in the string if not exist return -1
print(a.index("oy")) #give the index number of 'oy' if it exist in the string if not exist return error occur
print(a.islower()) #if all character in a string in lower case return true other wise return false
print(a.isprintable()) #if all character in a string in printable(means all character in input string same as output (** \n cannot show in output **)) return true outher wise return false
print(a1.isspace()) #if the string has no character only space
print(a.isspace())
print(a.istitle())
print(a.swapcase()) #convert all upper case to lower case and lower case to upper case
print(a.title()) #convert first character in all word in a string  uppercase 


