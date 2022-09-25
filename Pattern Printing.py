n = int(input("Enter a number :\n"))
for i in range(n):
    for j in range(n):
        print((n-j)**(i+1), end=" ")
    print()
