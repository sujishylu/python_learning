# tressure island learning the if conditional operator

print("you are wanting to go to a tressure island which transport you want to take ?")
descison1 = input("train or car or bike?")
if descison1.lower().strip() == "train":
    print("Game Over")
elif descison1.lower().strip() == "car":
        descion2 = input("which place you need to go river side mountain dessert ?")
        if descion2.lower() == "river side":
            print( "well done ")
            descision3 = input(" which color box you want to open 1 , 2 or 3 ??")
            if descision3.strip() == '1':
                    print(" you found the tressure!!!")
            else:
                    print( "Game Over!!")
        else:
            print("Game Over!!!")
else:
    print( " Game OVer!!!")

