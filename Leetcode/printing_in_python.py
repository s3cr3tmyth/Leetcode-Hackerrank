name = "Omkar"

age = 26

# %-formatting

print("My name is %s. My age is %s" % (name, age))


# Use str.format()

print("My name is {}. My age is {}".format(name, age))

print("My name is {0}. My age is {1}".format(name, age))

print("My name is {1}. My age is {0}".format(name, age))

# using values from dictionaries

# person = {'name': 'Omkar', 'age': 26}

# print("My name is {name}. My age is {age}".format(**person))



### using f-strings

print(f"My name is {name}. My age is {age}")
