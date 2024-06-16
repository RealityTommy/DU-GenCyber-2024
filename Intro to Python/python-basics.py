# This is a single-line comment.

'''
This is a multi-line
comment.
'''

name = "Tommy"   # string data type
age = 18         # integer data type
health = 100.0   # float data type
alive = True     # boolean data type
inventory = ["sword", "shield", "cake"]  # list data type
money = {"copper": 25, "silver": 2}   # dictionary data type
quests = {"eat cake"}   # set data type

welcome_message = "Welcome, " + name + "!"   # strong concatenation

health -= 10.0  # subtract 10.0 from number

inventory.append("health potion")   # add item to list
inventory.remove("cake")            # remove item from list

money["gold"] = 1       # add item to dicionary
money.pop("gold")       # remove item from dictionary
money["silver"] += 1    # arithmetic on item in dictionary

quests.add("save kitten")   # add item to set
quests.remove("eat cake")   # remove item from set
