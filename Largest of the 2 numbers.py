a = input("enter 1st num:")
b = input("enter 2nd num:")
if a >= b:
    if a == b:
        print("both are equal")
    else:
        print("1st number "+str(a)+" is the largest")
else:
    print("2nd number "+str(b)+" is the largest")