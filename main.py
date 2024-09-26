import random

class game: #class for easier action between rounds
  def __init__(self):
    
    self.mainDeck = []
    for i in range(13): #adds 4 of each rank into the deck
      for p in range(4):
        self.mainDeck.append(i+1)
    random.shuffle(self.mainDeck) #shuffles the maindeck
    
    self.deck1 = []
    self.deck2 = []
    
    for i in range(51):
      if(i % 2 == 0):
        self.deck1.append(self.mainDeck[i])
      else:
        self.deck2.append(self.mainDeck[i])
      
    self.p1Hand = 0 #these are the hands for both players
    self.p2Hand = 0
#    self.score = pass
  def drawCard(self):
    self.p1Hand = self.deck1[0]
    self.p2Hand = self.deck2[0] 
    
    self.deck1.pop(0)
    self.deck2.pop(0)
    if self.p1Hand > self.p2Hand:
      print("p1 wins")
      print(self.p1Hand, self.p2Hand)
    elif self.p2Hand > self.p1Hand:
      print("p2 wins")
      print(self.p1Hand, self.p2Hand)
    else:
      print("tie")
      print(self.p1Hand, self.p2Hand)
      self.war()
  def war(self):
    warPile = []
    warPile.append(self.p1Hand)
    warPile.append(self.p2Hand)
    warPile.append(self.deck1.pop(0))
    warPile.append(self.deck2.pop(0))
    self.drawCard()
  def judge(self):
    if self.p1Hand > self.p2Hand:
      print("P1 Wins!")
      print(self.p1Hand, self.p2Hand)
      self.deck1.extend[self.p1Hand, self.p2Hand]
#  def shuffleSplit(self):
# pass
#  def newRound(self):
#    pass
obj = game()
obj.drawCard()
