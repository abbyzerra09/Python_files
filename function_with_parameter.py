
# (Positional parameters)
# ----

# def greet(name, greeting):

#     print(f"{greeting}, {name}!")

# greet("Rohit", "Hii there")  --> Positional parameters




# (Default parameters)
# ----

# def greet(name, greeting="Hello"):
#     print(f"{greeting}, {name}!")

# # greet("rohit")
# greet("rohit", "Hii")
# greet("rohit", "Howdy")

# (greeting is a default parameter set to "Hello". If no greeting is provided during the function call, it defaults to "Hello")



# (keyword parameters)

# def greet(name, greeting):
#     print(f"{greeting}, {name}!")

# greet(greeting="Hola", name="Rohit")



# Arbitrary Number of arguments
# def sum_values(*args):
#     total = sum(args)
#     print(total)

# sum_values(1, 2, 3, 4, 5)