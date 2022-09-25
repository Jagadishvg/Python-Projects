def sum():
    n = int(input("Enter a number \n"))
    sum1 = 0
    for i in range(n+1):
        sum1 = sum1 + i
    print("The sum of given n numbers is: "+str(sum1))

sum()