mystring = "This is my string"
print(mystring)
print(type(mystring))
print(str(mystring)  + "is of data type of" + str(type(mystring)))

firststring = "shiva"
secondstring = "prasad"
thirdstring = firststring + secondstring
print(thirdstring)

name = input("Enter your name")
print(name)

string1 = 'SHIVAPRASAD'
for letters in string1:
    print(letters)
    
color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")
print("{}, you like a {} {}!".format(name,color,animal))
