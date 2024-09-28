import random

class game: #class for easier action between rounds
  def __init__(self):
    
    self.mainDeck = []
    self.deck1 = []
    self.deck2 = []
    self.p1Hand = 0 #these are the hands for both players
    self.p2Hand = 0
    self.warPile = []
    self.roundCounter = 0
    for i in range(13): #adds 4 of each rank into the deck
      for p in range(4):
        self.mainDeck.append(i+1)
    random.shuffle(self.mainDeck) #shuffles the maindeck
    
    for i in range(52): #splits the main deck into two
      if(i % 2 == 0):
        self.deck1.append(self.mainDeck[i])
      else:
        self.deck2.append(self.mainDeck[i])
    
    #keeps looping the game until one player has enough cards to prevent war or the round limit is reached
    while len(self.deck1) < 49 and len(self.deck2) < 49:
      self.drawCard()
      if self.roundCounter >= 256:
        break
    if len(self.deck1) > len(self.deck2):
      print(f"with {len(self.deck1)} cards in their deck Player 1 wins!")
    elif len(self.deck2) > len(self.deck1):
      print(f"with {len(self.deck2)} cards in their deck player 2 wins!")
    else:
      print("tie!")
  def drawCard(self):

    self.p1Hand = self.deck1[0] #sets the current card in hand with the top card of the deck
    self.p2Hand = self.deck2[0] 
    
    self.deck1.pop(0)
    self.deck2.pop(0)

    self.judge()
    self.roundCounter += 1

  def war(self): #in case of a tie
    self.warPile.append(self.p1Hand)
    self.warPile.append(self.p2Hand) #adds the two tieing cards to the list

    self.warPile.append(self.deck1.pop(0))
    self.warPile.append(self.deck2.pop(0)) #the two "face down cards get added to the list"

    self.drawCard() #calls the draw card function again to run the new round to see who wins the war


  def judge(self):
    if self.p1Hand > self.p2Hand: #checks if p1 wins
      print(f"P1 had {self.p1Hand}, P2 had {self.p2Hand}")

      if len(self.warPile) > 1: #this code just adds the warpile to the deck in the case judge was run after a war
        self.deck1.extend(self.warPile)
        self.warPile.clear()
      self.deck1.extend([self.p1Hand, self.p2Hand])
      

      print(f"Player 1's deck is currently at {len(self.deck1)}")
      
    elif self.p1Hand < self.p2Hand: #checks if p2 wins
      print(f"P1 had {self.p1Hand}, P2 had {self.p2Hand}")

      if len(self.warPile) > 1:
        self.deck2.extend(self.warPile)
        self.warPile.clear()

      self.deck2.extend([self.p1Hand, self.p2Hand])

      print(f"Player 2's deck is currently at {len(self.deck2)}")
    else:
      print("A tie Has occured!")
      print(f"P1 has {self.p1Hand}, P2 has {self.p2Hand}")
      self.war()


obj = game()