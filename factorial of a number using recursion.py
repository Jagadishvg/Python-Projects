def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)


num = int(input("Enter a number:"))
factorial = fact(num)
print("The factorial of", num, "is", factorial)




