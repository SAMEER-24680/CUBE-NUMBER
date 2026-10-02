def factorial(x):
    '''THIS IS A RECURSIVE FUNCTION TO FIND OUT A FACTORIAL OF AN INTEGER'''
    if x == 0 or x == 1:
        return 1
    else:
        return x*factorial(x - 1)
print(factorial.__doc__)
print("THE FACTORIAL OF 0 : ", factorial(0))
print("THE FACTORIAL OF 1 : ", factorial(1))
print("THE FACTORIAL OF 2 : ", factorial(2))
print("THE FACTORIAL OF 5 : ", factorial(5))
print("THE FACTORIAL OF 10 : ", factorial(10))