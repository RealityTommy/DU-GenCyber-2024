# This is a single-line comment.

'''
This is a multi-line
comment.
'''

name = "Tommy"   # string data type
age = 18         # integer data type
health = 100.0   # float data type
hungry = True     # boolean data type
inventory = ["sword", "shield", "cake"]  # list data type
money = {"copper": 25, "silver": 2}   # dictionary data type
quests = {"eat cake"}   # set data type

welcome_message = "Welcome, " + name + "!"   # string concatenation

health -= 10.0  # subtract 10.0 from number

inventory.append("health potion")   # add item to list
inventory.remove("cake")            # remove item from list

money["gold"] = 1       # add item to dicionary
money.pop("gold")       # remove item from dictionary
money["silver"] += 1    # arithmetic on item in dictionary

quests.add("save kitten")   # add item to set
quests.remove("eat cake")   # remove item from set

print(welcome_message)              # display message in console
name = input("What's your name? ")  # get user input

# Condition with if else statement
if health <= 0:
    print("Player is passed out.")
else:
    print("Player is awake.")

# Condition with elif
if health == 0:
    print("Player is passed out.")
elif health <= 50:
    print("Player is weak.")
else:
    print("Player is awake.")

# For loop to output inventory
for item in inventory:
    print(item)

# While loop while player is fighting
while health > 0:
    health -= 10
    print(health)

# Function to check which player is stronger
def strength_check(p1, p2):
    if p1 > p2:
        return "Player 1 wins!"
    
    elif p1 < p2:
        return "Player 2 wins!"

    else:
        return "Draw!"

player1 = input("What is player 1's power level? ")
player2 = input("What is player 2's power level? ")

winner = strength_check(player1, player2)
print(winner)