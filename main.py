#math test problem
#imports
from random import randint
from time import sleep

#subroutine to create and mark maths test
def maths_test(number_of_questions):
  #loop to keep program running
  while True:
    #initialises two dimensional array
    test = [["" for y in range(3)] for x in range(number_of_questions)]

    #creates the 5 questions
    for a in range(0,5):
      answer = randint(20,99)
      num1 = answer-randint(10,answer-10)
      num2 = answer-num1

      test[a][0] = num1
      test[a][1] = num2
      test[a][2] = answer

    total = 0
    print("There are {} in this test. You may begin.".format(number_of_questions))
    #loops until all questions are answers
    for x in range (0,number_of_questions):
      sleep(1)
      print("What is {} + {} = [ ]".format(test[x][0],test[x][1]))

      #validates answer
      while True:
        try:
          user_answer = input("> ")
          user_answer = int(user_answer)
          break

        except ValueError:
          print("\nPlease enter an integer.\n\n")

      if user_answer == test[x][2]:
        print("\nCorrect!\n\n")
        total += 1
      else:
        print("Incorrect.")

    print("Test complete.\n\n You scored {} out of {}".format(total,number_of_questions))
    sleep(3)
    print("\n\n\n")
#main program
maths_test(5)