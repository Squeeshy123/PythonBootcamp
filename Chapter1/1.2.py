# 1.2: Declaring variables and accepting input

# Variables work just how they do in math.
# you assign value with the '=' sign, then 
funny_number = 69420
print("Funny number:", funny_number)

# You can do math in python too!
math_number = 100 * 256
print("What is 100 * 256?", math_number)

# You can even accept input with variables
user_input = input("What do you want to say? ")
print("You:", user_input)

# but watch out!
# print("You: ", user_input - 5) # This will give you an error! 
# Because the input function returns a string so
# it thinks you are trying to subtract a number from a word!
# We will fix this in 1.3
evaluated_input = eval(input("Type some equation or something: "))
print(evaluated_input)
