#TASK-1: Calculate length of string without using inbuilt function
name = "Monika"
index = 0
for letter in name:
    index = index + 1
print("the length of string is : " + str(index))
#-----------------------------

# Reverse a string, a very nice tricky way to do so
def reverse(s):
    str = ""
    for i in s:
        str =  i + str
        print(str)
    return str

s = "arun"
print("The reversed string(using loops) is : ", end="")
print(reverse(s))
print(s[::-1])    #easier and faster way to reverse a string
#-----------------------------
