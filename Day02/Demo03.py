
print("Correct statement")

# print("First Statement"
# above code will cause compiler error -- no byte code created -- interpreter not called
# SyntaxError: '(' was never closed

printf("Second Statement")
# above code will cause runtime error -- compiler found syntax correct
# here compiler create byte code and PVM/interpreter will try to execute line by line
# at runtime, it get this error -- printf() is not available function
# NameError: name 'printf' is not defined.

