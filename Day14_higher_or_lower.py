# build a game . give a list of personality and followers
import random
insta_follower = [
    {"name": "Nayanan",
     "followers": 12800,
     "description": "Actor"
     },
    {"name": "Vijay",
     "followers": 1234,
     "description": "Actor"
     },
    {"name": "Rajini",
     "followers": 99999,
     "description": "Actor"
     }
]
score = 0
def question():
    r1,r2 = random.sample(insta_follower,2)
    answer = input("which has more followers A/B)"+ "A: " + r1["name"] + "\n " + "B"+ r2["name"] )
    if r1["followers"] >r2["followers"] and answer == 'A':
        print (" right")
        return True
    elif r1["followers"] < r2["followers"] and answer == 'B':
        print(" right")
        return True
    else:
        print("Wronng your game is over")
        return False

print("welcome to the higher lowee game")
if input( " do you want to start Y/N?") == "Y":
    bol = question()
    while bol:
        score = score + 1
        bol = question()

print(" your score is ", score)

