# types and Ids
a = input("What is your name: ")

print(a)
print(type(a))  # prints the type of object a
print(id(a))  # prints the id of 6

# +
firstName = input("Enter the first name: ")
lastName = input("Enter the last name: ")

name = firstName + lastName  # + adds the two strings
print(name)

# + with print, seperated values
print("Hello" + "World")  # combines the two, NO SPACE
print("Hello", "World")  # combines the two with space because of ,
print("Hello", "World", sep="....")  # sep = puts whatever's between then

# single, double, triple quotes
print('Hello "My" World')  # puts it in quotations
print("Hello 'My' World")  # puts it in ''
print(
    """This is a paragraph with breaks.
it just broke."""
)

# mutable
value = 27
valueTwo = 22
value = (
    27 - 12
)  # the id changes here because the "value" gets a different value alltogether

print(id(value))
print(id(27))  # the id is the same as the original because value is the same as 27.
