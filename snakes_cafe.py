import sys
# creating menu 
a = """
######################################
##    Welcome to the Snakes Cafe!   ## 
##    Please see our menu below.    ##
##  To quit at any time, type quit  ##
######################################

MENU

Appitizers
----------
chips and guac
quesidillas
nachos
tortilla soup

Entrees
-------
street tacos
tostada
enchilada
fajitas

Desserts
--------
churros
flan
mexican chocolate pie

Drinks
------
margarita
mojito
jalapeno lemonade


"""

print(a)


# adding dictionary to keep track of count

foods = {
   "chips and guac": 0,
    "quesidillas" : 0,
    "nachos": 0,
    "tortilla soup": 0, 
    "street tacos": 0, 
    "tostada": 0, 
    "enchilada": 0, 
    "fajitas": 0, 
    "churros": 0, 
    "flan": 0, 
    "mexican chocolate pie": 0, 
    "margarita": 0, 
    "mojito": 0, 
    "jalapeno lemonade": 0
}

def exit_app():
    print('goodbye')
    sys.exit()

while True: 
    answer = input ('What would you like to order?')
    if answer == 'quit':
        exit_app()
    if answer in foods:
        foods[answer] += 1
        print(f"{foods[answer]} {answer} has been added to your meal")
    else:
        print("Hmmm... that's not on the menu")

