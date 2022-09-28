"""
Craig Chen, Aaron Gershkovich, Kosta Dubovskiy
SoftDev
K04-krewes
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
    * Generate a random key value from the given list of keys and then generate a random value somewhere within the length of that key. Return the value at that key value and then find a random value within the value assigned to the key.
"""

krewes = {2:
           ["NICHOLAS",  "ANTHONY",  "BRIAN",  "SAMUEL",  "JULIA",  "YUSHA",  "CORINA",  "CRAIG",  "FANG MIN",  "JEFF",  "KONSTANTIN",  "AARON",  "VIVIAN",  "AYMAN",  "TALIA",  "FAIZA",  "ZIYING",  "YUK KWAN",  "DANIEL",  "WEICHEN",  "MAYA",  "ELIZABETH",  "ANDREW",  "VANSH",  "JONATHAN",  "ABID",  "WILLIAM",  "HUI",  "ANSON",  "KEVIN",  "DANIEL",  "IVAN",  "JASMINE",  "JEFFREY"], 
           7:["DIANA",  "DAVID",  "SAM",  "PRATTAY",  "ANNA",  "JING YI",  "ADEN",  "EMERSON",  "RUSSELL",  "JACOB",  "WILLIAM",  "NADA",  "SAMANTHA",  "IAN",  "MARC",  "ANJINI",  "JEREMY",  "LAUREN",  "KEVIN",  "RAVINDRA",  "SADI",  "EMILY",  "GITAE",  "MAY",  "MAHIR",  "VIVIAN",  "GABRIEL",  "BRIANNA",  "JUN HONG",  "JOSEPH",  "MATTHEW",  "JAMES",  "THOMAS",  "NICOLE",  "Karen"],
           8:["ALEKSANDRA",  "NAKIB",  "AMEER",  "HENRY",  "DONALD",  "YAT LONG",  "SEBASTIAN",  "DAVID",  "YUKI",  "SHAFIUL",  "DANIEL",  "SELENA",  "JOSEPH",  "SHINJI",  "RYAN",  "APRIL",  "ERICA",  "JIAN HONG",  "VERIT",  "JOSHUA",  "WILSON",  "AAHAN",  "GORDON",  "JUSTIN",  "MAYA",  "FAIYAZ",  "SHREYA",  "ERIC",  "JEFFERY",  "BRIAN",  "KEVIN",  "SAMSON",  "BRIAN",  "HARRY",  "wanying"]
         }


import random

def get_devo(dictionary):
    randKey = random.choice(list(dictionary.keys()))
    randDevo = random.randint(0, len(dictionary[randKey]) - 1)
    return dictionary[randKey][randDevo]

print(get_devo(krewes))
