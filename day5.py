# ##command line variables
# import sys

# def add(a,b):
#     c = a+b
#     return c

# def sub(a,b):
#     c = a-b
#     return c

# def mul(a,b):
#     c = a*b
#     return c

# def div(a,b):
#     c = a/b
#     return c


# a = int(sys.argv[1])
# operation = sys.argv[2]
# b = int(sys.argv[3])

# if operation == "add":
#     output = add(a,b)
#     print(output)

# if operation == "sub":
#     output = sub(a,b)
#     print(output)

# if operation == "mul":
#     output = mul(a,b)
#     print(output)

# if operation == "div":
#     output = div(a,b)
#     print(output)


##ENVIRONMENT VARIABLES
# to make env variables we can make it in terminal using command
# export envirnment_variable_name = value_of_env_var



#remember no spaces while creating an env variable
import os

print(os.getenv("aws_key"))
