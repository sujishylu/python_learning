#learning random
import random

#print(random.randint(1,5) +random.random().__round__(4))

# print(random.random()*6)
game_list = ['rock','paper','scissors']
conti_flag = True

while conti_flag != False :
    your_choice = input("input rock paper or scissors")
    i= random.randint(0, 2)
    comp_choice = game_list[i]
    print ( comp_choice)
    print(type(comp_choice))

    if ( your_choice == "rock" and  str(comp_choice) == "scissors" ):
        print ("  computer win ")
    elif (your_choice == "rock" and comp_choice == "paper" ):
                print (  " you win ")
    elif (your_choice == "rock"  and comp_choice == "rock" ):
                print( "draw")
    elif (your_choice == "paper"):
        if (comp_choice == "rock"):
            print("you win")
        elif (comp_choice == "scissors" ):
                print("comp win")
        else:
                print("draw")
    elif( your_choice == 'scissors'):
        if (comp_choice == "rock"):
                print("Comp win")
        elif (comp_choice =="scissors"):
                print("draw")
        else:
                print("you win")

    conti_flag = True if input ( " do you want to continue?") == "Y" else False

