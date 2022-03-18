def exponentiate(base, exponent):
    ''' # doc string to help people know what the function is
    Returns base raised to exoponent
    :param base: int exponent
    :param exponent: int
    :return: int
    '''

    return (base ** exponent)


def raise_to_fourth_power(base):
    '''Calls the exponentiate function to raise the given paremeter to the 4th power.
    :param base: int
    :return: int
    '''

    return exponentiate(base,4)  # calls base function and reaises it to the 4th power

#lamba makes a variable a function
square = lambda x: x * x
cube = lambda x: x * x * x

print(square(2))
print(cube(2)) # turns x into 2 because x is in lambda
print(raise_to_fourth_power(2))