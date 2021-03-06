# Linked Lists

## Introduction

A common data structure, where all the items in a list have properties that depend on one another, is called a linked list. A linked list is a list that has a designated head and tail, and each item in the list has a memory connection of some sort to the next and previous item in the list. This is more common in C++, where information is typically not stored in memory right next to each other, but instead has a pointer to where in memory the information is stored for the next node and the previous node if the node is not the head or tail.

## Snake: Link Lists in Action

An example of this in Python, is the game Snake. In Snake, each of the body pieces has a coordinate that moves according to where the next piece is, and the player typically controls the head. If the head moves left, the next piece needs to know that it will move there next and so on until the tail know sthe command as well. Each of these body items depends on the previous to know where to go next. Each node has three characteristics:

Previous: (where the previous node is located, if the node is the head, this is blank)
Current: (where the node itself is located)
Next: (where the next node is located, if the node is the tail, this is blank)

# Inserting & Removing

Say we have a linked list as follows, where each node has [Previous, Current, Next]:


* Head [[None,0,1], [0,1,2], [1,2,3], [2,3,4], [3,4,None]] Tail

How would we go about changing the head or tail, without changing the data structure type? How could we add a new head or tail, or remove the existing head or tail?

### For removing the head we can do the following:

Current list: 
* [[None,0,1], [0,1,2], [1,2,3], [2,3,4], [3,4,None]]

Change Head's Next to new head, emptying it's previous:
* [[None,0,1], [None,1,2], [1,2,3], [2,3,4], [3,4,None]]

Disconnect and thus remove the head by emptying its next:
* [None,0,None]     
* [[None,1,2], [1,2,3], [2,3,4], [3,4,None]]

### For adding a new head we do the opposite:
Current List and new node:
* [None,-1,None]    
* [[None,0,1], [0,1,2], [1,2,3], [2,3,4], [3,4,None]]

Change head's previous to new node's current, making it not a head:
* [None,-1,None]    
* [[-1,0,1], [0,1,2], [1,2,3], [2,3,4], [3,4,None]]

Add new Head with no previous, it's current location and it next as the old head's current:
* [[None,-1,0], [-1,0,1], [0,1,2], [1,2,3], [2,3,4], [3,4, None]]

### For removing the tail, it is similar to removing the head:

Current list:
* [[None,0,1], [0,1,2], [1,2,3], [2,3,4], [3,4,None]]

Change tail's previous node to the new tail, emptying it's next:
* [[None,0,1], [0,1,2], [1,2,3], [2,3,None], [3,4,None]]

Disconnect and thus remove the tail by emptying its previous:
* [[None,0,1], [0,1,2], [1,2,3], [2,3,None]]    [None,4,None]

### For adding a new tail, it is similar to adding a new head:

Current list and new node:
* [[None,0,1], [0,1,2], [1,2,3], [2,3,4], [3,4,None]]   [None,5,None]

Change tail's next to the new node's current, making the old tail not a tail anymore
* [[None,0,1], [0,1,2], [1,2,3], [2,3,4], [3,4,5]]      [None,5,None]

Add the new tail with no next, it's current location and it's previous as the old tail's previous
* [[None,0,1], [0,1,2], [1,2,3], [2,3,4], [3,4,5], [4,5,None]]

### For the middle, it's basically combining the tail and head logic

Current list and new node:
* [[None,0,1], [0,1,2], [1,2,3], [2,3,4], [3,4,None]]   
* [None,2.5,None]

Find where the node is to be placed
* [[None,0,1], [0,1,2], [1,2,3], [new node to go here] [2,3,4], [3,4,None]]   
* [None,2.5,None]

Change the surrounding nodes to match the new node instead of each other:
* [[None,0,1], [0,1,2], [1,2,2.5], [new node to go here] [2.5,3,4], [3,4,None]]   
* [None,2.5,None]

Effectively add the new node by changing it's previous and next to match surrounding nodes:
* [[None,0,1], [0,1,2], [1,2,2.5], [2, 2.5, 3] [2.5,3,4], [3,4,None]]

### To remove a node from the middle:

Current list:
* [[None,0,1], [0,1,2], [1,2,3], [2,3,4], [3,4,None]]

Let's remove the third node. Change it's next and previous to None, effectively removing it:
* [[None,0,1], [0,1,2?], [2?,3,4], [3,4,None]]    
* [None,2,None]

Change the surrounding nodes to have previouses and nexts that match the previous or next node's current:
* [[None,0,1], [0,1,3], [1,3,4], [3,4,None]]      
* [None,2,None]

## Problem to Solve: Uno

In the card game, Uno, players draw cards and typically sort them in their hands. The sorting rules can vary, but typically players will sort their hands by color first, then by value.

```python
from random import shuffle

deck = []
start_hand_size = 7

def create_deck():
    global deck
    #action_cards = ["Skip", "Reverse", "Draw-2"] #there are two of each of these in each of the four colors, for 24 total
    colors = ["red", "blue", "yellow", "green"] #25 of each color, 1-9 twice, 1 0 (19) and 6 action cards = 25
    #wild_cards = [["black", "wild"], ["black", "draw-4"]] #8 wilds, or four of each)
    number_range = 9
    deck = []

    for color in colors:
        #for card in action_cards:
            #new_card = [color, card]
            #deck.append(new_card)
            #deck.append(new_card) #add twice as there are two of each action card
        for card in range(0, number_range+1):
            new_card = [color, card]
            deck.append(new_card)
            if card != 0:
                deck.append(new_card)
    # for card in wild_cards:
    #     deck.append(card)
    #     deck.append(card)
    #     deck.append(card)
    #     deck.append(card)
    
    print(deck)
    shuffle(deck)
    print("Shuffled:")
    print(deck)
    print(len(deck))

class drawn_card():
    def __init__(self, card):
        self.previous = []
        self.current = [card]
        self.next = []

def draw_card():
    global deck
    if len(deck) != 0:
        card = drawn_card(deck.pop(0))
        return card
    else:
        print("deck is empty, reshuffling")
        create_deck()
        draw_card()

class hand():
    def __init__(self):
        self.cards = []

    def sort_hand(self):
        #sort by color
        red_cards = []
        blue_cards = []
        yellow_cards = []
        green_cards = []
        black_cards = []
        for item in self.cards:
            if item.current[0] == "red":
                red_cards.append(item.current)
            elif item.current[0] == "blue":
                blue_cards.append(item.current)
            elif item.current[0] == "yellow":
                yellow_cards.append(item.current)
            elif item.current[0] == "green":
                green_cards.append(item.current)
            elif item.current[0] == "black":
                black_cards.append(item.current)
        #sort by value

def main():
    create_deck()
    player_hand = hand()
    for i in range(1, start_hand_size+1):
        drawn_card = draw_card()
        player_hand.cards.append(drawn_card)
    for item in player_hand.cards:
        print(item.current)
    (player_hand.sort_hand)

if __name__ == "__main__":
    main()
```
