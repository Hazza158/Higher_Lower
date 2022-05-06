
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()
        
        if response == "yes" or response == "y":
            response = "yes"
            return response
            
        
        elif response == "no" or response == "n":
            response = "no"
            return response
        
        else:
            print("please answer yes / no")



def instructions():
    print("**** How to Play ****")
    print()
    print("pick the lowest number e.g '1' and then pick the highest number e.g '10'")
    print("the computer will chose a random number between the '1' and the '10'")
    print()
    print("your job is to guess the number that the computer has chosen")
    print("you will have 3 guesses to find the correct number")
    print()
    print("when you guess a number the computer will say either 'higher' or 'lower' this will help you to find the number easier")
    print("")
    print("")
    print("")
    print()
    print("\t***Good luck, have fun***")
    print()
    return "" 

played_before = yes_no("have you played the game before?")

if played_before == "no": 
    instructions()
    
print("program continues")