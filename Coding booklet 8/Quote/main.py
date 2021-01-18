import random

def RandomQuote():
  Quote = [["" for x in range(2)]for Y in range(3)]
  Quote[1][0] = "code is like humour, when you have to explain it, it's bad."
  Quote[0][1] = "martin fowler"
  Quote[2][0] = "Simplicity is the soul of efficiency."
  Quote[2][1] = "Austin Freeman"
  Quote[0][0] = "Any fool can write code that a computer can understand.Good programers write code that humans can understand."
  Quote[1][1] = "Cory House"
  
  Index = random.randint(0,2)
  return Quote[Index][0], Quote[Index][1]

Quote, Author = RandomQuote()
random.seed()

print("{} - {}".format(Quote, Author))
