def factorial(no):
    if no == 0:
        return 1
    else:
        return no*factorial(no-1)
print("factorial o0f a number is :",factorial(8)) 
