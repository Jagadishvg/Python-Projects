import random
print("Hi what is your name \n")
name = input()
print("Hello "+ name )
print("Enter a number between 1 to 10 \n")
secretnumber = random.randint(1, 10)
try:
    for guesstaken in range(1,7):
        guess = int(input("enter your number \n"))
        if guess>secretnumber:
            print("no its too high")
        elif guess<secretnumber:
            print("no its too low")
        else:
            break
    if guess == secretnumber:
        print("Yes " + str(secretnumber) + " is the number ")
        print("You have taken " + str (guesstaken)+" guesses to find the correct number")
    else:
        print("I was thinking of" + secretnumber)

except:
    print("enter a number not a word/letter")