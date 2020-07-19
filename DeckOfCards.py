import random


print("Welcome to Deck of Cards")
print("\n")



# Deck of Card Class
class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        print("{} of {}".format(self.value, self.suit))



# Deck of Cards Class
class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()


    def build(self):
        for suitval in ["Clubs", "Diamonds","Hearts","Spades"]:
            for rankval in range(1, 14):
                self.cards.append(Card(suitval,rankval))

    def show(self):
        for c in self.cards:
            c.show()


    def shuffle(self):
        for i in range(len(self.cards)-1,0,-1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]



deck = Deck()
deck.shuffle()
deck.show()
