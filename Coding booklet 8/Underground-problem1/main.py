#subroutine to calculate number of stops between two stops on the victoria line
def victoria_line():
  victoria = ["Brixton", "Stockwell", "Vauxhall", "Pimlico", "Victoria", "Green Park", "Oxford Circus","Warren Street", "Euston","King's Cross","Highbury & Islington", "Finsbury Park","Seven Sisters","Tottenham Hale", "Blackhorse Road and Walthamstow Central"]

  #outputs all the stations
  for station in victoria:
    print("- " + station + "\n",end="")
  print()
  #validates station
  while True:
    start = input("Please enter your start station.\n> ")
    if start in victoria:
      break
    else:
      print("Please enter a valid station.")

  #validates station and makes sure it is not the same
  while True:
    end = input("Please enter your final station.\n> ")
    if end in victoria and end != start:
      break
    else:
      print("Please enter a valid station.")
 
  start_num = victoria.index(start) + 1

  end_num = victoria.index(end) + 1

  total_stops = 0

  #calculates station difference if it goes past the end of the loop

  if end_num < start_num:
    total_stops = 15-start_num
    total_stops += end_num
    #subtracts the final stop
    total_stops -= 1

  #calculates difference normally
  else:
    total_stops = end_num - start_num - 1

  print("Total number of stops between {} and {} is {}".format(start,end,total_stops))


#main program
victoria_line()