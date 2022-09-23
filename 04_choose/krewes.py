"""
Craig Chen, Aaron Gershkovich, Kosta Dubovskiy
SoftDev
04-krewes
-Dictionaries and Random- 
2022-09-22
time spent: 30 minutes
DISCO:
    * The key in the dictionary can be anything, and it's useful for categorization of many things
    * Need to import random with lowercase
    * Need to randint needs two arguments
    * randint is inclusive on both ends
    * random.choice(sequence) returns a random element
QCC:
    * Is there a way to generate a random item from an input list, with a built in random method
OPS SUMMARY:
    * We made a function, that given a dictionary with key:array pairs returns a random element of a random array
"""

krewes = {2:["devo1", "devo2", "devo3", "devo4", "devo5"], 7:["devo1", "devo2", "devo3", "devo4", "devo5"], 8:["devo1", "devo2", "devo3", "devo4", "devo5"]}

import random

def get_devo(dictionary):
    randKey = random.choice(list(dictionary.keys()))
    randDevo = random.randint(0, len(dictionary[randKey]) - 1)
    return dictionary[randKey][randDevo]

print(get_devo(krewes))
