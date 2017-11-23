#coding: utf-8


# Created by: Anthony Freeman
# Created on: 2017
# Created for: ICS3U
import ui
import random 
#card values
card1 = random.randint(1, 10)
card2 = random.randint(1, 10)
card3 = random.randint(1, 10)
dealercard1 = random.randint(1, 10)
dealercard2 = random.randint(1, 10)
dealercard3 = random.randint(1, 10)

def deal_cards(sender):
    #deals cards
    global card1 
    global card2
    view['yourcard1label'].text = '{:,.2f}'.format(card1)
    view['yourcard2label'].text = '{:,.2f}'.format(card2)
#determines winner
def determine_winner(player,dealer):
    global dealercard1
    global dealercard2
    global dealercard3
    print(player,dealer)
    view['dealercard1label'].text = '{:,.2f}'.format(dealercard1)
    view['dealercard2label'].text = '{:,.2f}'.format(dealercard2)
    view['dealercard3label'].text = '{:,.2f}'.format(dealercard3)
    if ((player > 21 and dealer > 21) or (dealer == player)):
      view['outcomelabel'].text = 'draw'
    elif ((player > dealer)and (player <= 21)):
      view['outcomelabel'].text = 'you win'
    elif ((dealer > player) and (dealer <= 21)):
      view['outcomelabel'].text = 'you lose'
    else:
      view['outcomelabel'].text = 'you are the village idiot'
#if you hit
def hit(sender):
    global card1
    global card2
    global card3
    global dealercard1
    global dealercard2
    global dealercard3
    view['yourcard3label'].text = '{:,.2f}'.format(card3)
    yourtotal = card1 + card2 + card3
    dealertotal = dealercard1 + dealercard2 + dealercard3
    determine_winner(yourtotal,dealertotal)
#if you stand
def stand(sender):
    global card1
    global card2
    global dealercard1
    global dealercard2
    global dealercard3
    yourtotal = card1 + card2
    dealertotal = dealercard1 + dealercard2 + dealercard3
    determine_winner(yourtotal,dealertotal)



view = ui.load_view()
view.present('fullscreen')
