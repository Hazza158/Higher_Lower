
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

    print(

        """

    **** How To Play ****

    You will start by choosing 2 numbers of your choice to guess between.

    Then the computer will choose a number at random between your 2 chosen numbers.

    You will then have a specific amount of guesses ranging from how big the difference in your 2 numbers is.

    You will guess a number and the computer will say either higher or lower to get you closer to your number.

    ****Good Luck!****

        """

    )

    return ""

played_before = yes_no("have you played the game before?")

if played_before == "no": 
    instructions()
    
print("program continues")