

import random

def gen_animal(seed):
  creatures = ["lizard ", "humanoid", "insect", "reaper", "bird"]
  colours= ["red", "green", "blue", "black", "white", "purple", "orange", "yellow" ]
  characteristics = ["angry", "happy", "mutual", "hostile", "passive", "friendly"]
  random.seed(seed)
  
  creature_pos = random.randint(0,len(creatures)-1)
  colours_pos = random.randint(0,len(colours)-1)
  characteristics_pos = random.randint(0,len(characteristics)-1)

  print("Animal:\n{} {} {}".format(characteristics[characteristics_pos],colours[colours_pos],creatures[creature_pos]))


while True:
  try:
    planet_num = int(input("Enter number of planet. \n"))
    break
  except ValueError:
    print("Please enter a number \n\n")

gen_animal(planet_num)