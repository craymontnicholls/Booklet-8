#making variables global
global inventory
global floor
#import random integers
from random import randint
#takes the users input
def takeinput():
  Valid_input = False
  while Valid_input == False:
    user_input = input("> ") 
    try:
      user_input.lower()
      Valid_input = True
      return user_input
    except ValueError:
      print("please enter a string.")


#allows the user to pick up items from the floor
def pick():
  not_picked = False
  while not_picked == False:
    print("What item would u like to pickup?")
    for item in floor:
      print("-" + item + "\n",end="")
    print()
    item = takeinput()
    
    if item.lower() in floor:
      
      pos = floor.index(item)
      floor.pop(pos)
      inventory.append(item)
      not_picked = True
      
      access_inventory()
    else:
      print("item not found on floor")
  return
#allows user to drop items from the inventory
def  drop():
  not_dropped = False
  while not_dropped == False:
    print("What item would u like to drop?")
    item = takeinput()
    if item.lower() in inventory:
      pos = inventory.index(item)
      
      inventory.pop(pos)
      floor.append(item)
      not_dropped = True
    else:
      print("item not found in Inventory")



  return
#shows the user a random item from the inventory
def pull():
  random_num = randint(0,len(inventory))
  print("\nItem selected {}".format(inventory[random_num]))
  access_inventory()
  return
#allows the user to see all  items in the inventory
def search():
  print("items in inventory: \n")
  for item in inventory:
    print(item + "\n",end="")
  print()
  access_inventory()

  return
#start the other functions if certain things are inputted
def Action(action):
  action = action.lower()

  if action == "pick":
    pick()

  elif action == "drop":
    drop()

  elif action == "pull":
    pull()

  elif action == "search":
    search()
#tells the user to select an action nad validates it
def access_inventory():

  
  
 

  
  valid_action = False

  while valid_action == False:

    action = input("Select an action \n")
    try:
      action = action.lower()
    except ValueError: 
      print("\n Please enter an action")

    if action == "pick" or action == "drop" or action == "pull" or action == "search":
      Action(action)
    else:
      print("please select a valid action \n \n")

    

    
#item with the inventory
inventory = [ "sword", "shield", "bow", "rpg"] 
floor = ["axe", "mace", "crossbow", "hazmat", "semi-automatic rifle"]

access_inventory()