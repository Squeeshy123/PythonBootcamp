# 1.1: Printing something
print("Hello World!") # Prints any object given to it provided that it can be converted to a string

# This requests the user for input, but I'm using it to pace the examples
input("You can put anything in the print function")

print(256)

class SomeObject:
    some_data = 0

object = SomeObject()

print(object)


input("You can also change certain parts of the print function ")

# you can also add something to the end of a print statement
#                                                            vv this just means make a new line
print(12345, end=" this is what is at the end of the print\n")
print("fox", end="es ")

# See what happens without the \n                        vvvv makes 2 new lines
input("this is what it's like without a \\n Weird right? \n\n but now I'm on this line! ")
# The backslash "\" will let you specify certain commands in RegEx, but thats fancy shennanigans.
# All you need to know for now is that \n makes a new line.

print("")


