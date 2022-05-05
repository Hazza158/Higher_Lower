



# functions go here
def instructions():
    print("**** How to Play ****")
    print()
    print("1) Choose amount of rounds or press <enter> for infinite mode")
    print()
    print("2) For each round, choose from rock / paper / scissors(or xxx to quit)")
    print("   You can type r / p / s / x if you dont want to type the entire word")
    print()
    print("3) The rules are:")
    print()
    print(" - rock beats scissors")
    print(" - paper beats rock")
    print(" - scissors beats paper")
    print()
    print("\t***Good luck, have fun***")
    print()
    return "" 

def check_rounds():

    while True:
        response = input("how many rounds: ")
        round_error = "please type either <enter> or an integer that is more than 0"
        # if infinite mode is not chosen, chech response
        # is an integer that is more than 0 
        if response != "":
            try:
                response = int(response)
                # if respons is too low, go back to start of loop
                if response < 1:
                    print(round_error)
                    continue
            # if response is not an integer, go back to
            # start of loop
            except ValueError:
                print(round_error)
                continue

        return response

def choice_checker(question, valid_list, error):

    valid = False
    while not valid:

        #ask user for choice (and put choice in lower case)
        response = input(question).lower()

        # iterates through list and if response is an item
        # in the list (or the first letter of an item), 
        # the full name is returned

        for item in valid_list:
            if response == item [0] or response == item:
                return item
        
        #output error if item nt in list
        print(error)
        print()

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
# instructions



# base component



# end game summary

# game stats
rounds_won = rounds_played - rounds_lost

# calculate game stats
percent_win = rounds_won / rounds_played * 100
percent_lose = rounds_lost / rounds_played * 100


print()
print("\t**** Game History ****")
print()
for game in game_summary:
    print(game)


print()

# displays game stats with % values to the nearest whole number
print("\t**** Game Statistics ****")
print()
print("Win: {}, ({:.0f}%)\nLoss: {}, ({:.0f}%)\nTie: {}, ({:.0f}%)".format(rounds_won, percent_win, rounds_lost, percent_lose,))

# show game statistics
# quick calculations (stats)
rounds_won = rounds_played - rounds_lost

# end of game statements
print()
print("\t**** End Game Summary ****")
print()
print("Won: {} \t|\t Lost: {}".format(rounds_won, rounds_lost,))
print()
print("Thanks for playing")
