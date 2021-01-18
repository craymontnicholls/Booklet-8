
def notebook():
  book = []
  for counter in range (0,9):
    book.append("")
  while True:
    valid_input = False
    while valid_input == False:
      note_access = input("which note would like to access? (1-10) \n")

      try:
        note_access = int(note_access)
        
        note_access -= 1
        if note_access <=9 and note_access >= 0:
          
          valid_input = True
        else:
          print("Please enter a number between 1 and 10")
      except ValueError:
        print("please a number between 1 and 10")
    if book[note_access] != "":
      print("There is already a note saved in this slot\n\n")
      print(book[note_access])
      note_change = input("Would you like to change this note?\n").lower()
      if note_change == "yes":
        new_note = input("Enter text \n\n> ")
        book[note_access] = new_note
    else:
      new_note = input("Enter text \n\n> ")
      book[note_access] = new_note


notebook()

    

