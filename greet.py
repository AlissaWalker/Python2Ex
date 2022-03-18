def greet(name): # functions begin with def; Function is like a method in java
    #name = input("Enter your name:")
    print("Salutations " + name)

#greet(" ")

# whats in the parenthesis is the argument (parameter in java); this has no argument
def name_input():
    name = input("Enter your name:")
    return name # need () for return if im learning more than 1 thing



name_from_user = name_input() # return staements help = a return statement  <--better way
greet(name_from_user)

# greet(name_input())  #this is another way to get an answer # entire arguments show up as functions
