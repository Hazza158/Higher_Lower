import random

comp_choice = 0

comp_num = [" computer # choice is {}"]

for item in range (0,20):
    comp_choice = random.choice(comp_num[:-1])
    print(comp_choice, end="\t")