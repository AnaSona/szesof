money = 100 #this is an integer variable
money = money-20 #you have 80 of money from now.
name = "gay user" #this is a string
name = input("What's your name? ")
#this makes the "name" variable not "gay user", but whatever the user types.
#Note that this always returns a STRING, even if you type a number.

player_inventory = [] #this is an empty list
shopkeeper_inventory = ["wine","wine","beer"] #this is a list of strings.


print("hello", name + "!")
print("I have these:")
print(shopkeeper_inventory)
while (True): #infinite loop
    
    question_answer = input("Do you want to buy wine? Type yes or no ")
    if (question_answer == "yes"):
        if ("wine" in shopkeeper_inventory):
            shopkeeper_inventory.remove("wine")
            print(shopkeeper_inventory)
        else:
            print("Sorry, I actually ran out of wine")
            print("bye bye")
            break #break the infinite loop, end the game





#ideas to continue:
#
#make the player spend money while using the shop
#make the player able to choose what to buy

