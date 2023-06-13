#its a game
import random
def pick_card( pack_of_cards):
    """this function will pick  card in random for you"""
    one_card = random.choice(pack_of_cards)
    return int(one_card)
def remove_card(x,l):
    new_list = l.pop(x)
    return new_list
playing_card =[1,2,3,4,5,6,7,8,9,10,10,10,10]*4
your_card=[]
comp_card=[]
i = input("do you want to conntionue ? Y/N")
while i.strip() == 'Y':
    one_card = pick_card(playing_card)
    your_card.append(one_card)
    playing_card.pop(one_card)
    one_card = pick_card(playing_card)
    comp_card.append(one_card)
    playing_card.pop(one_card)
    print("your_card", your_card)
    i = input("do you want to conntionue ? Y/N")
print("your list", your_card)
print("computer_list", comp_card)
if sum(your_card) > sum(comp_card):
    print("you win!")
elif sum(your_card) < sum(comp_card):
    print("comp win!")

else :
    print("darw")



