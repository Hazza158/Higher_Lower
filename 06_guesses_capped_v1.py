import random
print ("welcome to the guess my number hardcore edition ")

print ("In this program you only get 5 guesses\n")

print ("good luck")

the_number = random.randint(1, 10)

user = int(input("What's the number?"))


count = 1
while user != the_number:

    if user > the_number:
     print ("Lower")

    elif user < the_number:
     print ("Higher")

    user = int(input("What's the number?"))
    count += 1
    if count == 5:
     break

else:
    print("You guessed it!!, the number is", the_number, "and it only"\
       " took you", count , "tries")

input ("\nPress enter to exit")    

