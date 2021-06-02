# 1.1: Printing something
print("Hello World!") # Prints any object given to it provided that it can be converted to a string

# This requests the user for input, but I'm using it to pace the examples
input("You can put anything in the print function")

print(256)

class SomeObject:
    some_data = 0

object = SomeObject()

print(object)


#You can even change certain parts of the print function
print(12345, end=" this is what is at the end of the print\n")

#or even like this
print("The", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog", sep="|")



