# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 04:27:26 2020

blackjack - milestone project 2 - blackjack

@author: jblock
"""

"""
to-do list
---------------
v     -class for deck actions
v     -class for card actions
v     -class for hand actions
v     -bank     
v     -create gameplay
v          -create player number q
v          -deck number q - 1-8
v          -start deal and set bets
v              -if ace check if 1/11
v          -turns
v                -if ace check if 1/11
v                -hit
v                -stand
v                -double down
v                -split a pair
v          -dealer actions
x          -deal with lack of cards when none can be delt
v          -pay winner
v          -creat bust and blackjack checker
v          -win check
v          -replay posoblity
v          -add instructions possible to choose
v    -play another hand num q     
optional
---------
    -creat gui


problems
--------




"""


import random

suits = ("Hearts","Diamonds","Spades","Clubs")
ranks = ("Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace")
values = {"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":10,"Queen":10,"King":10,"Ace11":11,"Ace1":1}
players = 0
bets = {}
turn = 0
playerhands = {}
min_bet = 0
deck = 0
decks_num = 0
bank = {}

class Bank:
    def __init__(self):
        self.money = 0
        
    def deposit(self,amount):
        self.money += amount
        self.action_ok = True
    
    def withdraw(self,amount):
        if amount > self.money:
            self.action_ok = False
        else:
            self.money -= amount
        
    def __str__(self):
        return str(self.money) + "$"

class Card:
     def __init__(self,rank,suit):
          self.rank = rank
          self.suit = suit
          
     def __str__(self):
          return self.rank + " of " + self.suit

class Deck:
     def __init__(self,decknum):
          self.deck = []
          for decks in range(decknum):
              for suit in suits:
                    for rank in ranks:
                         self.deck.append((rank,suit))
     def __str__(self):
          x = ""
          for y,z in self.deck:
              x = x + str(Card(y,z)) + ", "
          return x
     def shuffle(self):
          random.shuffle(self.deck)
     
     def deal(self):
          return self.deck.pop()

class Hand:
    def __init__(self,belongs_to):
        self.belongs_to = belongs_to
        self.blackjack = False
        self.bust = False
        self.cards = []
        self.value = [0]
        self.aces = 0
    def __str__(self):
          x = ""
          for y,z in self.cards:
              d = y
              if y == "Ace1" or z == "Ace11":
                 d = "Ace"
              x = x + str(Card(d,z))  + ", "
          return x
    def add_card(self,card,suit):
          self.cards.append((card,suit))
     
    def check_value(self):
         value = 0
         for x,y in self.cards:
             value += values[x]
         return value



#gameplay
while True:
    #instructions q
    while True: 
         instructionsq = input("do you want instructions? y/n ")
         if instructionsq.lower() == "y":
              print("\n\n--------------------\ninstructions\n--------------------\nThe Objective of Blackjack\n----------------\nBeat The Dealer. There are some misconceptions about the objective of the game of blackjack but at the\nsimplest level all you are trying to do is beat the dealer.\n\nHow do you beat the dealer?\n--------------\n1) By drawing a hand value that is higher than the dealer’s hand value\n2) By the dealer drawing a hand value that goes over 21.\n3) By drawing a hand value of 21 on your first two cards, when the dealer does not.\n\nHow do you lose to the dealer? \n---------------------\n1) Your hand value exceeds 21.\n2)The dealers hand has a greater value than yours at the end of the round\n\nIt’s also important to note, the other players’ hands at the table have nothing to do with winning the game of\nBlackjack like they do in Poker games. For all practical purposes, it’s just you against the dealer. Unskilled\npatrons of the game will try to convince you “it’s a team sport” but don’t be fooled.\n\nHow Do You Find a Hand’s Total Value?\n-------------------------\nBlackjack is played with a conventional deck of 52 playing cards and suits don’t matter.\n1)2 through 10 count at face value, i.e. a 2 counts as two, a 9 counts as nine.\n2)Face cards (J,Q,K) count as 10.\n3) Ace can count as a 1 or an 11 depending on which value helps the hand the most.\n")
              print("The Blackjack Tables’ Layout\n-------------------------\n\nBlackjack is usually played on a semicircular table that can accommodate varying numbers of players. The most\ncommon tables accommodate 7 players (or seven “spots”) but we’ve seen tables that only allow 5 players and\nother tables that have 12 spots! The dealer stands behind the table and chip rack and the players sit on the\nother side.\n\nPlaying Blackjack\n--------------------\n\nBlackjack games come with many rule variations and different numbers of decks. The most common game of\nblackjack is dealt out of a 6-deck or 8-deck “shoe” (a plastic, card-dispensing device). Single and double deck\ngames are still alive and well but not all casinos that have blackjack will have single and double deck so the\n“shoe games” are a little more common. Our example will be the procedure for the most common blackjack\ngame played with 6 decks. Here is the basic overview of a round of blackjack:\n\n1. Player Buys Chips\n---------------------------\nBefore you can play at the table you need chips. Most casinos will not allow “cash plays” wagers anymore, so you will have to let the dealer exchange your money for casino chips. You do this by simply walking up to the table a placing your money on the felt of the table. Do not hand your money to the dealer (they won’t take it). For security reasons dealers cannot take anything out of a player’s hand or vice versa. Once you lay your money on the felt the dealer will lay it out on the table for the cameras to clearly see how much it is and a pit boss will come over and verify the amount. The dealer will count out chip denominations equal to the amount you’ve bought in for and push the chips toward you. You are now free to handle the chips and place your wager. The dealer will arrange your buy-in on the felt so the cameras can clearly see the amount. This is what buying in for $1000 looks like.\n2. Player Places a Wager\n---------------------------\nAt the start of a round the first thing you do is place a bet in the betting circle (sometimes it’s a square, or just a casino logo on the felt where your bet goes). The table will have a small sign on the far right or left side of the table telling you what the betting limits are. Most tables in the US will require a minimum of at least $5 per hand, but the minimum and maximum bet you can make will be different depending on what casino you go to and the regulatory environment where the casino is located.\n\n3. Dealer Deals Cards to Players\n--------------------------\n\nAfter you place your bet the dealer will deal clockwise, one card, face up, to each player at the table and then one card face down for herself. Then she will deal one more card face up to each player and one more card for herself, face up. Each player has 2 cards, face up, in front of them, but the dealer has one card face up and one face down. It should look something like the picture below. Now it’s time to play the game!\n\n4. Player decides how to play hand\n------------------------")
              print("The dealer will start at the person on their left (also known as “first base”) and wait for that player to play their hand. You have two cards face up in front of your bet. To play your hand, first you add the card values together and get a hand total anywhere from 4 to 21. If you’re dealt a ten-value card and an Ace as your first two cards that means you got a Blackjack! Congratulations! Those get paid 3 to 2 (or 1.5 times your wager) immediately, without playing through the round, as long as the dealer doesn’t also have a Blackjack. If the dealer also has a Blackjack, you wouldn’t win anything but you also wouldn’t lose your original wager. This is called a “push”. If YOU don’t have a Blackjack AND the dealer doesn’t have a blackjack, your dealer will point to each player in succession and wait for you to decide how you want to play your hand. When it’s your turn, you will have to make your decision using the appropriate hand signal. Dealers will not respond to your verbal instructions because the cameras need to see your decisions as well. There are 5 ways you can play your hand:\nStand – If your first two cards are acceptable, you can stand and the dealer will move on to the next player. [Hand signal: Wave your hand or simply put out an open palm over the felt.]\n\nHit – If you would like more cards to improve your hand total, the dealer will deal you more cards, one at a time, until you either “bust” (go over 21) or you choose to stand. There is no limit on the number of cards you can take (other than going over a total of 21). [Hand Signal: Tap the felt with your finger.]\n\nSplit – If you’re dealt a pair (2 cards of equal value) you have the option to put out a second wager and the dealer will split the two cards so that each card will become the first card on two new hands. This also applies to face cards. You are allowed to split a hand consisting of a King and a Jack because they both have the same value, even though they are not actually a pair. [Hand signal: Put up a second wager equal to your first. Then give a “peace sign” to signify you would like to split and not double down. The dealer will make two hands out of your first hand and you will be dealt a second card on each.]\n\nSurrender – If you don’t like your initial hand, you have the option of giving it up in exchange for half your original bet back. [Hand signal: draw a line across the felt behind your bet as if you were cutting a slit in the felt with an imaginary knife. It is common for dealers to mistake this signal for the “hit” signal. To be safe, always verbalize the word “surrender” to your dealer and then make the signal on the felt for the cameras.]\n\n5. Dealer Plays Hand\n---------------------\nI know what you’re thinking, “Oh my gosh, that’s a lot of options, how do I know which one is the best choice?” Well, that depends on the dealer’s “up-card” (the dealer card that is face up and visible to the players)\nBasic Strategy\nBased on what the dealer is showing, and what you have in your hand, you make the choice that follows basic strategy. Basic strategy is the mathematically optimal way to play for every combination of player hand and dealer up-card. It was created by a computer that played millions of rounds of blackjack and determined the best way to play each hand combination based on what worked out best for the player most often. If you follow basic strategy it takes the guesswork out of the decision! Phew!")
              print("Player Hand Resolution\n-----------------------\nWhen you follow basic strategy and play your hand by using one of the 5 options listed above, one of 3 things will happen.\n1) You Stood Immediately – You were dealt a hand that basic strategy says you should not take any cards on.\n2)You made a hand – You took more cards (hit, double or split) and achieved a hand total of 21 or less and did not bust.\n3)Your hand is out of play – You hit your hand one or more times and “busted” or you chose to surrender your hand. If your hand busts you immediately lose your wager. This is why the casino has an edge on the game. The player must act first, so that even if the dealer eventually busts like you did, they still keep your money because you busted first.\n\nIf your hand hasn’t busted, and you didn’t surrender, then it’s time for the dealer to play their hand. The dealer will first flip over their “hole card” (the face down card) and add up their 2-card hand. If the dealer has a hand total of 17 or higher, they will automatically stand. If the dealer has a hand total of 16 or lower, they will take additional hit-cards. Doubling, splitting and surrender are not available to the dealer and the dealer does not have any choice with how they play their hand like the player does. The Dealer must play their hand the same way every time. The only exception is when the dealer has a 17 that consists of an Ace and a six. This is called a “soft 17” and, depending on the casino, this hand is sometimes hit by the dealer because it can also count as a 7 (due to the flexible value of an ace), giving the dealer more chances to get a better hand than 17. This gives the casino a bigger advantage than if the dealer stands on ALL 17s. Whether or not the dealer will hit a soft 17 will usually be prominently displayed, in text on the the felt, so you know how to expect the dealer to play their hand. Again, dealers do not have the option to deviate from the rules set by the casino.\n\n6. Payouts\n------------------\nOk so you’re done playing your hand and the dealer is done playing their hand according to the restrictions above. One of 2 things will happen.\n\n")
              print("The dealer will bust, and they will pay even money (1 times the wager) to each hand that is still in play on the table. or… The dealer will make a hand (17 through 21). If your hand is still in play, it’s a simple battle of who has the higher hand. If the dealer has the higher hand, they sweep your bet. If you have the higher hand, the dealer pays you one times your wager. If you and the dealer have the same hand-total, it’s considered a “push” and you keep your money but are not paid on your wager. Now the round is over! That’s all there is to it. The cards get swept up and you start another round. Interested in Playing Blackjack Properly? Check out our complete Blackjack Strategy Guide Blackjack Strategy Guide Special Situations There are a couple situations where a game of Blackjack will deviate from the procedures outlined above. Insurance/Even Money: Insurance is a side bet offered when the dealer has an Ace as an up-card. Before anyone plays their hands the dealer will offer insurance (or even money if you have a Blackjack). You can put up a wager equal to half your original wager or less, which will get paid 2 to 1 if the dealer has a ten as their hole card. So, put simply, you’re betting on whether or not the dealer has a blackjack. If you win, you get paid 2 to 1. As a basic strategy player you should always say no to insurance and even money. Only a card counter is skilled enough to play this side bet. Once all the players who want to buy insurance place their bets, the dealer will check her hole card (using a special viewing window in the table). If they have a ten underneath, the dealer got a Blackjack, and will take everyone’s original wager. Anyone who bought insurance will get paid 2 to 1 on their insurance wager. If the dealer does not have a ten underneath, she will take any insurance wagers that were made and the game will continue like it normally would. If you hold a blackjack while the dealer has an ace showing, you will be offered “even money.” Don’t be fooled! This is just another name for what is mathematically the same as insurance. If you take even money, your blackjack will not get paid 3 to 2 like it normally would. It will just get one times the original wager (even money) regardless of whether or not the dealer has a blackjack. If you do not take even money and the dealer has a blackjack your wager will push and your blackjack will not get paid. If you don’t take even money and the dealer does not have a blackjack you will be paid 3 to 2 like you normally would. Again, you should never take even money if you are not a professional card counter. To better understand the difference (or lack thereof) between insurance and even money watch this video from our premium video course: The Truth about Insurance. Non-Insurable Dealer Blackjack: It is possible for the dealer to have a blackjack without offering insurance or even money. If the dealer is showing a ten up, they will check their hole card automatically, before anyone is allowed to play their hands. If there is an ace underneath, the dealer has a blackjack and all bets on the table will be taken except for any player blackjacks, which would just push. Insurance is only offered when the dealer is showing an ace. Dead hand: If all players at the table bust before the dealer plays their hand, it’s considered a “dead hand” and the dealer will flip over her hole card (so the cameras can see it) and then sweep the cards up and put them in the discard tray. There is no reason to play the dealer’s hand and waste cards because the dealer has already beaten the player(s). Side bets: In the last 2 decades or so, Blackjack side bets have become popular. Insurance is the only side bet that is universally offered on all Blackjack tables and is a big part of beating the game for a card counter. But there are hundreds of other kinds of side bets on the felts these days. Most of them will require you to place a bet at the same time you place your main wager. You can be betting on getting a pair as your first two cards, betting on if the dealer’s cards will match yours, betting on your hand making a poker hand with the dealer’s up-card, betting on whether or not the dealer with bust, etc. These side bets are everywhere and have various different procedures and pay tables so we will not explain them here. Just know that they are not part of the game of Blackjack itself but may affect the normal dealing procedure of the game. We never recommend playing these side bets. Casinos only offer them because they have a huge advantage over you. Don’t be a sucker and learn how to count cards instead. Blackjack Rule Variations There are many different rule variations and conditions that can affect how the game of Blackjack is played. In other words, not all blackjack games are created equal, in terms of the odds and favorability to the player. Here is an overview of some of the rules that will affect the odds of the game. Doubling After Splitting (DAS): This simply means you can double down on a hand you just split. Some casinos will allow you to double after splitting and some don’t. Most casinos do allow this rule and it IS advantageous to the player. Re-Splitting Aces (RSA): Some casinos allow the player to re-split their aces after they have already split a pair of aces, meaning if you just split a pair of aces and received another ace as the next card, you are allowed to split to a 3rd hand up to a total of 4 hands. The ace is the most powerful card for the player so it is a very advantageous rule for the player if the casino allows RSA. Typically speaking, even if the casino offers RSA, you are still only allowed to take one card on each ace. You can’t double after splitting an ace and you can’t take additional cards. This is because the casinos know the Ace is the most powerful card and they are trying to limit situations where the player has an advantage. Early Surrender: This is a dead rule that hasn’t been in casinos in the United States since the 70s. It is the same as the usual “surrender” rule only you can surrender before the dealer checks for a blackjack or offers insurance. When it was still around it was highly favorable to the player, to the point where a perfect basic strategy player could have a small edge, without counting cards. It went extinct for that reason. Early surrender is also the reason why some perfectionists will call the common surrender rule by its proper name, “late surrender” to distinguish it from its counterpart. 6 to 5 Blackjacks: Some casinos that offer blackjack will reduce the 3 to 2 payout for Blackjacks down to only 6 to 5. This increases the house edge and takes more money out of people’s pockets. It also makes card counting basically useless. Even casinos that have this rule may not have it at every table. Be sure to read the rules on the felt before you sit down. CSM Blackjack: Some casinos use Continuous Shuffling Machines on their blackjack tables. This is a machine that continually shuffles the cards as they are being played. Instead of putting the cards in the discard tray until the end of the shoe, the dealer will continually feed the machine all the used cards and there is never an end to the shoe. This also makes card counting impossible and worsens the odds for a basic strategy player. Single Deck versus Multi-deck: All else being equal, the house edge on Blackjack gets higher for every deck you add to the game. As a rule of thumb, a 6 deck game will have a higher house edge than a 2 deck game if all other conditions are equal. The problem is, all the other conditions are rarely equal. Often times a single deck game will not allow doubling after splitting or re-splitting aces and will have 6 to 5 blackjacks, whereas an 8 deck game in the same casino might allow DAS, RSA, and have 3:2 Blackjacks and end up with a lower house edge. There are many trade-offs when it comes to the rules and number of decks. Deck/Shoe Penetration (PEN): This refers to the percentage of the cards that are actually dealt out over the course of a shoe. Usually the there is a cut card inserted in the shoe toward the back of the cards to be dealt. When the cut card is dealt out in the course of the game, it signals to the dealer that the shoe is running out of cards and the dealer will shuffle the cards and start a new shoe. While a quarter deck of cards is plenty sufficient to finish a round of Blackjack, most casinos will cut off much more than that (several decks) to limit the profitability of the game for a card counter. For a card counter, the depth of penetration can make or break a blackjack game. Games Masquerading As Blackjack Blackjack is a very popular game in the United States because many people try to beat it by counting cards. Because of its popularity and commonly known rules, many casinos have created Blackjack variants that use a lot of Blackjack rules and terminology to try and piggyback on Blackjack’s notoriety. Casinos know they are creating new games entirely, but they want you to think the new games are the same as blackjack so that you can feel like you’re playing a familiar game and the casino can enjoy a higher house edge. Here are some of the Blackjack doppelgängers you should avoid: Super Fun 21: This is usually pretending to be a single-deck blackjack game where you can surrender on any number of cards, you can double on any number of cards, and you can get paid automatically if you have a 6 card 20 or a 5 card 21 and a player blackjack always wins money! It sounds like a dream. The only problem is that blackjacks only pay even money (except for diamond suited blackjacks). That one change to how blackjacks get paid erases all the benefit of the “super fun” rules they give you and makes the house edge almost 3 times worse than regular blackjack. This game is not Blackjack. Stay away! Spanish 21: This game is very popular in many parts of the country. Many of the same rules as above are also present in this game but blackjacks still pay 3 to 2 and you can re-double (double down twice on the same hand). That sounds awesome right!? WRONG! They remove all the 10s from the shoe (the face cards are still in there but no ten cards). If you know anything about counting cards, you know the ten-value cards and aces are the most valuable cards for the player. Removing all the tens from the deck erases all the awesome you get from the better rules. It also has a more complicated basic strategy than conventional blackjack so most people do not play correctly and thus most people are playing at a much bigger disadvantage than what the game insert would print about the game. The casinos love Spanish 21 players. This game is not Blackjack. STAY AWAY! Free Bet Blackjack: In this game you play just like Blackjack but instead of supplying your own money to double down and split, the casino will let you do it for free but still pay you as if you had wagered the money. Sounds too good to be true right? It is! In exchange for the free roll, if the dealer goes over 21 with a hand total of 22, then all bets push (even though the dealer busted). BARF! This doubles the house edge of normal Blackjack. This is not Blackjack. Stay away! Blackjack Switch: This game is a little different. You start with 2 hands of blackjack and you can choose to switch the top cards of each hand if you think it will make you a better set of two hands. Any of us who have played blackjack a long time wish we could do that sometimes so this sounds like it could really save your hands right? NOPE! Just like Free Bet Blackjack, the dealer pushes all bets if they get a 22 and player Blackjacks only pay even money. This is not Blackjack! No thank you! There are many more games masquerading as Blackjack that we haven’t mentioned here because it would take all day. Don’t be fooled and make sure you’re playing real blackjack before you sit down!")
              break
         if instructionsq.lower() == "n":
              break
          
    #hand num q
    while True: 
         handnumq = input("how many hands will you play in this game? ")
         try:
              m = int(handnumq)
         except:
              print("you have not inputed a number - try again")
         else:
              hand_num = int(handnumq)
              break
              
    #deck num q
    while True: 
         decknumq = input("how many decks will this game have? 1-8 ")
         try:
              m = int(decknumq)
         except:
              print("you have not inputed a number - try again")
         else:
              if int(decknumq) >= 1 and int(decknumq) <= 8:
                  decks_num = int(decknumq)  
                  break
              else:
                    print("you have inputed a number that isn't between 1 and 8")
     
    #player num q
    while True: 
         playernumq = input("how many players will this game have? 1-7 ")
         try:
              m = int(playernumq)
         except:
              print("you have not inputed a number - try again")
         else:
              if int(playernumq) >= 1 and int(playernumq) <= 7:
                  players = (int(playernumq))
                  break
              else:
                    print("you have inputed a number that isn't between 1 and 7")
                    
    #money
    for x in range(players):
        bank[x+1] = Bank()
    while True: 
         deposit = input("how much do you want to inisialy deposit? $")
         try:
              m = int(deposit)
         except:
              print("you have not inputed a number - try again")
         else:
             deposit = int(deposit)
             for x in range(players):
                 bank[x+1].deposit(deposit)
             bank["original"] = deposit
             break
    stop2 = False         
    stop3 = False
    while not(stop3):
        stop2 = False         
        stop3 = False
        while not(stop2):
             moreq = input("do you want to deposit or withdraw from any player? y/n ")
             if moreq.lower() == "y":
                 
                 while not(stop2):
                     playerq = input(f"which player? (1-{players}) ")
                     try:
                          m = int(playerq)
                     except:
                          print("you have not inputed a number - try again")
                     else:
                         playerq = int(playerq)
                         if playerq <= players:
                             while not(stop2):
                                 typeq = input("deposit(d) or withdraw(w)? d/w ")
                                 if typeq.lower() == "d":
                                     while not(stop2):
                                         amount = input("how much do you want to deposit?$")
                                         try:
                                              m = int(amount)
                                         except:
                                              print("you have not inputed a number - try again")
                                         else:
                                             amount = int(amount)
                                             bank[playerq].deposit(amount)
                                             stop2 = True
                                             break
                                 elif typeq.lower() == "w":
                                     while not(stop2):
                                         amount = input("how much do you want to withdraw?$")
                                         try:
                                              m = int(amount)
                                         except:
                                              print("you have not inputed a number - try again")
                                         else:
                                             amount = int(amount)
                                             bank[playerq].withdraw(amount)
                                             if bank[playerq].action_ok:
                                                stop2 = True
                                                break
                                             else:
                                                print("not enugh money try again")
                                 else:
                                     print("you have not inputed d/w. exiting aditinal changes.")
                                     stop2 = True
                                     break
                             break
                         else:
                            print("you have not inputed an existing player. exiting aditinal changes.")
                            break
             elif moreq.lower() == "n":
                 stop2 = True
                 stop3 = True
                 break
             else:
                 stop2 = True
                 stop3 = True
                 print("you have not inputed y/n. presuming no-resuming.")
                 break
         
        while stop3:
            againq = input("do you want to deposit or withdraw from any player again? y/n ")
            if againq.lower() == "y":
                 break
            elif againq.lower() == "n":
                stop3 = True  
                break
            else:
                 print("you have not inputed y/n. try again")
    print("\n\nbank\n------------")
    counter = 0
    for x in range(len(bank)-1):
        counter +=1
        y = bank[counter].money
        print(f"Player {x+1} has {y}$")
    
    #minimum bet
    while True:
         min_bet = input("what should the minimum bet be? $")
         try:
              m = int(min_bet)
         except:
              print("you have not inputed a number - try again")
         else:
             min_bet = int(min_bet) 
             if min_bet > bank["original"]:
                 print("too much - no one has that much money")             
             else:
                 break
    for x in range(hand_num):    
        #make hands and deck
        for x in range(players):
            playerhands[x+1]=Hand(x+1)
        playerhands["dealer"] = Hand("dealer")
        deck = Deck(decks_num)
        
        #take bets
        for x in range(players):
            while True:
                if min_bet == 0:
                    bet = input(f"Player{x+1} what is your bet? $")
                else:
                    bet = input(f"Player{x+1}. place your bet. the minimum bet is ${min_bet}. your bet? $")
                try:
                    m = int(bet)
                except:
                    print("you have not inputed a number - try again")
                else:
                    if int(bet) >= min_bet:
                        if bank[x+1].money >= int(bet):
                            bets[x+1] = int(bet)
                            break
                        else:
                            print("you don't have enugh money place a lower bet.\n")
                    else:
                        print("that is less then then the minimum bet try again")
        
        #shuffle decks
        deck.shuffle()
        
        #deal first cards
        for z in range(2):    
            for x in range(players):
                y = deck.deck.pop()
                card = y[0]
                suit = y[1]
                if card == 'Ace':
                    while True: 
                        acetype = input(f"player {x+1} has received an ace. do you want it to be worth 11 or 1? 1/11 ")
                        if acetype == "1":
                            playerhands[x+1].add_card("Ace1",suit) 
                            break
                        elif acetype == "11":
                            playerhands[x+1].add_card("Ace11",suit) 
                            break
                        else:
                            print("try again you have not inputed 1 or 11") 
                            
                else:
                    print(f"\nplayer {x+1} has received a {Card(card,suit)}")
                    playerhands[x+1].add_card(card,suit)
        #dealer 2 cards
        y = deck.deck.pop()
        card = y[0]
        suit = y[1]
        if card == 'Ace':
            if playerhands["dealer"].check_value() + 11 > 21:
                ace = "Ace"
                print(f"the dealer has received a {Card(ace,suit)} and is counting it as a value of 1")
                playerhands["dealer"].add_card("Ace1",suit) 
                
            else:
                ace = "Ace"
                print(f"the dealer has received a {Card(ace,suit)} and is counting it as a value of 11")
                playerhands["dealer"].add_card("Ace11",suit) 
                
        else:
            print(f"the dealer has received a {Card(card,suit)}")
            playerhands["dealer"].add_card(card,suit)
        #hidden card
        y = deck.deck.pop()
        card = y[0]
        suit = y[1]
        if card == 'Ace':
            if playerhands["dealer"].check_value() + 11 > 21:
                playerhands["dealer"].add_card("Ace1",suit) 
                
            else:
                playerhands["dealer"].add_card("Ace11",suit) 
                
        else:
            playerhands["dealer"].add_card(card,suit)
        print("the dealer has received a card")
        
        #display hands
        print("\n the curent hands are -\n---------------------")
        for x in range(players):
            z = str(playerhands[x+1])
            m = playerhands[x+1].check_value()
            print(f"\nPlayer {x+1} has - a {z}. which has a value of {m}")
        visible_dealer_card = ()
        if playerhands["dealer"].cards[0][0] == "Ace":
            visible_dealer_card = ("Ace",playerhands["dealer"].cards[0][1])
        else:    
            visible_dealer_card = playerhands["dealer"].cards[0]
        print(f"\nThe dealer has a {visible_dealer_card[0]} of {visible_dealer_card[1]} and a hidden card")
        #check for blackjack
        for x in range(players):
            value = playerhands[x+1].check_value()
            if value == 21:
                playerhands[x+1].blackjack = True
            
        
        #turns
        for x in range(players):
            done = False
            while not(done):
                m = playerhands[x+1].check_value()
                if not(playerhands[x+1].bust or playerhands[x+1].blackjack):
                    if m >= 21:
                        playerhands[x+1].bust = True        
                        print(f"Player {x+1} has busted")
                        done = True
                if not(playerhands[x+1].bust or playerhands[x+1].blackjack):
                    while True: 
                        turnin = input(f"player {x+1} do you want to hit(type h) stand(type type st) double down(type d) or split a pair(type sp)?")
                        if turnin == "h":
                            y = deck.deck.pop()
                            card = y[0]
                            suit = y[1]
                            if card == 'Ace':
                                while True: 
                                    acetype = input(f"player {x+1} has received an ace. do you want it to be worth 11 or 1? 1/11 ")
                                    if acetype == "1":
                                        playerhands[x+1].add_card("Ace1",suit) 
                                        break
                                    elif acetype == "11":
                                        playerhands[x+1].add_card("Ace11",suit)
                                        break
                                    else:
                                        print("try again you have not inputed 1 or 11") 
                                
                            else:
                                print(f"\nplayer {x+1} has received a {Card(card,suit)}")
                                playerhands[x+1].add_card(card,suit)
                            print("\n the curent hands are -\n---------------------")
                            for x in range(players):
                                z = str(playerhands[x+1])
                                m = playerhands[x+1].check_value()
                                print(f"\nPlayer {x+1} has - a {z}. which has a value of {m}")
                            visible_dealer_card = ()
                            if playerhands["dealer"].cards[0][0] == "Ace":
                                visible_dealer_card = ("Ace",playerhands["dealer"].cards[0][1])
                            else:    
                                visible_dealer_card = playerhands["dealer"].cards[0]
                            print(f"\nThe dealer has a {visible_dealer_card[0]} of {visible_dealer_card[1]} and a hidden card")
                            break
                        elif turnin == "st":
                            print("\nstand\n")
                            done = True
                            break
                        elif turnin == "d":
                            if bank[x+1].money >= (bets[x+1] * 2):
                                bets[x+1] = bets[x+1] * 2
                                print("\nbet doubled.\n")
                                y = deck.deck.pop()
                                card = y[0]
                                suit = y[1]
                                if card == 'Ace':
                                    while True: 
                                        acetype = input(f"player {x+1} has received an ace. do you want it to be worth 11 or 1? 1/11 ")
                                        if acetype == "1":
                                            playerhands[x+1].add_card("Ace1",suit) 
                                            break
                                        elif acetype == "11":
                                            playerhands[x+1].add_card("Ace11",suit)
                                            break
                                        else:
                                            print("try again you have not inputed 1 or 11") 
                                    
                                else:
                                    print(f"\nplayer {x+1} has received a {Card(card,suit)}")
                                    playerhands[x+1].add_card(card,suit)
                                print("\n the curent hands are -\n---------------------")
                                for x in range(players):
                                    z = str(playerhands[x+1])
                                    m = playerhands[x+1].check_value()
                                    print(f"\nPlayer {x+1} has - a {z}. which has a value of {m}")
                                visible_dealer_card = ()
                                if playerhands["dealer"].cards[0][0] == "Ace":
                                    visible_dealer_card = ("Ace",playerhands["dealer"].cards[0][1])
                                else:    
                                    visible_dealer_card = playerhands["dealer"].cards[0]
                                print(f"\nThe dealer has a {visible_dealer_card[0]} of {visible_dealer_card[1]} and a hidden card")
                                
                            else:
                                print("not enugh money do a different action.\n")
                                break
                        elif turnin == "sp":
                            if len(playerhands[x+1].cards) == 2 and playerhands[x+1].cards[0][0] == playerhands[x+1].cards[1][0]:
                                o = len(playerhands)
                                playerhands[o] = Hand(x+1)
                                players += 1
                                bets[o] = Bank()
                                bets[o].deposit(bets[x+1].money)
                                print(f"player {x+1}. your new hand will be called Player {o}")
                                y = playerhands.cards.pop()
                                card = y[0]
                                suit = y[1]
                                if card == 'Ace':
                                    while True: 
                                        acetype = input(f"player {o} has received an ace. do you want it to be worth 11 or 1? 1/11 ")
                                        if acetype == "1":
                                            playerhands[o].add_card("Ace1",suit) 
                                            break
                                        elif acetype == "11":
                                            playerhands[o].add_card("Ace11",suit)
                                            break
                                        else:
                                            print("try again you have not inputed 1 or 11") 
                                    
                                else:
                                    print(f"\nplayer {o} has received a {Card(card,suit)}")
                                    playerhands[o].add_card(card,suit)
                                print("\n the curent hands are -\n---------------------")
                                for x in range(players):
                                    z = str(playerhands[x+1])
                                    m = playerhands[x+1].check_value()
                                    print(f"\nPlayer {x+1} has - a {z}. which has a value of {m}")
                                visible_dealer_card = ()
                                if playerhands["dealer"].cards[0][0] == "Ace":
                                    visible_dealer_card = ("Ace",playerhands["dealer"].cards[0][1])
                                else:    
                                    visible_dealer_card = playerhands["dealer"].cards[0]
                                print(f"\nThe dealer has a {visible_dealer_card[0]} of {visible_dealer_card[1]} and a hidden card")
                            else:
                                print("you do not have a pair")
                            break
                        else:
                            print("try again you have not inputed a valid input") 
                        print("\n the curent hands are -\n---------------------")
                        for x in range(players):
                            z = str(playerhands[x+1])
                            m = playerhands[x+1].check_value()
                            print(f"\nPlayer {x+1} has - a {z}. which has a value of {m}")
                else:
                    print(f"\nPlayer {x+1} is busted\n")
                    done = True
                    
        #dealer actions
            #show hidden card
        strdealer = "dealer"
        print(f"\nThe dealer will now reveal the hidden car\n----------------------------------------\nThe dealer has a {str(playerhands[strdealer])} which has a value of {playerhands[strdealer].check_value()}")
            #draw until 17
        while True:
            if playerhands[strdealer].check_value() < 17:
                y = deck.deck.pop()
                card = y[0]
                suit = y[1]
                if card == 'Ace':
                    if playerhands["dealer"].check_value() + 11 > 21:
                        ace = "Ace"
                        print(f"the dealer has received a {Card(ace,suit)} and is counting it as a value of 1")
                        playerhands["dealer"].add_card("Ace1",suit) 
                        
                    else:
                        ace = "Ace"
                        print(f"the dealer has received a {Card(ace,suit)} and is counting it as a value of 11")
                        playerhands["dealer"].add_card("Ace11",suit) 
                    
                else:
                    print(f"the dealer has received a {Card(card,suit)}")
                    playerhands["dealer"].add_card(card,suit)
            else:
                print("the dealer will stop drawing because his value is equal or over 17")
                break
        #display hands
        print("\n the curent hands are -\n---------------------")
        for x in range(players):
            z = str(playerhands[x+1])
            m = playerhands[x+1].check_value()
            print(f"\nPlayer {x+1} has - a {z}. which has a value of {m}")
        visible_dealer_card = ()
        if playerhands["dealer"].cards[0][0] == "Ace":
            visible_dealer_card = ("Ace",playerhands["dealer"].cards[0][1])
        else:    
            visible_dealer_card = playerhands["dealer"].cards[0]
        print(f"The dealer has a {str(playerhands[strdealer])} which has a value of {playerhands[strdealer].check_value()}")
        #win calc and disp
        win_check_results = {}
        for x in range(players):
            if not(playerhands[x+1].bust or playerhands[x+1].blackjack):
                if playerhands[x+1].check_value() > playerhands["dealer"].check_value():
                    win_check_results[x+1] = "win"
                else:
                    win_check_results[x+1] = "lose"
            elif playerhands[x+1].bust:
                win_check_results[x+1] = "bust"
            elif playerhands[x+1].blackjack:
                win_check_results[x+1] = "blackjack"
        #   disp
        print("\n\n these are the results of this hand")
        for x in range(len(win_check_results)-1):
            counter += 1
            if win_check_results[counter] == "blackjack":
                player = playerhands[counter].belongs_to
                print(f"Player {x+1} has won with a blackjack! therefore Player {player} will recieve his bet back and will get an extra 1.5 times his bet payed to him")
            elif win_check_results[counter] == "bust":
                player = playerhands[counter].belongs_to
                print(f"Player {x+1} has busted. therefore Player {player} lose the money of his bet.")
            elif win_check_results[counter] == "win":
                player = playerhands[counter].belongs_to
                print(f"Player {x+1} has won! therefore Player {player} will recieve his bet back and will get an extra of his bet payed to him again")
            else:
                player = playerhands[counter].belongs_to
                print(f"Player {x+1} has lost but has not busted. therefore Player {player} will recieve his bet back")
        
        #pay win
        counter = 0
        for x in range(len(win_check_results)-1):
            counter += 1
            if win_check_results[counter] == "blackjack":
                player = playerhands[counter].belongs_to
                Bank[player].deposit((bets[counter].money * 1.5))
            elif win_check_results[counter] == "bust":
                player = playerhands[counter].belongs_to
                Bank[player].withdraw((bets[counter].money))
            else:
                player = playerhands[counter].belongs_to
                Bank[player].deposit((bets[counter].money))
        input("\nRestarting game...\n-------------\nnew hand.\npress enter to start the next hand")
        
        
    #play again? q
    stop = False
    while True:
         againq = input("do you want to play again? y/n ")
         if againq.lower() == "y":
              stop = False
              print("\n\nstarting game...\n")
              suits = ("Hearts","Diamonds","Spades","Clubs")
              ranks = ("Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace")
              values = {"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":10,"Queen":10,"King":10,"Ace11":11,"Ace1":1}
              playerhands = {}
              players = 0
              bets = {}
              turn = 0
              decks_num = 0
              deck = 0
              min_bet = 0
              bank = {}
              break
         elif againq.lower() == "n":
             stop = True 
             break
         else:
             print("you have not inputed y/n. closing.")
             stop = True 
             break
    if stop:
        break
input("press enter to close")